import logging
import unicornhat as uh
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)
uh.set_layout(uh.PHAT)
width,height=uh.get_shape()

def critical(blink,bright):
    logger.info('Red alert for '+ str(blink) +' s with brightness '+ str(bright)) 
    light(blink,bright,255,0,0)
    return True

def warning(blink,bright):
    logger.info('Orange alert for '+ str(blink) +' s with brightness '+ str(bright)) 
    light(blink,bright,255,129,0)
    return True

def info(blink,bright):
    logger.info('Green alert for '+ str(blink) +' s with brightness '+ str(bright)) 
    light(blink,bright,55,100,0)
    return True

def clear():
    logging.info('No alert')   
    uh.clear()
    uh.show()
    return True

def light(blink,bright,red,green,blue):
    for b in range(blink):
        clear()
        uh.brightness(bright)
        time.sleep(0.5)
        for w in range(8):
            for h in range(4):
                logging.info('No alert') 
                uh.set_pixel(w, h, red, green, blue)
                uh.show()
        time.sleep(0.5)
