from typing import List
import os


def check(operator_names: str) -> List[str]:
    """Function to check missing images for operators

    Args:
        operator_names (str): operator names list from BE api response

    Returns:
        List[str]: will return missing operator images name
    """
    IMG_DIR = os.getenv("IMAGES_DIR")
    img_files = []

    missing = []

    for file in os.listdir(IMG_DIR):
        img_files.append(os.path.splitext(file)[0])

    for name in operator_names:
        if name not in img_files:
            missing.append(name)

    return missing
