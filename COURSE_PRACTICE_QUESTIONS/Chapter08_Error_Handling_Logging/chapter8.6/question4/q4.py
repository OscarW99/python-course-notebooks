import logging
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))  

logger = logging.getLogger('bio_pipeline')

def analyze_dna():
    """Sample function that uses logger"""
    logger.info('Starting DNA analysis')
    logger.warning('Analysis complete with some warnings')
    return "Analysis complete"

# Add your logging configuration here to:
# 1. Create and configure handlers
# 2. Create formatter including function name (%(funcName)s)
# 3. Add handlers to logger
# 4. Test by calling analyze_dna()