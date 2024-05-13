import logging


# Faster logging
def setup_logging():
    # Setup
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Handler
    file_handler = ImmediateFlushFileHandler('restaurant_manager.log', mode='w')
    file_handler.setFormatter(formatter)

    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(file_handler)


class ImmediateFlushFileHandler(logging.FileHandler):
    def emit(self, record):
        super().emit(record)
        self.stream.flush()
