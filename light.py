import logging

def red():
    logging.info('red alert') 
    return True

def clear():
    logging.info('No alert') 
    return True