import os

from utils.sample import hello_world  # import of module from subfolder

"""
This script should serve as entrypoint to your program.
Every module or package it relies on has to be imported at the beginning.
The code that is actually executed is the one below 'if __name__ ...' (if run
as script).
"""

if __name__ == "__main__":
    # run example function
    hello_world_success = hello_world()
    print("Hello World completed successfully!") if hello_world_success else print(
        "Hello Wold failed!"
    )

    # exemplify how to access environment variables
    print("\nEnvironment variable: {}".format(os.environ["TEST_PW"]))
    print("In production never print password to console! :)\n")
