# Philips Hue REST proxy

A Python REST proxy to the Philips Hue API.

Supports controlling all lights, groups of lights, or individual lights.

See rest_server.py for example URLs.


### Rationale

Yes, the Hue API is already a REST interface, but this allows the authentication to be stored on the server side, as well as allowing lights to be given RGB values instead of the native (and somewhat esoteric) HSV values that Philips uses.
