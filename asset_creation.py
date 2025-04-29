from pathlib import Path
import sys

def make_dss_asset(datainfo):
    """
    Generate the asset file for the deep sky survey data.
    :param datainfo: Metadata about the dataset.
    :type datainfo: dict of {str : list}
    Output files:
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    :file:`[{order}]/[{version}]/consensus_species.asset`
        The asset file containing the OpenSpace configurations for the consensus species.
    """
    # We shift the stdout to our filehandle so that we don't have to keep putting
    # the filehandle in every print statement.
    # Save the original stdout so we can switch back later
    original_stdout = sys.stdout

    # Open the file to write to
    outfile = datainfo['filename'] + '.asset'
    outpath = Path.cwd() / datainfo['dir'] / datainfo['catalog_directory'] / outfile
    with open(outpath, 'wt') as asset:
        # Switch stdout to the file
        sys.stdout = asset
        # Print the header
        print("-- This file is auto-generated in the " + make_asset.__name__ + "() function inside " + Path(__file__).name)
        print()

        # importing local modules
        print('-- Set some parameters for OpenSpace settings')
        print(f'local csv = asset.resource("{datainfo["csv"]}")')
        print(f'local texture = asset.resource("{datainfo["texture"]}")')
        print(f'local cmap = asset.resource("{datainfo["cmap"]}")')

        print()

        # creating local object 
        print('local Object')
        print('    Identifier = "' + datainfo['identifier'] + '",')
        print('    Renderable = {')
        print('        Type = "RenderablePointCloud",')
        print('        Coloring = {')
        print('            FixedColor = {' + datainfo["fixed_color"] +'},')
        print('            ColorMap = {')
        print('                File = cmap,')
        print('                Enabled = true,') #issue quasar is false
        print('                ParameterOptions = {')
        # input color map parameters
        for param in datainfo["parameter_options"]:
            print('          { Key = "' + param["key"] + '", Range = {' + param["range"] + '} }')
        print('                },')
        print('        Opacity = 1.0,') #may change later
        print('        SizeSettings = {') 
        print('          ScaleExponent = ' + datainfo["ScaleExponet"] + ',') 
        print('          MaxSize = ' + datainfo["MaxSize"] + ',')
        print('          EnableMaxSizeControl = true')
        print('        },')
        print('        File = csv,')
        print('        Unit = "Mpc",')
        print('        Enabled = false,')
        print('        Texture = {')
        print('            File = texture')
        print('        },')
        print('    },')
        print('    GUI = {')
        print('        Name = "' + datainfo['gui_name'] + '",')
        print('        Path = "' + datainfo[file]['gui_path'] + '",')
        print('        Description = [[' + datainfo['description'] + ']],')
        print('    }')
        print('}')
        print()


        print('asset.onInitialize(function()')
        print('    openspace.addSceneGraphNode(Object)')
        print('end)')
        print()
        print('asset.onDeinitialize(function()')
        print('    openspace.removeSceneGraphNode(Object)')
        print('end)')
        print()
        print('asset.export(Object)')

        print('asset.meta = {')
        print('  Name = "' + datainfo["name"] + '",')
        print('  Description = Object.GUI.Description,')
        print('  Author =' + datainfo["author"] + ',')
        print('  URL = "https://www.amnh.org/research/hayden-planetarium/digital-universe",')
        print('  License = "AMNH Digital Universe"')
        print('}')
        print()
    sys.stdout = original_stdout
 
    # Report to stdout
    print()