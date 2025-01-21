import logging
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))  

logger = logging.getLogger('protein_analysis')
logger.setLevel(logging.WARNING)  # Only warning and above will be processed

# Create handlers for different log files
warning_handler = logging.FileHandler('logs/warnings.log')
error_handler = logging.FileHandler('logs/errors.log')

# 1. Create formatters
warning_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
error_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 2. Set handler levels
warning_handler.setLevel(logging.WARNING)
error_handler.setLevel(logging.ERROR)

# 3. Add handlers to logger
warning_handler.setFormatter(warning_format)
error_handler.setFormatter(error_format)
logger.addHandler(warning_handler)
logger.addHandler(error_handler)

# 4. Test the system
logger.warning('Warning: Protein sequence mismatch detected')
logger.error('Error: Protein folding simulation failed')