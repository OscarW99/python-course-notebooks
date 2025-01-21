import logging
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))  

# Create logger
logger = logging.getLogger('dna_processor')
logger.setLevel(logging.DEBUG)  # Set logger level to lowest so all messages are processed

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('logs/dna_processing.log')

# 1. Set handler levels
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.INFO)

# 2. Create and set formatters
console_formatter = logging.Formatter('%(levelname)s - %(message)s')
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

# 3. Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 4. Test with log messages
logger.debug('Debug message for DNA processing')
logger.info('Info message for DNA processing')
logger.warning('Warning message for DNA processing')
logger.error('Error message for DNA processing')
logger.critical('Critical message for DNA processing')