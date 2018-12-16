import logging
import unicornhat as uh

uh.set_layout(uh.PHAT)
uh.brightness(0.5)

def red():
    logging.info('red alert') 
    uh.set_pixel(0, 0, 255, 0, 0)
    uh.show()
    return True

def clear():
    logging.info('No alert') 
    uh.clear()
    uh.show()
    return True