import os

from utils.sample import hello_world

if __name__ == "__main__":
    hello_world()
    print("Environment variable: ", os.environ["TEST_PW"])
    print("In production never print password to console! :)")
