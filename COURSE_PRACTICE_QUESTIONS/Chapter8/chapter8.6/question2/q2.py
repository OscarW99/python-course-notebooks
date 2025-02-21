import logging
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))  

logger = logging.getLogger('sequence_analyzer')

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('logs/sequence_analysis.log')

# Your code here to:
# 1. Create formatters
# 2. Apply formatters to handlers
# 3. Add handlers to logger
# 4. Test the configuration