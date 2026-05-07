# Now to log into a different module can create a logger object and use it to log messages.
import logging
logger = logging.getLogger(__name__) # __name__ a special variable that holds the name of current module.
logger.info("Info from logger object")