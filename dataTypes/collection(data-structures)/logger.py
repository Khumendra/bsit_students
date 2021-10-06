import logging
# create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="test.log",
                    level=logging.DEBUG, format=LOG_FORMAT, 
                    filemode="w")
logger = logging.getLogger()


# Test the logger
# logger.info("Our End Message.")

print(logger.level)

# Test messages
logger.debug("This is harmless debug message.")
logger.info("Just some useful info.")
logger.warning("I'm sorry, but I can't do that, Dave.")
logger.error("Did you just try to divide by zero.")
logger.critical("This entire internet is down!!")