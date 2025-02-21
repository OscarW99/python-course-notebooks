import logging
import os

#$ This Just Makes Sure We're Starting in the Right Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))  

logger = logging.getLogger('bio_pipeline')
logger.setLevel(logging.DEBUG)

def analyze_dna():
    """Sample function that uses logger"""
    logger.info('Starting DNA analysis')
    logger.warning('Analysis complete with some warnings')
    return "Analysis complete"

# 1. Create and configure handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('logs/bio_pipeline.log')

# 2. Create formatter including function name (%(funcName)s)
formatter = logging.Formatter('%(asctime)s - %(funcName)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 3. Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 4. Test by calling analyze_dna()
result = analyze_dna()
logger.info(f'Analysis result: {result}')