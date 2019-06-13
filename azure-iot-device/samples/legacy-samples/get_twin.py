# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import os
import logging
from azure.iot.device import IoTHubDeviceClient
from azure.iot.device import auth

# logging.basicConfig(level=logging.DEBUG)

conn_str = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")
auth_provider = auth.from_connection_string(conn_str)
device_client = IoTHubDeviceClient.from_authentication_provider(auth_provider, "mqtt")

# connect the client.
device_client.connect()

# get the twin
twin = device_client.get_twin()
print("Reported temperature is {}".format(twin["reported"]["temperature"]))

# Finally, disconnect
device_client.disconnect()