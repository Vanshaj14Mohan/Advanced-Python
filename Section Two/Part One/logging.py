# In this part we'll learn about logging in python and how to use it to log messages in our code
# Logging is just a way to keep track of events that happen when some software runs.
# In this part we'll look into different logging levels, different configurations options
# How to log in different modules, how to use different log handlers, capturing stack traces and using rotating file handlers.

import logging
# After importing we can log into five different levels
# 1: debug, 2 info, 3 warning, 4 error, 5 critical
logging.debug("A debug message")
logging.info("An info message")
logging.warning("A warning message")
logging.error("An error message")
logging.critical("A critical message")

#Only warning, error and critical will be logged by default as default logging level is warning.
# Can change the logging level to debug to log all messages.