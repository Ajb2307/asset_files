from asset_creation import *
from asset_dict import *


keys = data_info_names()

for key in keys:
    try: 
        write_asset(data_info(key))
    except Exception as e:
        print(f"Error writing asset for {key}: {e}")