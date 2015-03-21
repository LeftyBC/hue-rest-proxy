#!/usr/bin/env python

import logging
logging.basicConfig(filename="hue-rest.log", level=logging.DEBUG)

from hue import set_lights, set_light_off, set_light_on
from bottle import route, run, response, Bottle

from config_file import all_lights, groups, listen_ip, listen_port

app = Bottle()


# e.g. localhost:10000/light/1/red/255/green/255/blue/255
# to set light 1 to white
@app.route('/light/<light>/red/<red>/green/<green>/blue/<blue>')
def single_light(light, red, green, blue):
    set_lights(light, red, green, blue)
    return({ "status": "ok" })

# e.g. localhost:10000/light/1/off
# to turn light 1 off
@app.route('/light/<light>/off')
def turn_light_off(light):
    set_light_off(light)
    return({ "status": "ok"})

# e.g. localhost:10000/light/1/on
# to turn light 1 on
@app.route('/light/<light>/on')
def turn_light_on(light):
    set_light_on(light)
    return({ "status": "ok"})

# e.g. localhost:10000/lights/all/on
# to turn all lights on
@app.route('/lights/all/on')
def all_lights_on():
    for light in all_lights:
        set_light_on(light)
    return({ "status": "ok" })

# e.g. localhost:10000/lights/all/off
# to turn all lights off
@app.route('/lights/all/off')
def all_lights_off():
    for light in all_lights:
        set_light_off(light)
    return({ "status": "ok" })

# e.g. localhost:10000/lights/all/red/255/green/255/blue/255
# to set all lights to white
@app.route('/lights/all/red/<red>/green/<green>/blue/<blue>')
def set_all_lights(red, green, blue):
    for light in all_lights:
        set_lights(light, red, green, blue)
    return({ "status": "ok"})

# e.g. localhost:10000/group/bedroom/on
# to turn bedroom lights on
@app.route('/group/<group>/on')
def turn_group_on(group):
    if group in groups:
        for light in groups[group]:
            set_light_on(light)
    return({ "status": "ok"})

# e.g. localhost:10000/group/bedroom/off
# to turn bedroom lights off
@app.route('/group/<group>/off')
def turn_group_off(group):
    if group in groups:
        for light in groups[group]:
            set_light_off(light)
    return({ "status": "ok"})


# e.g. localhost:10000/group/bedroom/red/255/green/255/blue/255
# to set all bedroom lights to white
@app.route('/group/<group>/red/<red>/green/<green>/blue/<blue>')
def set_group_colour(group, red, green, blue):
    if group in groups:
        for light in groups[group]:
            set_lights(light, red, green, blue)

    return({ "status": "ok"})


@app.hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


if __name__ == "__main__":
    run(app, host=listen_ip, port=listen_port)
