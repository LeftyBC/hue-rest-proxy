#!/usr/bin/env python

# This file specifies configuration for the REST server

listen_ip   = '0.0.0.0'   # all interfaces
listen_port = 10000

# the IP of the Hue bridge
default_bridge_ip = "10.10.92.106"

# the list of lights to control when using /lights/all
all_lights = [1, 2, 3 ,4, 5]

# groups of lights
groups = {
    'bed': [ 1 ],
    'desk': [ 2, 3 ],
    'workbench': [ 4, 5 ],
    'first_two': [ 1, 3 ],
    'all': all_lights
}
