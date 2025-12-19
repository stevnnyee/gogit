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
import argparse

logger = logging.getLogger(__name__)

def main():
    logger.info("Starting Go Git")
    logger.info("Go Git is a simple version of git that allows you to create a repository and commit changes to it.")

    parser = argparse.ArgumentParser(description="Go Git is a simple version of git that allows you to create a repository and commit changes to it.")
    parser.add_argument("command", help="The command to execute")
    parser.add_argument("args", help="The arguments to the command")
    args = parser.parse_args()

    if args.command == "init":
        init()
    elif args.command == "add":
        add()
    elif args.command == "commit":
        commit()

        BAKAAAAA MAKA SHAKALAKA PAKABAKAfsadfasdfasdf