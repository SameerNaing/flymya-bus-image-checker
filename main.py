import os
from dotenv import load_dotenv
import schedule
import time

from git import pull, checkout_master
from bus_operators_api.operators import get_operators
from images_check import check
from google_chat import send_message


def main():
    # Change to Front-end project dir
    REPO_DIR = os.getenv("REPO_DIR")
    os.chdir(REPO_DIR)
    checkout_master()
    pull()

    PO_CHAT_ID = os.getenv("PO_CHAT_ID")

    operator_names = get_operators()
    missing = check(operator_names)

    if len(missing) == 0:
        return

    total_missing = len(missing)
    missing = "\n".join(missing)

    message = f"""
    <users/{PO_CHAT_ID}>
    Total : `{total_missing}` missing.
    ```{missing}```"""

    # Change to current file dir
    os.chdir(os.path.dirname(__file__))
    send_message(message)


if __name__ == "__main__":
    load_dotenv()
    schedule.every(1).week.do(main)

    while True:
        schedule.run_pending()
        time.sleep(2)
