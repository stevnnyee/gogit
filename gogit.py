"""Go git is a simple version of git that allows you to create a repository and commit changes to it."""

import collections as col
import os
import sys
import time
import datetime
import hashlib
import json
import logging
import logging.handlers
import logging.config
import logging.handlers 

logger = logging.getLogger(__name__)

def main():
    logger.info("Starting Go Git")
    logger.info("Go Git is a simple version of git that allows you to create a repository and commit changes to it.")