import unittest
from pathlib import Path
import logging

log_dir = Path(__file__).parent / "webtest"
log_dir.mkdir(exist_ok=True)

log_file = log_dir / "log_webtest.log"

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(log_file, mode='w')
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logging.info("Spouštím hlavní testovací modul")

import webtest.logintest

# main
if __name__ == '__main__': 
    unittest.main(module=webtest.logintest, verbosity=2)
