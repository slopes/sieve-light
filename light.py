import logging
import unicornhat as uh
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)
uh.set_layout(uh.PHAT)
width,height=uh.get_shape()

def light(blink,bright,red,green,blue):       
    uh.brightness(bright)
    for x in range(blink):
        clear()
        time.sleep(0.5)
        for y in range(height):
            for x in range(width):
                uh.set_pixe((x, y, red, green, blue)
        uh.show()
        time.sleep(0.5)
    

def critical(blink,bright):
    logger.info('Red alert for '+ str(blink) +' s with brightness '+ str(bright)) 
    light(blink,bright,255,0,0)
    return True

def warning(blink,bright):
    logger.info('Orange alert for '+ str(blink) +' s with brightness '+ str(bright)) 
    light(blink,bright,55,100,0)
    return True

def info(blink,bright):
    logger.info('Green alert for '+ str(blink) +' s with brightness '+ str(bright)) 
    light(blink,bright,60,91,89)
    return True

def clear():
    logging.info('No alert')   
    uh.clear()
    uh.show()
    return True