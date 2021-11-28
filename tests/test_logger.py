import logging

# add filemode="w" to overwrite

class My_logger:

    def __init__(self):
        logging.basicConfig(filename="sample.log", level=logging.INFO)

        logging.debug("This is a debug message")
        logging.info("Informational message")
        logging.error("An error has happened!")