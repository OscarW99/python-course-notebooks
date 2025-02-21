import logging
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))  

logger = logging.getLogger('protein_analysis')

# Create handlers for different log files
warning_handler = logging.FileHandler('logs/warnings.log')
error_handler = logging.FileHandler('logs/errors.log')

# Your code here to:
# 1. Create formatters
# 2. Set handler levels
# 3. Add handlers to logger
# 4. Test the system