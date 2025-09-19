import os
import time

class Utils:
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def wait(self, sg):
        time.sleep(sg)