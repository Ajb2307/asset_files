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
    'open_clusters': {
        "renderable": "RenderablePolygonCloud",
        "filename": "oc",
        "Enabled": "false",
        "asset_dir": "open_cluster",
        "data_file": "oc.csv",
        "PolygonSides": "12",
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
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)"
    },
    'pulsars': {
        "renderable": "RenderablePolygonCloud",
        "filename": "pulsars",
        "Enabled": "false",
        "asset_dir": "pulsars",
        "data_file": "pulsars.csv",
        "Unit": "Kpc",
        "PolygonSides": "4",
        "Opacity": "1.0",
        "texture": None,  # No texture specified in the asset file
        "cmap": None,  # No colormap specified in the asset file
        "identifier": "Pulsars_test",
        "fixed_color": "0.7, 0.0, 0.0",
        "colormap_enabled": "false",
        "parameter_options": [],  # No parameter options specified in the asset file
        "ScaleExponent": "18.1",
        "MaxSize": "19.0",
        "csv_labels": True,
        "LabelColor": "0.75, 0.21, 0.21",
        "LabelSize": "15.27",
        "LabelMinMaxSize": "4, 20",
        "gui_name": "Pulsars-test",
        "gui_path": "/Milky Way/Stellar Remnants",
        "description": """A pulsar is a spinning neutron star, an ultra-dense stellar remnant
        resulting from a supernova-driven collapse of the stellar core. Upon death, stars
        leave behind one of three possible remnants: a white dwarf, a neutron star, or a
        black hole. Stars that are more massive than the sun will often become neutron
        stars in a violent explosion called a supernova. Pulsars are not pulsing but are
        spinning neutron stars whose beams of radiation point toward Earth just as a
        lighthouse sweeps the horizon. Their strong magnetic fields funnel beams of light
        from its poles. When these beams point to Earth, we see a strong radio signal.
        Census: 3,221 pulsars.""",
        "meta_name": "Pulsars",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)",
    },
    'supernova_remnants': {
        "renderable": "RenderablePolygonCloud",
        "filename": "snr",
        "asset_dir": "supernova_remnants",
        "Enabled": "false",
        "data_file": "snr.csv",
        "Unit": "pc",
        "PolygonSides": "7",
        "Opacity": "0.32",
        "texture": None,  # No texture specified in the asset file
        "cmap": None,  # No colormap specified in the asset file
        "identifier": "SupernovaRemnants_test",
        "fixed_color": "1.0, 0.5, 0.0",
        "colormap_enabled": "false",
        "parameter_options": [],  # No parameter options specified in the asset file
        "ScaleExponent": "18.4",
        "MaxSize": "19.0",
        "csv_labels": True,
        "LabelColor": "0.51, 0.40, 0.04",
        "LabelSize": "16.0",
        "LabelMinMaxSize": "4, 100",
        "gui_name": "Supernova Remnants-test",
        "gui_path": "/Milky Way/Nebulae",
        "description": """A supernova remnant is the nebulous gas left over from a supernova
        explosion. This gas expands at great speeds and rams into the surrounding
        interstellar gas. This excites the surrounding gas and causes it to glow, producing
        the nebulous cloud we observe from Earth. A supernova remnant contains a neutron
        star or pulsar at its center, the core of the dying star. The cloud that enshrouds
        the core does not last long, though. After about 50,000 years, the gas mixes into
        the interstellar medium and no longer glows. Astronomically, this is a very short
        time, so the supernova remnants we see must be left from explosions that have
        occurred recently, cosmically speaking. Census: 112 supernova remnants.""",
        "meta_name": "Supernova Remnants",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)",
    },
    'h2_regions': {
        "renderable": "RenderablePolygonCloud",
        "filename": "h2",
        "asset_dir": "h2_regions",
        "Enabled": "false",
        "data_file": "h2.csv",
        "Unit": "pc",
        "PolygonSides": "6",
        "Opacity": "0.7",
        "texture": None,  # No texture specified in the asset file
        "cmap": None,  # No colormap specified in the asset file
        "identifier": "HIIRegions_test",
        "fixed_color": "0.0, 0.5, 1.0",
        "colormap_enabled": "false",
        "parameter_options": [],  # No parameter options specified in the asset file
        "ScaleExponent": "18.5",
        "MaxSize": "8.0",
        "csv_labels": True,
        "LabelColor": "0.5, 0.5, 0.5",
        "LabelSize": "16.24",
        "LabelMinMaxSize": "4, 20",
        "gui_name": "HII Regions -test",
        "gui_path": "/Milky Way/Nebulae",
        "description": """HII (pronounced "H-two") regions are stellar nurseries for newborn
        stars. Stars are born from condensing clouds of hydrogen gas. As these clouds
        condense, the densities become high enough to form stars. An HII region is the
        surrounding clouds of hydrogen that glow from the stars born within them. The
        result is a bright, glowing nebula which is seen to great distances. One local
        celebrity among HII regions is the Orion Nebula (M42). These star-forming regions
        lie in the plane of the Galaxy because that is where star formation occurs in
        spiral galaxies such as our Milky Way. Because of this, they are great tracers of
        the spiral arms of the Galaxy. Census: 1,108 star-forming regions.""",
        "meta_name": "HII Regions",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)",
    },
    'ob_associations': {
        "renderable": "RenderablePolygonCloud",
        "filename": "ob",
        "Enabled": "false",
        "asset_dir": "ob_association",
        "data_file": "ob.csv",
        "PolygonSides": "7",
        "cmap": "ob.cmap",
        "Unit": "pc",
        "identifier": "OBAssociations_test",
        "fixed_color": None,  # No fixed color specified in the asset file
        "Opacity": "0.7",
        "colormap_enabled": "true",
        "parameter_options": [{"key": "armID", "range": "1.0, 3.0"}],
        "ScaleExponent": "16.9",
        "MaxSize": "17",
        "SizeMapping_ParameterOptions": "diameter",
        "csv_labels": True,
        "LabelColor": "0.4, 0.5, 1.0",
        "LabelSize": "16.24",
        "LabelMinMaxSize": "4, 25",
        "gui_name": "OB Associations-test",
        "gui_path": "/Milky Way/Star Clusters",
        "description": """Stellar associations are loose agglomerations of stars that form from
        the same gas cloud. OB associations typically have on the order of dozens of O and
        B stars in them (hotter, massive, younger stars) in addition to cooler stars. Over
        time the stars disperse and the association is less concentrated. These associations
        track relatively recent star formation. Colors: Blue trace the Sagittarius Arm,
        Purple are in the local Orion Spur, and Orange are in the Perseus Arm. Census: 61 OB
        associations.""",
        "meta_name": "OB Associations",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)",
    },
    'globular_clusters': {
        "renderable": "RenderablePolygonCloud",
        "filename": "gc",
        "Enabled": "false",
        "asset_dir": "globular_clusters",
        "data_file": "gc.csv",
        "PolygonSides": "5",
        "cmap": None,  # No colormap specified in the asset file
        "Unit": "pc",
        "identifier": "GlobularClusters_test",
        "fixed_color": "0.8, 0.8, 0.0",
        "Opacity": "0.65",
        "colormap_enabled": "false",
        "parameter_options": [],  # No parameter options specified in the asset file
        "ScaleExponent": "18.6",
        "MaxSize": "13.0",
        "csv_labels": True,
        "LabelColor": "0.36, 0.36, 0.0",
        "LabelSize": "16.7",
        "LabelMinMaxSize": "4, 20",
        "gui_name": "Globular Clusters-test",
        "gui_path": "/Milky Way/Star Clusters",
        "description": """Globular star clusters are gravitationally bound groups of 100,000
        to 1 million stars. They are compact, spherical "balls" of stars with very high
        stellar densities. These clusters are typically 30 to 100 light years in diameter.
        Census: 161 globular clusters.""",
        "meta_name": "Globular Clusters",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)",
    },
    'manga': {
        "renderable": "RenderablePolygonCloud",
        "filename": "manga",
        "Enabled": "false",
        "asset_dir": "manga",
        "data_file": "manga.csv",
        "PolygonSides": "5",
        "cmap": None,  # No colormap specified in the asset file
        "Unit": "Mpc",
        "identifier": "MaNGA_test",
        "fixed_color": "0.8, 0.8, 0.0",
        "Opacity": "0.8",
        "colormap_enabled": "false",
        "parameter_options": [],  # No parameter options specified in the asset file
        "ScaleExponent": "22.6",
        "MaxSize": "0.15",
        "FadeInDistances": "220.0, 650.0",
        "csv_labels": False,  # No labels specified in the asset file
        "LabelColor": None,
        "LabelSize": None,
        "LabelMinMaxSize": None,
        "gui_name": "MaNGA Nearby Galaxy Catalog -test",
        "gui_path": "/Universe/Deep Sky Surveys",
        "description": """MaNGA Nearby Galaxy Catalog.""",
        "meta_name": "SDSS4 MaNGA",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)",
    },
    'stars' : {
        "renderable": "RenderableStars",
        "filename": "stars",
        "asset_dir": "stars",
        "data_file": "stars.speck",
        "core_texture": "glare.png",
        "glare_texture": "halo.png",
        "cmap": "colorbv.cmap",
        "other_cmap": "viridis.cmap",
        "identifier": "Stars_test",
        "Bv_column": "colorb_v",
        "Luminance_column": "lum",
        "AbsoluteMagnitude_column": "absmag",
        "ApparentMagnitude_column": "appmag",
        "Vx_column": "vx",
        "Vy_column": "vy",
        "Vz_column": "vz",
        "Speed_column": "speed",
        "gui_name": "Stars -test",
        "gui_path": "/Milky Way/Stars",
        "description": """These are the nearby stars that surround the Sun and are close enough
        to get accurate distances. These include all the stars we see with the unaided eye
        and many stars dimmer than that. Over the entire night sky, all year round, and in
        the northern and southern hemispheres, we can see roughly 9,000 stars total with
        the unaided eye. Stars are the light factories of the universe, and come in a
        variety of sizes, colors, and brightnesses. The base catalog is Hipparcos, with Gaia
        DR3 data applied for distance and velocity when available. Census: 112,746 stars.""",
        "meta_name": "Stars",
        "author":  "Brian Abbott, Zack Reeves, Andrew Ayala, Jackie Faherty, Ally Baldelli (AMNH)"
        },
    'quasars': {
        "renderable": "RenderablePointCloud",
        "filename": "quasars",
        "Enabled": "true",
        "asset_dir": "quasars",
        "data_file": "qso.csv",
        "texture": "point3A.png",
        "cmap": "viridis.cmap",
        "Unit": "Mpc",
        "identifier": "Quasars_test",
        "fixed_color": "0.85, 0.35, 0.18",
        "Opacity": "0.95",
        "colormap_enabled": "false",
        "parameter_options": [{"key": "lookback_time", "range": "1.4, 13.0"}],
        "ScaleExponent": "23.5",
        "MaxSize": "0.3",
        "FadeInDistances": "1000.0, 10000.0",
        "csv_labels": False,  # No labels specified in the asset file
        "LabelColor": None,
        "LabelSize": None,
        "LabelMinMaxSize": None,
        "gui_name": "Quasars-test",
        "gui_path": "/Universe/Deep Sky Surveys",
        "description": """Quasars are the most distant objects we see. They are extremely
        active galaxies that contain supermassive black holes which gobble up material at a
        furious rate. As the material falls into the black hole, it forms a disk and emits
        high-energy light that we see to great distances. Census: 755,850 quasars.""",
        "meta_name": "Quasars",
        "author": "Brian Abbott, Sohum Udani, Ally Baldelli (AMNH)",
    },
    'black_holes': {
        "renderable": "RenderablePointCloud",
        "filename": "bh",
        "Enabled": "false",
        "asset_dir": "black_holes",
        "data_file": "bh.csv",
        "texture": "point4.png",
        "cmap": None,  # No colormap specified in the asset file
        "Unit": "pc",
        "identifier": "BlackHole_test",
        "fixed_color": "0.3, 0.15, 0.9",
        "Opacity": None,  # No opacity specified in the asset file
        "colormap_enabled": "false",
        "parameter_options": [],  # No parameter options specified in the asset file
        "ScaleExponent": "18.6",
        "MaxSize": "13.0",
        "csv_labels": False,  # No labels specified in the asset file
        "LabelColor": None,
        "LabelSize": None,
        "LabelMinMaxSize": None,
        "gui_name": "Black Hole- test",
        "gui_path": "/Milky Way/Stellar Remnants",
        "description": """BlackCAT: A catalogue of stellar-mass black holes in X-ray transients""",
        "meta_name": "Black Holes",
        "author": "Zack Reeves, Brian Abbott,  Ally Baldelli (AMNH)",
    },
    'planetary_nebulae': {
        "renderable": "RenderablePolygonCloud",
        "filename": "pn",
        "Enabled": "false",
        "asset_dir": "planetary_nebulae",
        "data_file": "pn.csv",
        "PolygonSides": "3",
        "cmap": None,  # No colormap specified in the asset file
        "Unit": "pc",
        "identifier": "PlanetaryNebulae_test",
        "fixed_color": "0.4, 0.4, 0.9",
        "Opacity": "0.99",
        "colormap_enabled": "false",
        "parameter_options": [],  # No parameter options specified in the asset file
        "ScaleExponent": "18.2",
        "MaxSize": "19.0",
        "csv_labels": True,
        "LabelColor": "0.35, 0.35, 0.60",
        "LabelSize": "16.24",
        "LabelMinMaxSize": "4, 25",
        "gui_name": "Planetary Nebulae -test",
        "gui_path": "/Milky Way/Nebulae",
        "description": """A planetary nebula is an expanding shell of gas ejected from an
        average-sized star late in its life cycle. Appearing like greenish disks to a
        telescopic observer, planetary nebulae received their name from their resemblance to
        the gaseous planets of our solar system. In no way are they related to planets,
        rather, they are products of dying stars. As the gas from the star expands, it
        sweeps up the cooler gas like a snowplow. The gas glows because of the ultraviolet
        light from the stellar remnant at the center. Because the planetary nebula phase of
        a star's evolution is relatively short, we observe only those that have occurred
        recently in the younger stellar population. Therefore, we expect to see planetary
        nebulae in the disk of the Galaxy. Census: 1,657 planetary nebulae.""",
        "meta_name": "Planetary Nebulae",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)"
    },
    'star_uncertainty': {
        "renderable": "RenderableConstellationLines",
        "filename": "stellar_uncertainty",
        "identifier": "StarUncertainty_test",
        "Enabled": "false",
        "asset_dir": "stellar_uncertainty",
        "data_file": "star_uncertainty.speck",
        "label_file": "star_uncertainty.label",
        "dat_file": "star_uncertainty.dat", 
        "Opacity": "0.8",
        "LineWidth": "5.0",
        "LabelColor": "0.6, 0.6, 1.0",
        "LabelSize": "14.1",
        "LabelMinMaxSize": "8, 170",
        "Unit": "pc",
        "DimInAtmosphere": 'true',
        "Colors":  "{1.0, 1.0, 0.0}, {0.0, 0.8, 1.0}, {0.957, 0.51, 0.10}", 
        "gui_name": "Star Distance Uncertainty-test",
        "gui_path": "/Milky Way/Stars",
        "description": """The uncertainty of a star's position is derived from the uncertainty
        in its parallax measurement. This results in a range in distance where the star
        could exist. Here we draw lines on top of select stars which give us a visual cue
        of the range in possible distances for that star. Colors: Aqua lines are stars with
        Gaia geometric parallax measurements (the most accurate), orange lines indicate
        stars with Hipparcos geometric parallaxes, and yellow lines are stars with Gaia
        photogeometric parallaxes (the least accurate). The label includes the star name
        and the length of the uncertainty in light years. Census: 3,440 stars with
        uncertainty.""",
        "meta_name": "Star Distance Uncertainty",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)",
    },
    'constellations': {
        "renderable": "RenderableConstellationLines",
        "identifier": "Constellations_test",
        "zodiacs": True,
        "constellation_actions": True,
        "filename": "constellations",
        "Enabled": "false",
        "asset_dir": "constellations",
        "data_file": "constellation_lines.speck",
        "label_file": "constellation_lines.label",
        "dat_file": "constellations.dat",
        "Opacity": "0.3",
        "LineWidth": None,  # Not specified in the asset file
        "csv_labels": False,  # No CSV labels specified in the asset file
        "LabelColor": "0.8, 0.8, 0.8",
        "LabelSize": "14.5",
        "LabelMinMaxSize": "8, 170",
        "Unit": "pc",
        "DimInAtmosphere": 'true',
        "Colors": '{0.6, 0.4, 0.4}, {0.8, 0.0, 0.0}, {0.0, 0.3, 0.8}' ,
        "gui_name": "Constellation Lines -test",
        "gui_path": "/Milky Way/Constellations",
        "description": """Lines connecting the stars that make up the constellation figures.
        We represent the constellations by connecting the main stars that make up the
        constellation "stick figures," as seen from Earth. Colors: most constellations
        are pink, while the zodiacal constellations are red. We also color Orion and Ursa
        Major blue as two recognizable constellations in the night sky. Census: 88
        constellations.""",
        "meta_name": "Constellations",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)",
    },
    'star_orbits': {
        "renderable": "RenderableDUMeshes",
        "filename": "star_orbits",
        "Enabled": "false",
        "asset_dir": "star_orbits",
        "data_folder": "",
        "Unit": "pc",
        "Opacity": "1.0",
        "gui_path": "/Milky Way/Star Orbits",
        "objects": {"SunOrbit": {
                        "identifier": "SunOrbit_test",
                        "speck_file": "starorbits-Sun.speck",
                        "MeshColor": "1.0, 0.65, 0.0",
                        "gui_name": "Sun Orbit -test",
                        "description": """Projected orbit of the Sun around the Milky Way over the next 1 billion years.""" 
                        },
                    "BarnardsOrbit":  {
                        "identifier": "BarnardsOrbit_test",
                        "speck_file": "starorbits-BarnardsStar.speck",
                        "MeshColor": "0.39, 0.58, 0.93",
                        "gui_name": "Barnards Orbit -test",
                        "description": """Projected orbit of the Barnard's Star around the Milky Way over the next 1 billion years.""" 
                        },
                    "KapteynsOrbit":  {
                        "identifier": "KapteynsOrbit_test",
                        "speck_file": "starorbits-KapteynsStar.speck",
                        "MeshColor": "0.6, 0.6, 0.6",
                        "gui_name": "Kapteyns Orbit -test",
                        "description": """Projected orbit of the Kapteyn's Star around the Milky Way over the next 1 billion years.""" 
                        },
                    "Lacaille9352Orbit":  {
                        "identifier": "Lacaille9352Orbit_test",
                        "speck_file": "starorbits-Lacaille9352.speck",
                        "MeshColor": "0.58, 0.0, 0.83",
                        "gui_name": "Lacaille 9352 Orbit -test",
                        "description": """Projected orbit of the Lacaille9352 around the Milky Way over the next 1 billion years.""" }, 
                    "LSR1826Orbit":  {
                        "identifier": "LSR1826Orbit_test",
                        "speck_file": "starorbits-LSR1826+3014.speck",
                        "MeshColor": "0.0, 0.39, 0.0",
                        "gui_name": "LSR1826+3014 Orbit -test",
                        "description": """Projected orbit of the LSR1826+3014 around the Milky Way over the next 1 billion years.""" },
                    "LSRJ0822Orbit":  {
                        "identifier": "LSRJ0822Orbit_test",
                        "speck_file": "starorbits-LSRJ0822+1700.speck",
                        "MeshColor": "0.5, 1.0, 0.0",
                        "gui_name": "LSRJ0822+1700 Orbit -test",
                        "description": """Projected orbit of the LSRJ0822+1700 around the Milky Way over the next 1 billion years.""" },
                    "PM_J13420Orbit":  {
                        "identifier": "PM_J13420Orbit_test",
                        "speck_file": "starorbits-PM_J13420-3415.speck",
                        "MeshColor": "0.70, 0.13, 0.13",
                        "gui_name": "PM_J13420-3415 Orbit -test",
                        "description": """Projected orbit of the PM_J13420-3415 around the Milky Way over the next 1 billion years.""" },
        },
        "meta_name": "Star Orbits",
        "meta_description": """Projected star orbits for selected stars over the next 1 billion years. Census: 7 star orbits.""",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)"
    }
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