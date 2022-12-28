
import argparse
import os
import platform
from logging.handlers import RotatingFileHandler
import logging
logger = logging.getLogger()

import farm

# https://thingspeak.com/channels/68316/private_show

def main():
    logger.info("PiFarm v1.0")
    logger.info(f'python-version = {platform.python_version()}')

    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", help="Debug mode, forces use of windows", action="store_true")
    args = parser.parse_args()

    farm.init_logs(args.debug)

    try:
        logger.debug(f'Setting up sensor array...')
        sensors = farm.Sensors()
        sensors.append(farm.RandomSensor())
        sensors.append(farm.RandomSensor())

        logger.debug(f'Starting farm monitor...')
        while True:
            ret = sensors.read()


    finally:
        pass

if __name__ == "__main__":
    main()
