import os

from helpers.sample import hello_world

if __name__ == "__main__":
    hello_world()
    print('Environment Variable: ', os.environ['TEST_PW'])
