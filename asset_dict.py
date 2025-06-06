master_dictionary = {
    '2dF': {
        "renderable": "RenderablePointCloud",
        "Enabled": "false",
        "filename": "2df",
        "asset_dir": "twodF",
        "data": {
            "File": "2df.csv",
            "Name": "2dF Speck Files",
            "Identifier": "digitaluniverse_2dF_speck",
            "Version": 3
            },
        "local_modules": True,
        "Unit": "Mpc",
        "Texture": {
            "File": "point3A.png",
            "Name": "Point Textures",
            "Identifier": "digitaluniverse_point_textures",
            "Version": 1
            },
        "Identifier": "2dF_test",
        "FixedColor": "1.0, 1.0, 1.0", # not used
        "Opacity": "1.0",
        "ColorMapping": {
            "Name": "2dF Speck Files",
            "Identifier": "digitaluniverse_2dF_speck",
            "Version": 3,
            "File": "2dF.cmap",
            "Enabled": "true",
            "ParameterOptions": [{"Key": "num_nearby_galaxies", "Range": "1.0, 25.0"},
                                {"Key": "redshift", "Range": "0.0, 0.075"}]
            },
        "ScaleExponent": "22.6",
        "MaxSize": "0.2",
        "GUI":{ 
            "Name": "2dF Galaxies -test",
            "Path": "/Universe/Deep Sky Surveys",
            "Description": """The Two-degree Field (2dF) Survey was a project designed to map 
            portions of the extragalactic universe. The 2dF survey has three main components: 
            the North Galactic Pole strip, the South Galactic Pole strip, and the random fields
            that surround the South Galactic Pole strip. Colors: Orange galaxies show dense 
            regions of galaxies, aqua galaxies are areas of intermediate density, and green
            galaxies are areas of lower density. Census: 229,293 galaxies."""
            },
        "meta_name": "2dF Galaxies",
        "author": "Brian Abbott (AMNH), Eric Gawiser (Rutgers U), Ally Baldelli (AMNH)",
    },
    'brown_dwarfs': {
        "renderable": "RenderablePointCloud",
        "local_modules": True,
        "Enabled": "false",
        "filename": "bd",
        "asset_dir": "brown_dwarf",
        "data": {
            "File": "bd.csv",
            "Name": "Brown Dwarf Speck Files",
            "Identifier": "digitaluniverse_brown_dwarfs_speck",
            "Version": 1
            },
        "Unit": "pc",
        "Texture": {
            "File": "point3.png",
            "Name": "Point Textures",
            "Identifier": "digitaluniverse_point_textures",
            "Version": 1
            },
        "Identifier": "BrownDwarfs_test",
        "FixedColor": "0.4, 0.0, 0.1",
        "Opacity": "1.0",
        "ColorMapping": {
            "Name": "Brown Dwarf Speck Files",
            "Identifier": "digitaluniverse_brown_dwarfs_speck",
            "Version": 1,
            "File": "bd.cmap",
            "Enabled": "true",
            "ParameterOptions": [{"Key": "typeindex", "Range": "1.0, 4.0"}]
        },
        "ScaleExponent": "15.8",
        "MaxSize": "0.7",
        "Labels":{ 
            "csv": True,
            "Color": "0.6, 0.3, 0.4",
            "Size": "13.75",
            "MinMaxSize": "10, 100"
            },
        "GUI": {
            "Name": "Brown Dwarfs -test",
            "Path": "/Milky Way/Substellar Objects",
            "Description": r"""For decades it was believed that M stars were the coolest stars in
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
            2,196 objects."""
        },
        "meta_name": "Brown Dwarfs",
        "author": "Brian Abbott, Zack Reeves, Jackie Faherty, Ally Baldelli (AMNH)"
    },
    '6dF': {
        "renderable": "RenderablePointCloud",
        "Enabled": "false",
        "filename": "6df",
        "local_modules": True,
        "asset_dir": "sixdF",
        "data": {
            "File": "6df.csv",
            "Name": "6dF Speck Files",
            "Identifier": "digitaluniverse_6dF_speck",
            "Version": 3
            },
        "Texture": {
            "File": "point3A.png",
            "Name": "Point Textures",
            "Identifier": "digitaluniverse_point_textures",
            "Version": 1
            },
        "Unit": "Mpc",
        "Identifier": "6dF_test",
        "FixedColor": "1.0, 1.0, 0.0",
        "Opacity": "1.0",
        "ColorMapping": {
            "File": "6dF.cmap",
            "Enabled": "true",
            "ParameterOptions": [
                {"Key": "num_nearby_galaxies", "Range": "1.0, 10.0"},
                {"Key": "redshift", "Range": "0.0, 0.075"}],
            "Name": "6dF Speck Files",
            "Identifier": "digitaluniverse_6dF_speck",
            "Version": 3
            },
        "ScaleExponent": "22.5",
        "MaxSize": "0.2",
        "GUI": {
            "Name": "6dF Galaxies -test",
            "Path": "/Universe/Deep Sky Surveys",
            "Description": """The Six-degree Field (6dF) Galaxy Survey mapped nearly half the sky
            from the Anglo-Australian Observatory. Because it's a southern hemisphere survey,
            there is no coverage in these data for the northern hemisphere's sky. As with all
            galaxy surveys, the orange galaxies are in relatively dense areas, the green
            galaxies are in relatively sparse areas, and the aqua galaxies are between. Census:
            109,569 galaxies."""
        },
        "meta_name": "6dF Galaxies",
        "author": "Brian Abbott, Ally Baldelli (AMNH)",
    },
    'SDSS': {
        "renderable": "RenderablePointCloud",
        "filename": "sdss",
        "Enabled": "true",
        "asset_dir": "ssds",
        "local_modules": True,
        "data": {
            "File": "sdss.csv",
            "Name": "Sloan Digital Sky Survey Speck Files",
            "Identifier": "digitaluniverse_sloandss_speck",
            "Version": 4
            },
        "Texture": {
            "File": "point3A.png",
            "Name": "Point Textures",
            "Identifier": "digitaluniverse_point_textures",
            "Version": 1
            },
        "Identifier": "SloanDigitalSkySurvey_test",
        "Unit": "Mpc",
        "FixedColor": "0.8, 0.8, 1.0",
        "Opacity": "0.8",
        "ColorMapping": {
            "File": "SDSSgals.cmap",
            "Enabled": "true",
            "ParameterOptions": [{"Key": "num_nearby_galaxies", "Range": "1.0, 25.0"}],
            "Name": "Sloan Digital Sky Survey Speck Files",
            "Identifier": "digitaluniverse_sloandss_speck",
            "Version": 4
            },
        "ScaleExponent": "22.6",
        "MaxSize": "0.15",
        "FadeInDistances": "220.0, 650.0",
        "GUI": {
            "Name": "Sloan Digital Sky Survey -test",
            "Path": "/Universe/Deep Sky Surveys",
            "Description": r"""The Sloan Digital Sky Survey (SDSS) is an ambitious project to image
            about 35% of the sky, deep into the universe. The SDSS galaxies form triangular
            wedges, revealing those parts of the sky observed by the telescope. If the entire
            sky were covered, you would see a spherical distribution of galaxies surrounding
            the Milky Way. With only 35% of the entire sky observed, we see only a few select
            slices or larger wedgelike portions from that sphere. The weblike cosmic structure
            is echoed in these data, with orange clusters standing out among the less dense
            aqua-colored galaxies and the less dense regions of green-colored galaxies.
            Census: 2,862,767 galaxies."""
        },
        "meta_name": "Sloan Digital Sky Survey Galaxies",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH), Eric Gawiser (Rutgers)"
        },
    'white_dwarfs': {
        "renderable": "RenderablePointCloud",
        "filename": "wd",
        "asset_dir": "white_dwarfs",
        "local_modules": True,
        "Enabled": "false",
        "data": {
            "File": "wd.csv",
            "Name": "White Dwarf Speck Files",
            "Identifier": "digitaluniverse_white_dwarfs_speck",
            "Version": 1
            },
        "Texture": {
            "File": "point3.png",
            "Name": "Point Textures",
            "Identifier": "digitaluniverse_point_textures",
            "Version": 1
            },
        "Identifier": "WhiteDwarfs_test",
        "Unit": "pc",
        "FixedColor": "1.0, 1.0, 1.0",
        "Opacity": "1.0",
        "ScaleExponent": "15.5",
        "MaxSize": "0.7",
        "GUI": {
            "Name": "White Dwarfs- test",
            "Path": "/Milky Way/Stellar Remnants",
            "Description": r"""A white dwarf is the core of a dying star. These are dim objects that
            are roughly the size of Earth but with the density of a sun-like star. Stars that are
            not massive enough to end in a neutron star or black hole will evolve into a white
            dwarf. This is the ultimate fate of over 95% of the stars in our Galaxy. As the
            star is dying, the outer layers will expand out and the gas will glow and become a
            planetary nebula, while the core of the star transforms into a white dwarf. Census:
            192,613 white dwarfs."""
        },
        "meta_name": "White Dwarfs",
        "author": "Zack Reeves, Brian Abbott, Ally Baldelli (AMNH)"
    },
    'exoplanets': {
        "renderable": "RenderablePointCloud",
        "filename": "expl",
        "asset_dir": "exoplanets",
        "local_modules": True,
        "Enabled": "false",
        "data": {
            "File": "expl.csv",
            "Name": "Exoplanets Speck Files",
            "Identifier": "digitaluniverse_exoplanets_speck",
            "Version": 4
            },
        "Texture": {
            "File": "target-blue.png",
            "Name": "Exoplanets Textures",
            "Identifier": "digitaluniverse_exoplanets_textures",
            "Version": 1
            },
        "Unit": "pc",
        "Identifier": "Exoplanets_test",
        "FixedColor": None,  # No fixed color specified in the asset file
        "Opacity": "1.0",
        "ScaleExponent": "16.9",
        "MaxSize": "2.8",
        "Labels": {
            "csv": True,
            "Color": "0.3, 0.3, 0.8",
            "Size": "13.75",
            "MinMaxSize": "10, 100"
            },
        "GUI": {
            "Name": "Exoplanets-test",
            "Path": "/Milky Way/Exoplanets",
            "Description": """Extrasolar planets, or exoplanets, are a relatively new phenomenon in
            astronomy - no observational evidence was available until 1995. To the eye,
            exoplanets are lost in the glare of their host star. Unconventional techniques are
            required to infer or observe them. Here, exoplanet systems are represented by a blue
            ring centered on each host star. The ring is not intended to signify an orbit, but
            serve only as a marker. The labels list the host star name, and if there is more
            than one planet, will list the number of planets in parentheses. Census: 5,589
            planets in 4,139 systems."""
            },
        "meta_name": "Exoplanets",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)",
    },
    'exoplanet_candidates': {
        "renderable": "RenderablePointCloud",
        "filename": "expl_candidates",
        "asset_dir": "exoplanets",
        "data": {
            "File": "expl_candidates.csv",
            "Name": "Exoplanets Candidates Speck Files",
            "Identifier": "digitaluniverse_exoplanets_candidates_speck",
            "Version": 2
            },
        "local_modules": True,
        "Enabled": "false",
        "Texture": {
            "File": "halo.png",
            "Name": "Exoplanets Candidates Textures",
            "Identifier": "digitaluniverse_exoplanets_candidates_textures",
            "Version": 1
            },
        "Identifier": "PlanetaryCandidates_test",
        "Unit": "pc",
        "FixedColor": "1.0, 1.0, 0.0",
        "Opacity": "0.99",
        "ColorMapping": {
            "File": "expl_candidates.cmap",
            "Enabled": "true",
            "ParameterOptions": [{"Key": "survey_num", "Range" : "1.0, 3.0"}],
            "Name": "Exoplanets Candidates Speck Files",
            "Identifier": "digitaluniverse_exoplanets_candidates_speck",
            "Version": 2
            },
        "ScaleExponent": "17.8",
        "MaxSize": "1.0",
        "GUI": {
            "Name": "Exoplanetary Candidates -test",
            "Path": "/Milky Way/Exoplanets",
            "Description": """The exoplanet candidate stars are likely hosts for exoplanets. These
            are stars plucked from NASA's Kepler and TESS space telescopes. Further observations
            are needed to confirm a planet's existence. Rather than represent them
            photo-realistically, with accurate colors, we choose to visualize them as generic,
            colored stars. The nature of these stars is not important, it is the sheer numbers
            of potential exoplanets that allows us to wonder just how many we will find in the
            entire Galaxy. Colors: Yellow denote Kepler candidates, Orange stars are from the K2
            mission, and green stars are from TESS. Census: 7,225 candidate stars."""
            },
        "meta_name": "Exoplanetary Candidates",
        "author": "Brian Abbott, Zack Reeves, Emily Rice, Jason No, and Ally Baldelli (AMNH)",
    },
    'alternate_star_labels': {
        "renderable": "StarLabels", # technically its renderable point cloud, but this is a special case
        "filename": "alt_star_labels",
        "asset_dir": "stars",
        "local_modules": True,
        "data": {
            "File": "stars_labels.csv",
            "Name": "Star Labels Alternate Speck Files",
            "Identifier": "digitaluniverse_alternatestarlabels_speck",
            "Version": 3
            },
        "Identifier": "StarLabelsAlternate_test",
        "Enabled": "false",
        "colormap_enabled": "false",
        "Labels": {
            "csv": True,
            "column": "alt_label",
            "Color": "0.4, 0.4, 0.4",
            "Size": "14.4",
            "MinMaxSize": "15, 20"
            },  
        "Unit": "pc",
        "Opacity": "0.65",
        "GUI": {
            "Name": "Stars Labels - Alternate -test",
            "Path": "/Milky Way/Stars",
            "Description": """Alternate star labels for the stars. Priority goes to Bayer IDs
            (Greek designations, like Alpha Orionis), then to Flamsteed numbers (like 1
            Orionis)."""
            },
        "meta_name": "Alternative Labels for the Stars",
        "author": "Zack Reeves, Brian Abbott, Ally Baldelli (AMNH)",
    },
    'star_labels': {
        "renderable": "StarLabels", # technically its renderable point cloud, but this is a special case
        "filename": "star_labels",
        "Enabled": "false",
        "asset_dir": "stars",
        "local_modules": True,
        "data": {
            "File": "stars_labels.csv",
            "Name": "Star Labels Speck Files",
            "Identifier": "digitaluniverse_starlabels_speck",
            "Version": 3
            },
        "Identifier": "StarLabels_test",
        "colormap_enabled": "false",
        "Labels": {
            "csv": True,
            "column": "label",
            "Color": "0.4, 0.4, 0.4",
            "Size": "14.4",
            "MinMaxSize": "6, 50"
            },
        "Unit": "pc",
        "Opacity": "0.65",
        "GUI": {
            "Name": "Stars Labels -test",
            "Path": "/Milky Way/Stars",
            "Description": """Common name labels for nearby stars in the Milky Way. See 'Stars'
            for more information."""
            },
        "meta_name": "Star Labels",
        "author": "Zack Reeves, Brian Abbott, Ally Baldelli (AMNH)",
    },
    'open_clusters': {
        "renderable": "RenderablePolygonCloud",
        "filename": "oc",
        "Enabled": "false",
        "asset_dir": "open_cluster",
        "local_modules": True,
        "data": {
            "File": "oc.csv",
            "Name": "Open Clusters Speck Files",
            "Identifier": "digitaluniverse_openclusters_speck",
            "Version": 4
            },
        "PolygonSides": "12",
        "Unit": "pc",
        "Identifier": "OpenStarClusters_test",
        "FixedColor": "0.13, 0.99, 0.50",
        "Opacity": "0.9",
        "ScaleExponent": "17.8",
        "MaxSize": "23.0",
        "Labels": {
            "csv": True,
            "Color": "0.0, 0.36, 0.14",
            "Size": "15.5",
            "MinMaxSize": "4, 30"
            },
        "GUI": {
            "Name": "Open Star Clusters -test",
            "Path": "/Milky Way/Star Clusters",
            "Description": """An open star cluster is a loose assemblage of stars numbering from
            hundreds to thousands that are bound by their mutual gravitation. Because these are
            young stars, we expect to see them in the star-forming regions of our Galaxy, namely
            in the spiral arms. For this reason, open clusters exist, for the most part, in the
            plane of the Galaxy and indicate relatively recent star formation. Census: 1,867 star
            clusters."""
            },
        "meta_name": "Open Star Clusters",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)"
    },
    'pulsars': {
        "renderable": "RenderablePolygonCloud",
        "filename": "pulsars",
        "Enabled": "false",
        "asset_dir": "pulsars",
        "local_modules": True,
        "data": {
            "File": "pulsars.csv",
            "Name": "Pulsars Speck Files",
            "Identifier": "digitaluniverse_pulsars_speck",
            "Version": 3
            },
        "Unit": "Kpc",
        "PolygonSides": "4",
        "Opacity": "1.0",
        "Identifier": "Pulsars_test",
        "FixedColor": "0.7, 0.0, 0.0",
        "ScaleExponent": "18.1",
        "MaxSize": "19.0",
        "Labels": {
            "csv": True,
            "Color": "0.75, 0.21, 0.21",
            "Size": "15.27",
            "MinMaxSize": "4, 20"
            },
        "GUI": {
            "Name": "Pulsars-test",
            "Path": "/Milky Way/Stellar Remnants",
            "Description": """A pulsar is a spinning neutron star, an ultra-dense stellar remnant
            resulting from a supernova-driven collapse of the stellar core. Upon death, stars
            leave behind one of three possible remnants: a white dwarf, a neutron star, or a
            black hole. Stars that are more massive than the sun will often become neutron
            stars in a violent explosion called a supernova. Pulsars are not pulsing but are
            spinning neutron stars whose beams of radiation point toward Earth just as a
            lighthouse sweeps the horizon. Their strong magnetic fields funnel beams of light
            from its poles. When these beams point to Earth, we see a strong radio signal.
            Census: 3,221 pulsars."""
            },
        "meta_name": "Pulsars",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)",
    },
    'supernova_remnants': {
        "renderable": "RenderablePolygonCloud",
        "filename": "snr",
        "asset_dir": "supernova_remnants",
        "Enabled": "false",
        "local_modules": True,
        "data": {
            "File": "snr.csv",
            "Name": "Supernova Remnants Speck Files",
            "Identifier": "digitaluniverse_supernovaremnants_speck",
            "Version": 3
            },
        "Unit": "pc",
        "PolygonSides": "7",
        "Opacity": "0.32",
        "Identifier": "SupernovaRemnants_test",
        "FixedColor": "1.0, 0.5, 0.0",
        "ScaleExponent": "18.4",
        "MaxSize": "19.0",
        "Labels": {
            "csv": True,
            "Color": "0.51, 0.40, 0.04",
            "Size": "16.0",
            "MinMaxSize": "4, 100"
            },
        "GUI": {
            "Name": "Supernova Remnants-test",
            "Path": "/Milky Way/Nebulae",
            "Description": """A supernova remnant is the nebulous gas left over from a supernova
            explosion. This gas expands at great speeds and rams into the surrounding
            interstellar gas. This excites the surrounding gas and causes it to glow, producing
            the nebulous cloud we observe from Earth. A supernova remnant contains a neutron
            star or pulsar at its center, the core of the dying star. The cloud that enshrouds
            the core does not last long, though. After about 50,000 years, the gas mixes into
            the interstellar medium and no longer glows. Astronomically, this is a very short
            time, so the supernova remnants we see must be left from explosions that have
            occurred recently, cosmically speaking. Census: 112 supernova remnants."""
            },
        "meta_name": "Supernova Remnants",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)",
    },
    'h2_regions': {
        "renderable": "RenderablePolygonCloud",
        "filename": "h2",
        "asset_dir": "h2_regions",
        "Enabled": "false",
        "local_modules": True,
        "data": {
            "File": "h2.csv",
            "Name": "HII Regions Speck Files",
            "Identifier": "digitaluniverse_h2regions_speck",
            "Version": 4
            },
        "Unit": "pc",
        "PolygonSides": "6",
        "Opacity": "0.7",
        "Identifier": "HIIRegions_test",
        "FixedColor": "0.0, 0.5, 1.0",
        "ScaleExponent": "18.5",
        "MaxSize": "8.0",
        "Labels": {
            "csv": True,
            "Color": "0.5, 0.5, 0.5",
            "Size": "16.24",
            "MinMaxSize": "4, 20"
            },
        "GUI": {
            "Name": "HII Regions -test",
            "Path": "/Milky Way/Nebulae",
            "Description": """HII (pronounced "H-two") regions are stellar nurseries for newborn
            stars. Stars are born from condensing clouds of hydrogen gas. As these clouds
            condense, the densities become high enough to form stars. An HII region is the
            surrounding clouds of hydrogen that glow from the stars born within them. The
            result is a bright, glowing nebula which is seen to great distances. One local
            celebrity among HII regions is the Orion Nebula (M42). These star-forming regions
            lie in the plane of the Galaxy because that is where star formation occurs in
            spiral galaxies such as our Milky Way. Because of this, they are great tracers of
            the spiral arms of the Galaxy. Census: 1,108 star-forming regions."""
            },
        "meta_name": "HII Regions",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)",
    },
    'ob_associations': {
        "renderable": "RenderablePolygonCloud",
        "filename": "ob",
        "Enabled": "false",
        "asset_dir": "ob_association",
        "local_modules": True,
        "data": {
            "File": "ob.csv",
            "Name": "OB Associations Speck Files",
            "Identifier": "digitaluniverse_obassociations_speck",
            "Version": 4
            },
        "PolygonSides": "7",
        "Unit": "pc",
        "Identifier": "OBAssociations_test",
        "FixedColor": None,  # No fixed color specified in the asset file
        "Opacity": "0.7",
        "ColorMapping": {
            "File": "ob.cmap",
            "Enabled": "true",
            "ParameterOptions": [{"Key": "armID", "Range": "1.0, 3.0"}],
            "Name": "OB Associations Speck Files",
            "Identifier": "digitaluniverse_obassociations_speck",
            "Version": 4
            },
        "ScaleExponent": "16.9",
        "MaxSize": "17",
        "SizeMapping_ParameterOptions": "diameter",
        "Labels": {
            "csv": True,
            "Color": "0.4, 0.5, 1.0",
            "Size": "16.24",
            "MinMaxSize": "4, 25"
            },
        "GUI": {
            "Name": "OB Associations-test",
            "Path": "/Milky Way/Star Clusters",
            "Description": """Stellar associations are loose agglomerations of stars that form from
            the same gas cloud. OB associations typically have on the order of dozens of O and
            B stars in them (hotter, massive, younger stars) in addition to cooler stars. Over
            time the stars disperse and the association is less concentrated. These associations
            track relatively recent star formation. Colors: Blue trace the Sagittarius Arm,
            Purple are in the local Orion Spur, and Orange are in the Perseus Arm. Census: 61 OB
            associations."""
            },
        "meta_name": "OB Associations",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)",
    },
    'globular_clusters': {
        "renderable": "RenderablePolygonCloud",
        "filename": "gc",
        "Enabled": "false",
        "asset_dir": "globular_clusters",
        "local_modules": True,
        "data": {
            "File": "gc.csv",
            "Name": "Globular Clusters Speck Files",
            "Identifier": "digitaluniverse_globularclusters_speck",
            "Version": 3
            },
        "PolygonSides": "5",
        "Unit": "pc",
        "Identifier": "GlobularClusters_test",
        "FixedColor": "0.8, 0.8, 0.0",
        "Opacity": "0.65",
        "ScaleExponent": "18.6",
        "MaxSize": "13.0",
        "Labels": {
            "csv": True,
            "Color": "0.36, 0.36, 0.0",
            "Size": "16.7",
            "MinMaxSize": "4, 20"
            },
        "GUI": {
            "Name": "Globular Clusters-test",
            "Path": "/Milky Way/Star Clusters",
            "Description": """Globular star clusters are gravitationally bound groups of 100,000
            to 1 million stars. They are compact, spherical "balls" of stars with very high
            stellar densities. These clusters are typically 30 to 100 light years in diameter.
            Census: 161 globular clusters."""
            },
        "meta_name": "Globular Clusters",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)",
    },
    'manga': {
        "renderable": "RenderablePolygonCloud",
        "filename": "manga",
        "Enabled": "false",
        "asset_dir": "manga",
        "local_modules": True,
        "data": {
            "File": "manga.csv",
            }, # this data doesn't exist in OpenSpace yet
        "PolygonSides": "5",
        "Unit": "Mpc",
        "Identifier": "MaNGA_test",
        "FixedColor": "0.8, 0.8, 0.0",
        "Opacity": "0.8",
        "ScaleExponent": "22.6",
        "MaxSize": "0.15",
        "FadeInDistances": "220.0, 650.0",
        "GUI": {
            "Name": "MaNGA Nearby Galaxy Catalog -test",
            "Path": "/Universe/Deep Sky Surveys",
            "Description": """MaNGA Nearby Galaxy Catalog."""
            },
        "meta_name": "SDSS4 MaNGA",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)",
    },
    'stars' : {
        "renderable": "RenderableStars",
        "filename": "stars",
        "asset_dir": "stars",
        "local_modules": True,
        "data": {
            "File": "stars.speck",
            "Name": "Stars Speck Files",
            "Identifier": "stars_du",
            "Version": 6
            },
        "Texture": {
            "Glare": "halo.png",
            "Core": "glare.png",
            "Name": "Stars Textures",
            "Identifier": "stars_textures",
            "Version": 1
            },
        "ColorMap":{
            "ColorMap": "colorbv.cmap",
            "OtherDataColorMap": "viridis.cmap",
            "Name": "Stars Color Table",
            "Identifier": "stars_colormap",
            "Version": 3
            },
        "Identifier": "Stars_test",
        "Bv_column": "colorb_v",
        "Luminance_column": "lum",
        "AbsoluteMagnitude_column": "absmag",
        "ApparentMagnitude_column": "appmag",
        "Vx_column": "vx",
        "Vy_column": "vy",
        "Vz_column": "vz",
        "Speed_column": "speed",
        "GUI": {
            "Name": "Stars -test",
            "Path": "/Milky Way/Stars",
            "Description": """These are the nearby stars that surround the Sun and are close enough
            to get accurate distances. These include all the stars we see with the unaided eye
            and many stars dimmer than that. Over the entire night sky, all year round, and in
            the northern and southern hemispheres, we can see roughly 9,000 stars total with
            the unaided eye. Stars are the light factories of the universe, and come in a
            variety of sizes, colors, and brightnesses. The base catalog is Hipparcos, with Gaia
            DR3 data applied for distance and velocity when available. Census: 112,746 stars."""
            },
        "meta_name": "Stars",
        "author":  "Brian Abbott, Zack Reeves, Andrew Ayala, Jackie Faherty, Ally Baldelli (AMNH)"
    },
    'quasars': {
        "renderable": "RenderablePointCloud",
        "filename": "quasars",
        "Enabled": "true",
        "asset_dir": "quasars",
        "local_modules": True,
        "data": {
            "File": "qso.csv",
            "Name": "Quasars Speck Files",
            "Identifier": "digitaluniverse_quasars_speck",
            "Version": 3
            },
        "Texture": {
            "File": "point3A.png",
            "Name": "Point Textures",
            "Identifier": "digitaluniverse_point_textures",
            "Version": 1
            },
        "Unit": "Mpc",
        "Identifier": "Quasars_test",
        "FixedColor": "0.85, 0.35, 0.18",
        "Opacity": "0.95",
        "ColorMapping": {
            "Name": "Quasars Colormap",
            "Identifier": "digitaluniverse_quasars_colormap",
            "Version": 1,
            "File": "viridis.cmap",
            "Enabled": "false",
            "ParameterOptions": [{"Key": "lookback_time", "Range": "1.4, 13.0"}]
            },
        "ScaleExponent": "23.5",
        "MaxSize": "0.3",
        "FadeInDistances": "1000.0, 10000.0",
        "GUI": {
            "Name": "Quasars-test",
            "Path": "/Universe/Deep Sky Surveys",
            "Description": """Quasars are the most distant objects we see. They are extremely
            active galaxies that contain supermassive black holes which gobble up material at a
            furious rate. As the material falls into the black hole, it forms a disk and emits
            high-energy light that we see to great distances. Census: 755,850 quasars."""
            },
        "meta_name": "Quasars",
        "author": "Brian Abbott, Sohum Udani, Ally Baldelli (AMNH)"
    },
    'black_holes': {
        "renderable": "RenderablePointCloud",
        "filename": "bh",
        "Enabled": "false",
        "asset_dir": "black_holes",
        "local_modules": True,
        "data": {
            "File": "bh.csv" # This data doesn't exist in OpenSpace yet
            },
        "Texture": {
            "File": "point4.png",
            "Name": "Point Textures",
            "Identifier": "digitaluniverse_point_textures",
            "Version": 1
            },
        "Unit": "pc",
        "Identifier": "BlackHole_test",
        "FixedColor": "0.3, 0.15, 0.9",
        "Opacity": None,  # No opacity specified in the asset file
        "ScaleExponent": "19.0",
        "MaxSize": "13.0",
        "GUI": {
            "Name": "Black Hole- test",
            "Path": "/Milky Way/Stellar Remnants",
            "Description": """BlackCAT: A catalogue of stellar-mass black holes in X-ray transients"""
            },
        "meta_name": "Black Holes",
        "author": "Zack Reeves, Brian Abbott,  Ally Baldelli (AMNH)"
        },
    'planetary_nebulae': {
        "renderable": "RenderablePolygonCloud",
        "filename": "pn",
        "Enabled": "false",
        "asset_dir": "planetary_nebulae",
        "local_modules": True,
        "data": {
            "File": "pn.csv",
            "Name": "Planetary Nebulae Speck Files",
            "Identifier": "digitaluniverse_planetarynebulae_speck",
            "Version": 3
            },
        "PolygonSides": "3",
        "Unit": "pc",
        "Identifier": "PlanetaryNebulae_test",
        "FixedColor": "0.4, 0.4, 0.9",
        "Opacity": "0.99",
        "ScaleExponent": "18.2",
        "MaxSize": "19.0",
        "Labels": {
            "csv": True,
            "Color": "0.35, 0.35, 0.60",
            "Size": "16.24",
            "MinMaxSize": "4, 25"
            },
        "GUI": {
            "Name": "Planetary Nebulae -test",
            "Path": "/Milky Way/Nebulae",
            "Description": """A planetary nebula is an expanding shell of gas ejected from an
            average-sized star late in its life cycle. Appearing like greenish disks to a
            telescopic observer, planetary nebulae received their name from their resemblance to
            the gaseous planets of our solar system. In no way are they related to planets,
            rather, they are products of dying stars. As the gas from the star expands, it
            sweeps up the cooler gas like a snowplow. The gas glows because of the ultraviolet
            light from the stellar remnant at the center. Because the planetary nebula phase of
            a star's evolution is relatively short, we observe only those that have occurred
            recently in the younger stellar population. Therefore, we expect to see planetary
            nebulae in the disk of the Galaxy. Census: 1,657 planetary nebulae."""
            },
        "meta_name": "Planetary Nebulae",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)"
    },
    'star_uncertainty': {
        "renderable": "RenderableConstellationLines",
        "filename": "stellar_uncertainty",
        "Identifier": "StarUncertainty_test",
        "Enabled": "false",
        "asset_dir": "stellar_uncertainty",
        "local_modules": True,
        "data": {
            "File": "star_uncertainty.speck",
            "NamesFile": "star_uncertainty.dat",
            "Name": "Star Distance Uncertainty Files",
            "Identifier": "digitaluniverse_star_uncertainty_data",
            "Version": 1
            }, 
        "Opacity": "0.8",
        "LineWidth": "5.0",
        "Labels": {
            "File": "star_uncertainty.label",
            "Color": "0.6, 0.6, 1.0",
            "Size": "14.1",
            "MinMaxSize": "8, 170"
            },
        "Unit": "pc",
        "DimInAtmosphere": 'true',
        "Colors":  "{1.0, 1.0, 0.0}, {0.0, 0.8, 1.0}, {0.957, 0.51, 0.10}",
        "GUI": {
            "Name": "Star Distance Uncertainty-test",
            "Path": "/Milky Way/Stars",
            "Description": """The uncertainty of a star's position is derived from the uncertainty
            in its parallax measurement. This results in a range in distance where the star
            could exist. Here we draw lines on top of select stars which give us a visual cue
            of the range in possible distances for that star. Colors: Aqua lines are stars with
            Gaia geometric parallax measurements (the most accurate), orange lines indicate
            stars with Hipparcos geometric parallaxes, and yellow lines are stars with Gaia
            photogeometric parallaxes (the least accurate). The label includes the star name
            and the length of the uncertainty in light years. Census: 3,440 stars with
            uncertainty."""
            },
        "meta_name": "Star Distance Uncertainty",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)",
    },
    'constellations': {
        "renderable": "RenderableConstellationLines",
        "Identifier": "Constellations_test",
        "zodiacs": True,
        "constellation_actions": True,
        "local_modules": True,
        "filename": "constellations",
        "Enabled": "false",
        "asset_dir": "constellations",
        "data": {
            "File": "constellation_lines.speck",
            "NamesFile": "constellations.dat",
            "Name": "Constellation Files",
            "Identifier": "digitaluniverse_constellations_data",
            "Version": 3
            },
        "Opacity": "0.3",
        "LineWidth": None,  # Not specified in the asset file
        "Labels": {
            "csv": False,  
            "File": "constellation_lines.label",
            "Color": "0.8, 0.8, 0.8",
            "Size": "14.5",
            "MinMaxSize": "8, 170"
            },
        "Unit": "pc",
        "DimInAtmosphere": 'true',
        "Colors": '{0.6, 0.4, 0.4}, {0.8, 0.0, 0.0}, {0.0, 0.3, 0.8}' ,
        "GUI": {
            "Name": "Constellation Lines -test",
            "Path": "/Milky Way/Constellations",
            "Description": """Lines connecting the stars that make up the constellation figures.
            We represent the constellations by connecting the main stars that make up the
            constellation "stick figures," as seen from Earth. Colors: most constellations
            are pink, while the zodiacal constellations are red. We also color Orion and Ursa
            Major blue as two recognizable constellations in the night sky. Census: 88
            constellations."""
            },
        "meta_name": "Constellations",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)",
    },
    'constellation_bounds': {
        "renderable": "RenderableConstellationBounds",
        "filename": "constellation_bounds",
        "Enabled": "false",
        "asset_dir": "constellations",
        "local_modules": True,
        "data": {
            "File": "constellation_boundaries.dat",
            "NamesFile": "constellations.dat",
            "Name": "Constellation Files",
            "Identifier": "digitaluniverse_constellations_data",
            "Version": 1
            },
        "Identifier": "ConstellationBounds-test",
        "GUI": {
            "Name": "Constellation Boundaries-test",
            "Path": "/Milky Way/Constellations",
            "Description": """As a continent is divided into countries, astronomers divide the sky
            into 88 regions called constellations. Every object falls into one of these 88
            regions. The boundaries of these regions are shown in this asset. Use these in
            concert with the constellation labels. Census: 88 constellations."""
        },
        "meta_name": "Constellation Bounds",
        "author": "Brian Abbott and Ally Baldelli (AMNH)"
    },
    'star_orbits': {
        "renderable": "RenderableDUMeshes",
        "filename": "star_orbits",
        "Enabled": "false",
        "asset_dir": "star_orbits",
        "local_modules": True,
        "data_folder": "",
        "data": {
            "Name": "Star Orbits Speck Files",
            "Identifier": "digitaluniverse_starorbits_speck",
            "Version": 2
            },
        "Unit": "pc",
        "Opacity": "1.0",
        "objects": {"SunOrbit": {
                        "Identifier": "SunOrbit_test",
                        "speck_file": "starorbits-Sun.speck",
                        "MeshColor": "1.0, 0.65, 0.0",
                        "GUI": {
                            "Name": "Sun Orbit -test",
                            "Path": "/Milky Way/Stars/Stars Orbits",
                            "Description": """Projected orbit of the Sun around the Milky Way over the next 1 billion years.""" 
                            }
                        },
                    "BarnardsOrbit":  {
                        "Identifier": "BarnardsOrbit_test",
                        "speck_file": "starorbits-BarnardsStar.speck",
                        "MeshColor": "0.39, 0.58, 0.93",
                        "GUI": {
                            "Name": "Barnards Orbit -test",
                            "Path": "/Milky Way/Stars/Stars Orbits",
                            "Description": """Projected orbit of the Barnard's Star around the Milky Way over the next 1 billion years.""" 
                            }
                        },
                    "KapteynsOrbit":  {
                        "Identifier": "KapteynsOrbit_test",
                        "speck_file": "starorbits-KapteynsStar.speck",
                        "MeshColor": "0.6, 0.6, 0.6",
                        "GUI": {
                            "Name": "Kapteyns Orbit -test",
                            "Path": "/Milky Way/Stars/Stars Orbits",
                            "Description": """Projected orbit of the Kapteyn's Star around the Milky Way over the next 1 billion years."""
                            } 
                        },
                    "Lacaille9352Orbit":  {
                        "Identifier": "Lacaille9352Orbit_test",
                        "speck_file": "starorbits-Lacaille9352.speck",
                        "MeshColor": "0.58, 0.0, 0.83",
                        "GUI": {
                            "Name": "Lacaille 9352 Orbit -test",
                            "Path": "/Milky Way/Stars/Stars Orbits",
                            "Description": """Projected orbit of the Lacaille9352 around the Milky Way over the next 1 billion years.""" 
                            }
                        }, 
                    "LSR1826Orbit":  {
                        "Identifier": "LSR1826Orbit_test",
                        "speck_file": "starorbits-LSR1826+3014.speck",
                        "MeshColor": "0.0, 0.39, 0.0",
                        "GUI": {
                            "Name": "LSR1826+3014 Orbit -test",
                            "Path": "/Milky Way/Stars/Stars Orbits",
                            "Description": """Projected orbit of the LSR1826+3014 around the Milky Way over the next 1 billion years.""" 
                            }
                        },
                    "LSRJ0822Orbit":  {
                        "Identifier": "LSRJ0822Orbit_test",
                        "speck_file": "starorbits-LSRJ0822+1700.speck",
                        "MeshColor": "0.5, 1.0, 0.0",
                        "GUI": {
                            "Name": "LSRJ0822+1700 Orbit -test",
                            "Path": "/Milky Way/Stars/Stars Orbits",
                            "Description": """Projected orbit of the LSRJ0822+1700 around the Milky Way over the next 1 billion years.""" 
                            }
                        },
                    "PM_J13420Orbit":  {
                        "Identifier": "PM_J13420Orbit_test",
                        "speck_file": "starorbits-PM_J13420-3415.speck",
                        "MeshColor": "0.70, 0.13, 0.13",
                        "GUI": {
                            "Name": "PM_J13420-3415 Orbit -test",
                            "Path": "/Milky Way/Stars/Stars Orbits",
                            "Description": """Projected orbit of the PM_J13420-3415 around the Milky Way over the next 1 billion years.""" 
                            }
                        }
                    }, # end of objects
        "meta_name": "Star Orbits",
        "meta_description": """Projected star orbits for selected stars over the next 1 billion years. Census: 7 star orbits.""",
        "author": "Brian Abbott, Zack Reeves, Ally Baldelli (AMNH)"
    } # end of star_orbits

} # master_dictionary

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