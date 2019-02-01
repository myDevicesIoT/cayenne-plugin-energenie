# Cayenne Energenie Pi-mote Plugin
A plugin allowing the [Cayenne Pi Agent](https://github.com/myDevicesIoT/Cayenne-Agent) to control electrical sockets using the Energie Pi-mote Control from the [Cayenne Dashboard](https://cayenne.mydevices.com).

## Requirements
### Hardware
* [Rasberry Pi](https://www.raspberrypi.org).
* [Energenie Pi-mote](https://energenie4u.co.uk/catalogue/category/Raspberry-Pi-Accessories)

### Software
* [Cayenne Pi Agent](https://github.com/myDevicesIoT/Cayenne-Agent). This can be installed from the [Cayenne Dashboard](https://cayenne.mydevices.com).
* [Git](https://git-scm.com/).

## Getting Started
### 1. Installation

   From the command line run the following commands to install this plugin.
   ```
   cd /etc/myDevices/plugins
   sudo git clone https://github.com/myDevicesIoT/cayenne-plugin-energenie.git
   cd cayenne-plugin-energenie
   sudo python3 setup.py install
   ```

### 2. Modifying the plugin 

   By default the plugin will create widgets for four sockets. If your device has fewer sockets you can set the `enabled` value to `false` in the `cayenne_energenie.plugin` file for any sockets you aren't using. Alternatively you can add the temporary widgets in the [Cayenne Dashboard](https://cayenne.mydevices.com) and then delete the ones you don't need.

### 3. Restarting the agent

   Restart the agent so it can load the plugin.
   ```
   sudo service myDevices restart
   ```
   Temporary widgets for the plugin should now show up in the [Cayenne Dashboard](https://cayenne.mydevices.com). You can make them permanent by clicking the plus sign.

   NOTE: If the temporary widgets do not show up try refreshing the [Cayenne Dashboard](https://cayenne.mydevices.com) or restarting the agent again using `sudo service myDevices restart`.