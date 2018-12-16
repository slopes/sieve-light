from flask import render_template
import connexion
import socket
import logging
import time
import unicornhat as uh

logger = logging.getLogger()
logger.setLevel(logging.INFO)

empty = 0,0,0
full= 0,0,255

ZERO = [
    [empty, full, full, full,full, full, full, empty],
    [full, empty, empty, empty,full, empty, empty, full],
    [full, empty, empty, full,empty, empty, empty, full],
    [empty, full, full, full,full, full, full, empty]
  
]

ONE = [
    [empty, empty, empty, empty,empty, empty, empty, full],
    [full, full, full, full,full, full, full, full],
    [full, empty, empty, empty,empty, empty, empty, full],
    [empty, empty, empty, empty,empty, empty, empty, full]
]

TWO = [
    [empty, full, full, full,empty, empty, empty, full],
    [full, empty, empty, empty,full, empty, empty, full],
    [full, empty, empty, empty,full, empty, empty, full],
    [full, empty, empty, empty,empty, full, full, empty]
]

THREE = [
    [empty, full, full, empty,full, full, full, empty],
    [full, empty, empty, full,empty, empty, empty, full],
    [full, empty, empty, full,empty, empty, empty, full],
    [full, empty, empty, empty,empty, empty, empty, full]
]

FOUR = [
    [empty, empty, empty, empty,full, empty, empty, empty],
    [full, full, full, full,full, full, full, full],
    [empty, full, empty, empty,full, empty, empty, empty],
    [empty, empty, full, full,full, empty, empty, empty]    
]

FIVE = [
    [full, empty, empty, empty,full, full, full, empty],
    [full, empty, empty, full,empty, empty, empty, full],
    [full, empty, empty, full,empty, empty, empty, full],
    [full, full, full, empty,empty, empty, empty, full]
]

SIX = [
    [full, empty, empty, empty,full, full, full, empty],
    [full, empty, empty, full,empty, empty, empty, full],
    [full, empty, empty, full,empty, empty, empty, full],
    [empty, full, full, full,full, full, full, empty]
]

SEVEN = [
    [full, full, full, empty,empty, empty, empty, empty],
    [full, empty, empty, full,full, empty, empty, empty],
    [full, empty, empty, full,empty, full, full, empty],
    [full, empty, empty, empty,empty, empty, empty, full]
]

EIGHT = [
    [empty, full, full, full,empty, full, full, empty],
    [full, empty, empty, empty,full, empty, empty, full],
    [full, empty, empty, empty,full, empty, empty, full],
    [empty, full, full, full,empty, full, full, empty]
]

NINE = [
    [empty, full, full, full,full, full, full, empty],
    [full, empty, empty, empty,full, empty, empty, full],
    [full, empty, empty, empty,full, empty, empty, full],
    [empty, full, full, full,empty, empty, empty, full]
]

DOT = [
    [empty, empty, empty, empty,empty, empty, empty, empty],
    [empty, empty, empty, empty,empty, empty, full, full],
    [empty, empty, empty, empty,empty, empty, full, full],
    [empty, empty, empty, empty,empty, empty, empty, empty]
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

def display(digit):
    uh.off()
    uh.set_pixels(digit)
    uh.show()
    time.sleep(5)

def init():
    uh.set_layout(uh.PHAT)
    uh.brightness(0.5)
    for c in get_ip() :
        if c == '0' :
            display(ZERO) 
        elif c == '1' :
            display(ONE) 
        elif c == '2' :
            display(TWO) 
        elif c == '3' :
            display(THREE) 
        elif c == '4' :
            display(FOUR) 
        elif c == '5' :
            display(FIVE) 
        elif c == '6' :
            display(SIX) 
        elif c == '7' :
            display(SEVEN) 
        elif c == '8' :
            display(EIGHT) 
        elif c == '8' :
            display(NINE)
        else :
            display(DOT) 
    
# create the application instance
app = connexion.App(__name__, specification_dir="./")

# Cead the swagger.yml file to configure the endpoints
app.add_api("swagger.yml")

if __name__ == "__main__":
    logging.info('Server stating : ' + get_ip()) 
    init()
    app.run(host='0.0.0.0', port=5000, debug=True)



