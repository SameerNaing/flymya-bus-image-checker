import os
import subprocess


def pull():
    """Function to pull update from git"""

    subprocess.run(["git", "pull"])


def checkout_master():
    """Function to checkout to master"""

    subprocess.run(["git", "checkout", "master"])
