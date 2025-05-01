from asset_creation import *
from asset_dict import *


keys = data_info_names()

for key in keys:
    make_RPC_asset(data_info(key))