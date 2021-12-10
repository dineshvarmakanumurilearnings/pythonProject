import logging
print("Start logging into a file......")
logging.basicConfig(filename='C://Users//LENOVO//Desktop//New folder//loggingfile.txt',level=logging.DEBUG)
logging.critical("This is a CRITICAL msg")
logging.error("This is a ERROR msg")
logging.warning("This is a WARNING msg")
logging.info("This is a INFO msg")
logging.debug("This is a DEBUG msg")
print("End logging into a file......")



