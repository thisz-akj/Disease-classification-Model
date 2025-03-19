import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from cnnClassifier import logger

from cnnClassifier import logger
logger.info("welcome to my custom log")