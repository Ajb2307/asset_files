from pathlib import Path
import sys


# functions to write parts of the asset file
def asset_outpath(datainfo):
    """
    Generate the output path for the asset file.
    :param datainfo: Metadata about the dataset.
    :type datainfo: dict of {str : list}
    :return: The output path for the asset file.
    :rtype: str
    """
    # Get the current working directory
    cwd = Path.cwd()
    
    # Create the output path using the current working directory and the asset name
    try:
        outfile = datainfo['filename'] + '.asset'
        outpath = cwd / datainfo['asset_dir']
    except KeyError:
        raise KeyError(f'need to set asset_dir in the datainfo dictionary')
        
    # Create the directory if it doesn't exist
    outpath.mkdir(parents=True, exist_ok=True)

    # Return the output path
    return outpath / outfile

def import_local_modules(datainfo):
        # importing local modules
        print('-- Set some parameters for OpenSpace settings')
        try:
            print(f'local data_file = asset.resource("{datainfo["data_file"]}")')
        except KeyError:
            raise KeyError(f'need to set data_file in the datainfo dictionary')

        if datainfo.get("texture") != None:
            print(f'local texture = asset.resource("{datainfo["texture"]}")')
        
        if datainfo.get("cmap") != None:
            print(f'local cmap = asset.resource("{datainfo["cmap"]}")')

        print()

def import_local_star_modules(datainfo):
        # importing local modules
        print('-- Set some parameters for OpenSpace settings')
        try:
            print(f'local data_file = asset.resource("{datainfo["data_file"]}")')
            print(f'local core_texture = asset.resource("{datainfo["core_texture"]}")')
            print(f'local glare_texture = asset.resource("{datainfo["glare_texture"]}")')
            print(f'local cmap = asset.resource("{datainfo["cmap"]}")')
            print(f'local other_cmap = asset.resource("{datainfo["other_cmap"]}")')
        except KeyError:
            raise KeyError(f'need to set data_file, core_texture, glare_texture, cmap, other_cmap in the datainfo dictionary')


        print()

def set_color_parameters(datainfo):
    # if color map is provided 
    if datainfo.get("cmap") != None:
        print('    Coloring = {')
        # provided fix color if applicable
        if datainfo.get("fixed_color") != None:
            print('      FixedColor = {' + datainfo["fixed_color"] +'},')
        print('      ColorMapping = {')
        print('        File = cmap,')
        print('        Enabled = ' + datainfo["colormap_enabled"] + ',')
        print('        ParameterOptions = {')
        
        ## input color map parameters
        for index, param in enumerate(datainfo["parameter_options"]):
            # not the last parameter, add a comma
            if index != len(datainfo["parameter_options"]) - 1:
                print('          { Key = "' + param["key"] + '", Range = {' + param["range"] + '} },')
            # last parameter, no comma
            else:
                print('          { Key = "' + param["key"] + '", Range = {' + param["range"] + '} }')
        print('        }')
        print('      }')
        print('    },')
    # if color map is not provided
    elif datainfo.get("fixed_color") != None:
        print('    Coloring = {')
        print('      FixedColor = {' + datainfo["fixed_color"] +'}')
        print('    },')
    
    # set opacity if provided
    if datainfo.get("Opacity") != None:
        print('    Opacity = ' + datainfo["Opacity"] + ',') #may change later

def set_size_parameters(datainfo):
    try:
        print('    SizeSettings = {') 
        if datainfo.get("SizeMapping_ParameterOptions") != None:
            print('      SizeMapping = {')
            print('        ParameterOptions = { "' + datainfo["SizeMapping_ParameterOptions"] + '" }')
            print('        },')
        print('      ScaleExponent = ' + datainfo["ScaleExponent"] + ',') 
        print('      MaxSize = ' + datainfo["MaxSize"] + ',')
        print('      EnableMaxSizeControl = true')
        print('     },')

    except KeyError:
        raise KeyError(f'need to set ScaleExponent and MaxSize in the datainfo dictionary')

def set_fading_parameters(datainfo):
    if datainfo.get("FadeInDistances") != None:
        print('    Fading = {')
        print('      FadeInDistances = {' + datainfo["FadeInDistances"] + '}')
        print('    },')

def set_label_parameters(datainfo):
    ## input label settings if csv_labels = True
    if datainfo.get("csv_labels") == True:

        # check if label column name is provided
        if datainfo.get("label_column") != None:
            label_column = datainfo["label_column"]
        else:
            label_column = "label"
        
        try:
            print('    DataMapping = {')
            print('      Name = "' + label_column + '" },')
            print('    Labels = {')
            # this is used for star labels
            if datainfo.get("LabelEnabled") == True:
                print('      Enabled = true,')

            print('      Color = { ' + datainfo["LabelColor"] + ' },')
            print('      Size = ' + datainfo["LabelSize"] + ',')
            print('      MinMaxSize = { ' + datainfo["LabelMinMaxSize"] + ' },')
            print('      Unit = "' + datainfo["Unit"] + '"')
            print('    }')
        except KeyError:
            raise KeyError(f'need to set LabelColor, LabelSize, and LabelMinMaxSize in the datainfo dictionary if csv_labels = True')

def define_GUI(datainfo):
    """
    Define the GUI settings for the asset file.
    :param datainfo: Metadata about the dataset.
    :type datainfo: dict of {str : list}
    """
    # GUI settings
    try:
        print('  GUI = {')
        print('    Name = "' + datainfo['gui_name'] + '",')
        print('    Path = "' + datainfo['gui_path'] + '",')
        print('    Description = [[' + datainfo['description'] + ']]')
        print('  }') # end of GUI
        print()
    except KeyError:
        raise KeyError(f'need to set gui_name, gui_path, and description in the datainfo dictionary')
    
def asset_metadata(datainfo):

    try:
        print('asset.meta = {')
        print('  Name = "' + datainfo["meta_name"] + '",')
        print('  Description = Object.GUI.Description,')
        print('  Author = "' + datainfo["author"] + '",')
        print('  URL = "https://www.amnh.org/research/hayden-planetarium/digital-universe",')
        print('  License = "AMNH Digital Universe"')
        print('}')
    
    except KeyError:
        raise KeyError(f'need to set meta_name, author, and license in the datainfo dictionary')

def initialize_asset_functions(Object = "Object"):
    """
    Initialize the asset functions for the asset file.
    :param datainfo: Metadata about the dataset.
    :type datainfo: dict of {str : list}
    """
    print('asset.onInitialize(function()')
    print('    openspace.addSceneGraphNode(' + Object + ')')
    print('end)')
    print()
    print('asset.onDeinitialize(function()')
    print('    openspace.removeSceneGraphNode(' + Object + ')')
    print('end)')
    print()
    print('asset.export(' + Object + ')')
    print()
    print()

# function to create the asset file for various renderables
def make_RenderablePointCloud_asset(datainfo):
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
    ## Save the original stdout so we can switch back later
    original_stdout = sys.stdout
    ## Open the file to write to
    outpath = asset_outpath(datainfo)

    with open(outpath, 'wt') as asset:
        # Switch stdout to the file
        sys.stdout = asset
        
        # Print the header
        print("-- This file is auto-generated in the " + make_RenderablePointCloud_asset.__name__ + "() function inside " + Path(__file__).name)
        print()
        
        import_local_modules(datainfo)

        # START OF OBJECT 
        print('local Object = {')
        print('  Identifier = "' + datainfo['identifier'] + '",')
        # START OF RENDERABLE
        print('  Renderable = {')
        print('    Type = "RenderablePointCloud",')
        
        # input file settings
        print('    File = data_file,')
        print('    Unit = "' + datainfo["Unit"] + '",')
        print('    Enabled = ' + datainfo["Enabled"] + ',')
        
        # color, opacity, texture, size settings
        set_color_parameters(datainfo)
        ## input texture settings
        print('    Texture = {')
        print('      File = texture },')
        ## size settings
        set_size_parameters(datainfo)
        ## fading settings
        set_fading_parameters(datainfo)
        ## input label settings if csv_labels = True
        set_label_parameters(datainfo)
        
        print('  },') # END OF RENDERABLE
        
        # input GUI settings
        define_GUI(datainfo)

        print('}') # END OF OBJECT
        print()

        # initialize asset functions 
        initialize_asset_functions()

        # Print the metadata for the asset
        asset_metadata(datainfo)
    
    # Close the file and switch back to original stdout
    sys.stdout = original_stdout

    # Report to stdout
    print()

def make_star_labels_asset(datainfo):
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
    ## Save the original stdout so we can switch back later
    original_stdout = sys.stdout
    ## Open the file to write to
    outpath = asset_outpath(datainfo)

    # set label enabled to true
    datainfo["LabelEnabled"] = True

    with open(outpath, 'wt') as asset:
        # Switch stdout to the file
        sys.stdout = asset

        # Print the header
        print("-- This file is auto-generated in the " + make_star_labels_asset.__name__ + "() function inside " + Path(__file__).name)
        print()
        
        import_local_modules(datainfo)

        # START OF OBJECT 
        print('local Object = {')
        print('  Identifier = "' + datainfo['identifier'] + '",')
        # START OF RENDERABLE
        print('  Renderable = {')
        print('    File = data_file,')
        print('    Type = "RenderablePointCloud",')
        print('    Enabled = ' + datainfo["Enabled"] + ',')
        
        # opacity, units, size settings
        print('    Opacity = ' + datainfo["Opacity"] + ',')
        print('    Unit = "' + datainfo["Unit"] + '",')
        print('    SizeSettings = {') 
        print('      ScaleExponent = 0,') 
        print('      MaxSize = 0,')
        print('      EnableMaxSizeControl = false')
        print('     },')

        ## input label settings if csv_labels = True
        set_label_parameters(datainfo)
        
        print('  },') # END OF RENDERABLE
        
        # input GUI settings
        define_GUI(datainfo)

        print('}') # END OF OBJECT
        print()

        # initialize asset functions 
        initialize_asset_functions()

        # Print the metadata for the asset
        asset_metadata(datainfo)
    
    # Close the file and switch back to original stdout
    sys.stdout = original_stdout

    # Report to stdout
    print()

def make_RenderablePolygonCloud_asset(datainfo):
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
    ## Save the original stdout so we can switch back later
    original_stdout = sys.stdout
    ## Open the file to write to
    outpath = asset_outpath(datainfo)

    with open(outpath, 'wt') as asset:
        # Switch stdout to the file
        sys.stdout = asset
        
        # Print the header
        print("-- This file is auto-generated in the " + make_RenderablePolygonCloud_asset.__name__ + "() function inside " + Path(__file__).name)
        print()
        
        import_local_modules(datainfo)

        # START OF OBJECT 
        print('local Object = {')
        print('  Identifier = "' + datainfo['identifier'] + '",')
        # START OF RENDERABLE
        print('  Renderable = {')
        print('    Type = "RenderablePolygonCloud",')
        print('    Enabled = ' + datainfo["Enabled"] + ',')
        
        # input file settings
        print('    File = data_file,')
        print('    Unit = "' + datainfo["Unit"] + '",')
        print('    PolygonSides = ' + datainfo["PolygonSides"] + ',')
        
        # color, opacity, texture, size settings
        set_color_parameters(datainfo)

        ## size settings
        set_size_parameters(datainfo)
        ## fading settings
        set_fading_parameters(datainfo)
        ## input label settings if csv_labels = True
        set_label_parameters(datainfo)
        
        print('  },') # END OF RENDERABLE
        
        # input GUI settings
        define_GUI(datainfo)

        print('}') # END OF OBJECT
        print()

        # initialize asset functions 
        initialize_asset_functions()

        # Print the metadata for the asset
        asset_metadata(datainfo)
    
    # Close the file and switch back to original stdout
    sys.stdout = original_stdout

    # Report to stdout
    print()

def make_RenderableStars_asset(datainfo):
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
    ## Save the original stdout so we can switch back later
    original_stdout = sys.stdout
    ## Open the file to write to
    outpath = asset_outpath(datainfo)

    with open(outpath, 'wt') as asset:
        # Switch stdout to the file
        sys.stdout = asset
        
        # Print the header
        print("-- This file is auto-generated in the " + make_RenderableStars_asset.__name__ + "() function inside " + Path(__file__).name)
        print()
        
        import_local_star_modules(datainfo)

        # START OF OBJECT 
        print('local Object = {')
        print('  Identifier = "' + datainfo['identifier'] + '",')
        # START OF RENDERABLE
        print('  Renderable = {')
        print('    Type = "RenderableStars",')

        # input file settings
        print('    File = data_file,')
        
        # input glare and halo settings
        print('    Core = {')
        print('      Texture = core_texture,')
        print('      Multiplier = 15.0,')
        print('      Gamma = 1.66,')
        print('      Scale = 0.18')
        print('      },')
        print('    Glare = {')
        print('      Texture = glare_texture,')
        print('      Multiplier = 0.65')
        print('      },')
        
        ## misc color size settings
        print('    MagnitudeExponent = 6.325,')
        print('    ColorMap = cmap,')
        print('    OtherDataColorMap = other_cmap,')
        print('    SizeComposition = "Distance Modulus",')
        
        print('    DataMapping = {')
        print('      Bv = "' + datainfo['Bv_column']+'",')
        print('      Luminance = "' + datainfo['Luminance_column']+'",')
        print('      AbsoluteMagnitude = "' + datainfo['AbsoluteMagnitude_column']+'",')
        print('      ApparentMagnitude = "' + datainfo['ApparentMagnitude_column']+'",')
        print('      Vx = "' + datainfo['Vx_column']+'",')
        print('      Vy = "' + datainfo['Vy_column']+'",')
        print('      Vz = "' + datainfo['Vz_column']+'",')
        print('      Speed = "' + datainfo['Speed_column']+'",')
        print('    },')
        
        print('    DimInAtmosphere = true')
        
        print('  },') # END OF RENDERABLE
        
        print('  Tag = { "daytime_hidden" },')

        # input GUI settings
        define_GUI(datainfo)

        print('}') # END OF OBJECT
        print()

        # initialize asset functions 
        initialize_asset_functions()

        # Print the metadata for the asset
        asset_metadata(datainfo)
    
    # Close the file and switch back to original stdout
    sys.stdout = original_stdout

    # Report to stdout
    print()
     

# master function to write the asset file
# This function will call the appropriate asset creation function based on the datainfo provided.
def write_asset(datainfo):
    """
    Write the asset file for the deep sky survey data.
    :param datainfo: Metadata about the dataset.
    :type datainfo: dict of {str : list}
    """

    if datainfo["renderable"] == "RenderablePointCloud":
        make_RenderablePointCloud_asset(datainfo)   
    
    elif datainfo["renderable"] == "StarLabels":
        make_star_labels_asset(datainfo)
    
    elif datainfo["renderable"] == "RenderablePolygonCloud":
        make_RenderablePolygonCloud_asset(datainfo)
    
    elif datainfo["renderable"] == "RenderableStars":
        make_RenderableStars_asset(datainfo)
