from pathlib import Path
import sys

def make_RPC_asset(datainfo):
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
    outpath = Path.cwd() / datainfo['asset_dir'] / outfile
    with open(outpath, 'wt') as asset:
        # Switch stdout to the file
        sys.stdout = asset
        # Print the header
        print("-- This file is auto-generated in the " + make_RPC_asset.__name__ + "() function inside " + Path(__file__).name)
        print()

        # importing local modules
        print('-- Set some parameters for OpenSpace settings')
        print(f'local csv = asset.resource("{datainfo["csv"]}")')
        print(f'local texture = asset.resource("{datainfo["texture"]}")')
        if datainfo["cmap"] != "":
            print(f'local cmap = asset.resource("{datainfo["cmap"]}")')

        print()

        # creating local object 
        print('local Object = {')
        print('  Identifier = "' + datainfo['identifier'] + '",')
        print('  Renderable = {')
        print('    Type = "RenderablePointCloud",')
        
        # input file settings
        print('    File = csv,')
        print('    Unit = "' + datainfo["Unit"] + '",')
        print('    Enabled = ' + datainfo["Enabled"] + ',')
        
        # color, opacity, texture, size settings
        print('    Opacity = ' + datainfo["Opacity"] + ',') #may change later

        if datainfo["cmap"] != "":
            print('    Coloring = {')
            print('      FixedColor = {' + datainfo["fixed_color"] +'},')
            print('      ColorMapping = {')
            print('        File = cmap,')
            print('        Enabled = ' + datainfo["colormap_enabled"] + ',')
            print('        ParameterOptions = {')
            ## input color map parameters
            for index, param in enumerate(datainfo["parameter_options"]):
                if index != len(datainfo["parameter_options"]) - 1:
                    print('          { Key = "' + param["key"] + '", Range = {' + param["range"] + '} },')
                else:
                    print('          { Key = "' + param["key"] + '", Range = {' + param["range"] + '} }')
            print('        }')
            print('      }')
            print('    },')
        elif datainfo["fixed_color"] != "":
            print('    Coloring = {')
            print('      FixedColor = {' + datainfo["fixed_color"] +'}')
            print('    },')
        ## input texture settings
        print('    Texture = {')
        print('      File = texture')
        print('        },')
        ## size settings
        print('    SizeSettings = {') 
        print('      ScaleExponent = ' + datainfo["ScaleExponent"] + ',') 
        print('      MaxSize = ' + datainfo["MaxSize"] + ',')
        print('      EnableMaxSizeControl = true')
        print('     },')

        ## input label settings if labels = True
        if datainfo["Labels"] == True:
            print('    DataMapping = {')
            print('      Name = "label" },')
            print('    Labels = {')
            print('      Color = { ' + datainfo["LabelColor"] + ' },')
            print('      Size = ' + datainfo["LabelSize"] + ',')
            print('      MinMaxSize = { ' + datainfo["LabelMinMaxSize"] + ' },')
            print('      Unit = "' + datainfo["Unit"] + '"')
            print('    }')

        print('  },')
        
        # input GUI settings
        print('  GUI = {')
        print('    Name = "' + datainfo['gui_name'] + '",')
        print('    Path = "' + datainfo['gui_path'] + '",')
        print('    Description = [[' + datainfo['description'] + ']]')
        print('  }')
        print('}')
        print()

        # initialize asset functions 
        print('asset.onInitialize(function()')
        print('    openspace.addSceneGraphNode(Object)')
        print('end)')
        print()
        print('asset.onDeinitialize(function()')
        print('    openspace.removeSceneGraphNode(Object)')
        print('end)')
        print()
        print('asset.export(Object)')

        print()
        print()

        # Print the metadata for the asset
        print('asset.meta = {')
        print('  Name = "' + datainfo["meta_name"] + '",')
        print('  Description = Object.GUI.Description,')
        print('  Author = "' + datainfo["author"] + '",')
        print('  URL = "https://www.amnh.org/research/hayden-planetarium/digital-universe",')
        print('  License = "AMNH Digital Universe"')
        print('}')
        print()
    
    # Close the file and switch back to original stdout
    sys.stdout = original_stdout
 
    # Report to stdout
    print()


    