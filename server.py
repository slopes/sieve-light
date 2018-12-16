from flask import render_template
import connexion
import socket
import logging
import unicornhat as uh

logger = logging.getLogger()
logger.setLevel(logging.INFO)

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
    width,height=uh.get_shape()
    uh.brightness(0.5)
    uh.set_pixel(0,0, 255, 0, 0)
    uh.set_pixel(0,width, 0, 255, 0)
    uh.set_pixel(height,0, 0, 0, 255)
    uh.set_pixel(height,width, 255, 0, 255)

# create the application instance
app = connexion.App(__name__, specification_dir="./")

# Cead the swagger.yml file to configure the endpoints
app.add_api("swagger.yml")


if __name__ == "__main__":
    logging.info('Server stating : ' + get_ip()) 
    init()
    app.run(host='0.0.0.0', port=5000, debug=True)



