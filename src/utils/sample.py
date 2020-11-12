from typing import List

"""
Example function. Take a closer look at the following details:
- typing of arguments, return value(s)
- use self-explanatory variables, function names
- describe function in detail at the beginning
- for cleaner code it is sometimes useful to compress for loops into one line
- handle possible errors appropriately according their type
- include comments where necessary
"""


def hello_world(cities: List[str] = ["Berlin", "Paris"]) -> bool:
    """
    Hello world function.

    Arguments:
    - cities: List of cities in which 'hello world' is posted.

    Return:
    - success: Whether or not function completed successfully.
    """

    try:
        [print("Hello {}!".format(c)) for c in cities]  # for loop one-liner
        return True

    except KeyboardInterrupt:
        return False

    finally:
        pass
