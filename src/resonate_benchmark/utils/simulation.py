from random import random


def random_failure() -> bool:
    seed = int(random() * 1000)

    if seed % 5 == 0:
        return True
    else:
        return False
