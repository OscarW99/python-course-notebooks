import logging
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))  

# Create logger
logger = logging.getLogger('dna_processor')

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('logs/dna_processing.log')

# Your code here to:
# 1. Set handler levels
# 2. Create and set formatters
# 3. Add handlers to logger
# 4. Test with log messages