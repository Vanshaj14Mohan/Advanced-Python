# Now to log into a different module can create a logger object and use it to log messages.
import logging
logger = logging.getLogger(__name__) # __name__ a special variable that holds the name of current module.
logger.propagate = False # won't propagate to base logger
logger.info("Info from logger object")

import logging.config
logging.config.fileConfig("logging.config")

# Create handler
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("file.log")

# Level and format for each handler
stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s') # name, level and message of logger
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning("A normal warning")
logger.error("A normal error")
