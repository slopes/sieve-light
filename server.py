from flask import render_template
import connexion
import socket
import logging
import unicornhat as uh

logger = logging.getLogger()
logger.setLevel(logging.INFO)

empty = 0,0,0
full= 0,0,255

null = [
    [empty, empty, empty, empty],
    [empty, empty, empty, empty],
    [empty, empty, empty, empty],
    [empty, empty, empty, empty],
    [empty, empty, empty, empty],
    [empty, empty, empty, empty],
    [empty, empty, empty, empty],
    [empty, empty, empty, empty]
]

ONE = [
    [empty, full, full, empty],
    [empty, empty, full, empty],
    [empty, empty, full, empty],
    [empty, empty, full, empty],
    [empty, empty, full, empty],
    [empty, empty, full, empty],
    [empty, empty, full, empty],
    [full, full, full, full]
]

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP 

def init():
    uh.set_layout(uh.PHAT)
    uh.brightness(0.5)
    uh.set_pixels(ONE)
    uh.show()

# create the application instance
app = connexion.App(__name__, specification_dir="./")

# Cead the swagger.yml file to configure the endpoints
app.add_api("swagger.yml")


if __name__ == "__main__":
    logging.info('Server stating : ' + get_ip()) 
    init()
    app.run(host='0.0.0.0', port=5000, debug=True)



