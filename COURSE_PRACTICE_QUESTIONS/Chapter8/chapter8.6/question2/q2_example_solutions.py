import logging
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))  

logger = logging.getLogger('sequence_analyzer')
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('logs/sequence_analysis.log')

# 1. Create formatters
console_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 2. Apply formatters to handlers
console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# 3. Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 4. Test the configuration
logger.debug('Debug message from sequence analyzer')
logger.info('Info message from sequence analyzer')
logger.warning('Warning message from sequence analyzer')
logger.error('Error message from sequence analyzer')