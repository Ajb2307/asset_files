from asset_creation import *
from asset_dict import *


keys = data_info_names()

for key in keys:
    if key in ["manga", "black_holes", "star_orbits", "star_labels", "alternate_star_labels", "constellation_boundaries"]:
        continue
    try: 
        datainfo = data_info(key)
        datainfo['asset_dir'] = "test_assets"
        datainfo["local_modules"] = False
        datainfo["filename"] = datainfo["filename"] + "test"
        datainfo["data"]["File"] = datainfo["data"]["File"].replace(".csv", ".speck")
        write_asset(datainfo)
        #write_asset(data_info(key))
    except Exception as e:
        print(f"Error writing asset for {key}: {e}")


datainfo = data_info("star_orbits")
datainfo["local_modules"] = False
datainfo['asset_dir'] = "test_assets"
datainfo["filename"] = datainfo["filename"] + "test"
#datainfo["data"]["File"] = datainfo["data"]["File"].replace(".csv", ".speck")
write_asset(datainfo)