import logging
import random

def main(number_of_readings):
    # emit these log readings to kafka
    i=1
    while i<=number_of_readings:
        logger.info('reading:' + str(random.random()))
        i = i + 1


def setup_logging():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(pathname)s - line:%(lineno)d -  %(message)s", datefmt='%m/%d/%Y %H:%M:%S')
    log_handler = logging.StreamHandler()
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)


# this is used to run when this script file is called
# not when the function is imported in some other module
if __name__=='__main__':
    setup_logging()
    logger = logging.getLogger(__name__)
    main(number_of_readings=10000)
