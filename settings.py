import os
import pathlib

BASE_PATH = pathlib.Path(__file__).parent
CONFIG_PATH = os.path.join(BASE_PATH, 'config')
TEST_CONFIG = os.path.join(CONFIG_PATH, "test.yaml")
