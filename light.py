import logging
import unicornhat as uh
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)
uh.set_layout(uh.PHAT)
width,height=uh.get_shape()

def red(blink,bright):
    
    logger.info('red alert for '+ str(blink) +' s with brightness '+ str(bright)) 
    uh.brightness(bright)
    for x in range(blink):
        clear()
        time.sleep(0.5)
        for y in range(height):
            for x in range(width):
                uh.set_pixel(x, y, 255, 0, 0)
        uh.show()
        time.sleep(0.5)
    return True

def clear():
    logging.info('No alert')   
    uh.clear()
    uh.show()
    return True