master_dictionary = {
    '2dF': {
        "renderable": "RenderablePointCloud",
        "Enabled": "false",
        "filename": "2df",
        "asset_dir": "twodF",
        "data_file": "2df.csv",
        "Unit": "Mpc",
        "texture": "point3A.png",
        "cmap": "2df.cmap",
        "identifier": "2dF_test",
        "fixed_color": "1.0, 1.0, 1.0", # not used
        "Opacity": "1.0",
        "colormap_enabled": "true",
        "parameter_options": [{"key": "num_nearby_galaxies", "range": "1.0, 25.0"},
                            {"key": "redshift", "range": "0.0, 0.075"}],
        "ScaleExponent": "22.6",
        "MaxSize": "0.2",
        "csv_labels": False,
        "LabelColor": None,
        "LabelSize": None,
        "LabelMinMaxSize": None,
        "gui_name": "2dF Galaxies -test",
        "gui_path": "/Universe/Deep Sky Surveys",
        "description": """The Two-degree Field (2dF) Survey was a project designed to map 
        portions of the extragalactic universe. The 2dF survey has three main components: 
        the North Galactic Pole strip, the South Galactic Pole strip, and the random fields
        that surround the South Galactic Pole strip. Colors: Orange galaxies show dense 
        regions of galaxies, aqua galaxies are areas of intermediate density, and green
        galaxies are areas of lower density. Census: 229,293 galaxies.""",
        "meta_name": "2dF Galaxies",
        "author": "Brian Abbott (AMNH), Eric Gawiser (Rutgers U), Ally Baldelli (AMNH)",
        },
    'brown_dwarfs': {
        "renderable": "RenderablePointCloud",
        "Enabled": "false",
        "filename": "bd",
        "asset_dir": "brown_dwarf",
        "data_file": "bd.csv",
        "Unit": "pc",
        "texture": "point3.png",
        "cmap": "bd.cmap",
        "identifier": "BrownDwarfs_test",
        "fixed_color": "0.4, 0.0, 0.1",
        "Opacity": "1.0",
        "colormap_enabled": "true",
        "parameter_options": [{"key": "typeindex", "range": "1.0, 4.0"}],
        "ScaleExponent": "15.8",
        "MaxSize": "0.7",
        "csv_labels": True,
        "LabelColor": "0.6, 0.3, 0.4",
        "LabelSize": "13.75",
        "LabelMinMaxSize": "10, 100",
        "gui_name": "Brown Dwarfs -test",
        "gui_path": "/Milky Way/Substellar Objects",
        "description": r"""For decades it was believed that M stars were the coolest stars in
        the Galaxy. Some M stars, called red dwarfs, make up 70% of the stars in the
        Galaxy. However, a new class of objects, even cooler than M stars, was recently
        discovered and given a spectral type of L. L-type objects straddle the boundary
        between red dwarfs and brown dwarfs and they are typically very dim stars or brown
        dwarfs. Even cooler than L-type objects are T-type objects. These are mostly brown
        dwarfs and resemble large, massive, Jupiter-like objects, too large to be planets
        and typically too small to be stars. Beyond the T dwarfs are the Y-type objects,
        which are even more dim. Brown dwarfs are extremely difficult to see, mainly because
        they are so dim in optical light. However, they appear brighter in infrared light.
        Colors: We represent these objects as exaggerated points and they are either red
        for L type objects, Maroon for T type, and purple for Y type objects. Census:
        2,196 objects.""",
        "meta_name": "Brown Dwarfs",
        "author": "Brian Abbott, Zack Reeves, Jackie Faherty, Ally Baldelli (AMNH)",
    },
    '6dF': {
        "renderable": "RenderablePointCloud",
        "Enabled": "false",
        "filename": "6df",
        "asset_dir": "sixdF",
        "data_file": "6df.csv",
        "texture": "point3A.png",
        "Unit": "Mpc",
        "cmap": "6df.cmap",
        "identifier": "6dF_test",
        "fixed_color": "1.0, 1.0, 0.0",
        "Opacity": "1.0",
        "colormap_enabled": "true",
        "parameter_options": [
            {"key": "num_nearby_galaxies", "range": "1.0, 10.0"},
            {"key": "redshift", "range": "0.0, 0.075"}
        ],
        "ScaleExponent": "22.5",
        "MaxSize": "0.2",
        "csv_labels": False,
        "LabelColor": None,
        "LabelSize": None,
        "LabelMinMaxSize": None,
        "gui_name": "6dF Galaxies -test",
        "gui_path": "/Universe/Deep Sky Surveys",
        "description": """The Six-degree Field (6dF) Galaxy Survey mapped nearly half the sky
        from the Anglo-Australian Observatory. Because it's a southern hemisphere survey,
        there is no coverage in these data for the northern hemisphere's sky. As with all
        galaxy surveys, the orange galaxies are in relatively dense areas, the green
        galaxies are in relatively sparse areas, and the aqua galaxies are between. Census:
        109,569 galaxies.""",
        "meta_name": "6dF Galaxies",
        "author": "Brian Abbott, Ally Baldelli (AMNH)",
    },
    'SDSS': {
        "renderable": "RenderablePointCloud",
        "filename": "sdss",
        "Enabled": "true",
        "asset_dir": "ssds",
        "data_file": "sdss.csv",
        "texture": "point3A.png",
        "cmap": "SDSSgals.cmap",
        "identifier": "SloanDigitalSkySurvey_test",
        "Unit": "Mpc",
        "fixed_color": "0.8, 0.8, 1.0",
        "Opacity": "0.8",
        "colormap_enabled": "true",
        "parameter_options": [{"key": "num_nearby_galaxies", "range": "1.0, 25.0"}],
        "ScaleExponent": "22.6",
        "MaxSize": "0.15",
        "FadeInDistances": "220.0, 650.0",
        "csv_labels": False,
        "LabelColor": None,
        "LabelSize": None,
        "LabelMinMaxSize": None,
        "gui_name": "Sloan Digital Sky Survey -test",
        "gui_path": "/Universe/Deep Sky Surveys",
        "description": r"""The Sloan Digital Sky Survey (SDSS) is an ambitious project to image
        about 35% of the sky, deep into the universe. The SDSS galaxies form triangular
        wedges, revealing those parts of the sky observed by the telescope. If the entire
        sky were covered, you would see a spherical distribution of galaxies surrounding
        the Milky Way. With only 35% of the entire sky observed, we see only a few select
        slices or larger wedgelike portions from that sphere. The weblike cosmic structure
        is echoed in these data, with orange clusters standing out among the less dense
        aqua-colored galaxies and the less dense regions of green-colored galaxies.
        Census: 2,862,767 galaxies.""",
        "meta_name": "Sloan Digital Sky Survey Galaxies",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH), Eric Gawiser (Rutgers)",
    },
    'white_dwarfs': {
        "renderable": "RenderablePointCloud",
        "filename": "wd",
        "asset_dir": "white_dwarfs",
        "Enabled": "false",
        "data_file": "wd.csv",
        "texture": "point3.png",
        "cmap": None,  # No colormap specified in the asset file
        "identifier": "WhiteDwarfs_test",
        "Unit": "pc",
        "fixed_color": "1.0, 1.0, 1.0",
        "Opacity": "1.0",
        "colormap_enabled": "false",
        "parameter_options": [],  # No parameter options specified in the asset file
        "ScaleExponent": "15.5",
        "MaxSize": "0.7",
        "csv_labels": False,
        "LabelColor": None,
        "LabelSize": None,
        "LabelMinMaxSize": None,
        "gui_name": "White Dwarfs- test",
        "gui_path": "/Milky Way/Stellar Remnants",
        "description": r"""A white dwarf is the core of a dying star. These are dim objects that
        are roughly the size of Earth but with the density of a sun-like star. Stars that are
        not massive enough to end in a neutron star or black hole will evolve into a white
        dwarf. This is the ultimate fate of over 95% of the stars in our Galaxy. As the
        star is dying, the outer layers will expand out and the gas will glow and become a
        planetary nebula, while the core of the star transforms into a white dwarf. Census:
        192,613 white dwarfs.""",
        "meta_name": "White Dwarfs",
        "author": "Zack Reeves, Brian Abbott, Ally Baldelli (AMNH)",
    },
    'open_clusters': {
        "renderable": "RenderablePolygonCloud",
        "filename": "oc",
        "Enabled": "false",
        "asset_dir": "open_cluster",
        "data_file": "oc.csv",
        "texture": "point4.png",
        "cmap": None,  # No colormap specified in the asset file
        "Unit": "pc",
        "identifier": "OpenStarClusters_test",
        "fixed_color": "0.13, 0.99, 0.50",
        "Opacity": "0.9",
        "colormap_enabled": "false",
        "parameter_options": [],  # No parameter options specified in the asset file
        "ScaleExponent": "17.8",
        "MaxSize": "23.0",
        "csv_labels": True,
        "LabelColor": "0.0, 0.36, 0.14",
        "LabelSize": "15.5",
        "LabelMinMaxSize": "4, 30",
        "gui_name": "Open Star Clusters -test",
        "gui_path": "/Milky Way/Star Clusters",
        "description": """An open star cluster is a loose assemblage of stars numbering from
        hundreds to thousands that are bound by their mutual gravitation. Because these are
        young stars, we expect to see them in the star-forming regions of our Galaxy, namely
        in the spiral arms. For this reason, open clusters exist, for the most part, in the
        plane of the Galaxy and indicate relatively recent star formation. Census: 1,867 star
        clusters.""",
        "meta_name": "Open Star Clusters",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)",
    },
    'exoplanets': {
        "renderable": "RenderablePointCloud",
        "filename": "expl",
        "asset_dir": "exoplanets",
        "Enabled": "false",
        "data_file": "expl.csv",
        "texture": "target-blue.png",
        "Unit": "pc",
        "cmap": None,  # No colormap specified in the asset file
        "identifier": "Exoplanets_test",
        "fixed_color": None,  # No fixed color specified in the asset file
        "Opacity": "1.0",
        "colormap_enabled": "false",
        "parameter_options": [],  # No parameter options specified in the asset file
        "ScaleExponent": "16.9",
        "MaxSize": "2.8",
        "csv_labels": True,
        "LabelColor": "0.3, 0.3, 0.8",
        "LabelSize": "13.75",
        "LabelMinMaxSize": "10, 100",
        "gui_name": "Exoplanets-test",
        "gui_path": "/Milky Way/Exoplanets",
        "description": """Extrasolar planets, or exoplanets, are a relatively new phenomenon in
        astronomy - no observational evidence was available until 1995. To the eye,
        exoplanets are lost in the glare of their host star. Unconventional techniques are
        required to infer or observe them. Here, exoplanet systems are represented by a blue
        ring centered on each host star. The ring is not intended to signify an orbit, but
        serve only as a marker. The labels list the host star name, and if there is more
        than one planet, will list the number of planets in parentheses. Census: 5,589
        planets in 4,139 systems.""",
        "meta_name": "Exoplanets",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)",
    },
    'exoplanet_candidates': {
        "renderable": "RenderablePointCloud",
        "filename": "expl_candidates",
        "asset_dir": "exoplanets",
        "data_file": "expl_candidates.csv",
        "Enabled": "false",
        "texture": "halo.png",
        "cmap": "expl_candidates.cmap",
        "identifier": "PlanetaryCandidates_test",
        "Unit": "pc",
        "fixed_color": "1.0, 1.0, 0.0",
        "Opacity": "0.99",
        "colormap_enabled": "true",
        "parameter_options": [{"key": "survey_num", "range" : "1.0, 3.0"}],
        "ScaleExponent": "17.8",
        "MaxSize": "1.0",
        "csv_labels": False,
        "LabelColor": None,
        "LabelSize": None,
        "LabelMinMaxSize": None,
        "gui_name": "Exoplanetary Candidates -test",
        "gui_path": "/Milky Way/Exoplanets",
        "description": """The exoplanet candidate stars are likely hosts for exoplanets. These
        are stars plucked from NASA's Kepler and TESS space telescopes. Further observations
        are needed to confirm a planet's existence. Rather than represent them
        photo-realistically, with accurate colors, we choose to visualize them as generic,
        colored stars. The nature of these stars is not important, it is the sheer numbers
        of potential exoplanets that allows us to wonder just how many we will find in the
        entire Galaxy. Colors: Yellow denote Kepler candidates, Orange stars are from the K2
        mission, and green stars are from TESS. Census: 7,225 candidate stars.""",
        "meta_name": "Exoplanetary Candidates",
        "author": "Brian Abbott, Zack Reeves, Emily Rice, Jason No, and Ally Baldelli (AMNH)",
    },
    'alternate_star_labels': {
        "renderable": "StarLabels", # technically its renderable point cloud, but this is a special case
        "filename": "alt_star_labels",
        "asset_dir": "stars",
        "data_file": "stars_labels.csv",  # No CSV file specified in the asset file
        "identifier": "StarLabelsAlternate_test",
        "Enabled": "false",
        "colormap_enabled": "false",
        "csv_labels": True,
        "label_column_name": "alt_label",
        "LabelColor": "0.4, 0.4, 0.4",
        "LabelSize": "14.4",
        "LabelMinMaxSize": "15, 20",
        "Unit": "pc",
        "Opacity": "0.65",
        "gui_name": "Stars Labels - Alternate -test",
        "gui_path": "/Milky Way/Stars",
        "description": """Alternate star labels for the stars. Priority goes to Bayer IDs
        (Greek designations, like Alpha Orionis), then to Flamsteed numbers (like 1
        Orionis).""",
        "meta_name": "Alternative Labels for the Stars",
        "author": "Zack Reeves, Brian Abbott, Ally Baldelli (AMNH)",
    },
    'star_labels': {
        "renderable": "StarLabels", # technically its renderable point cloud, but this is a special case
        "filename": "star_labels",
        "Enabled": "false",
        "asset_dir": "stars",
        "data_file": "stars_labels.csv",  # No CSV file specified in the asset file
        "identifier": "StarLabels_test",
        "colormap_enabled": "false",
        "csv_labels": True,
        "label_column_name": "label",
        "LabelColor": "0.4, 0.4, 0.4",
        "LabelSize": "14.4",
        "LabelMinMaxSize": "6, 50",
        "Unit": "pc",
        "Opacity": "0.65",
        "gui_name": "Stars Labels -test",
        "gui_path": "/Milky Way/Stars",
        "description": """Common name labels for nearby stars in the Milky Way. See 'Stars'
        for more information.""",
        "meta_name": "Star Labels",
        "author": "Zack Reeves, Brian Abbott, Ally Baldelli (AMNH)",
    },
}

def data_info(data_name):
    """
    Returns the data information dictionary for the given data name.
    
    Parameters:
    data_name (str): The name of the data set.
    
    Returns:
    dict: The data information dictionary for the given data name.
    
    Raises:
    KeyError: If the data name is not found in the master dictionary.
    """
    try:
        return master_dictionary[data_name]
    except KeyError:
        available_keys = ', '.join(master_dictionary.keys())
        raise KeyError(f"Data name '{data_name}' not found in master dictionary. Available keys are: {available_keys}")
    
def data_info_names():
    """
    Returns a list of all data names available in the master dictionary.
    """
    return list(master_dictionary.keys())