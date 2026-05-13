import os
from aiogram.types import FSInputFile, InputMediaPhoto


# ---------- STYLE IMAGES ----------
def get_style_images(style: str):

    folder_map = {
        "casual": "images/casual",
        "классика": "images/classic",
        "sports chic": "images/sports chic",
        "вечерний": "images/evening"
    }

    folder = folder_map.get(style.lower())

    media = []

    if folder and os.path.exists(folder):

        for image_name in os.listdir(folder):

            image_path = f"{folder}/{image_name}"

            media.append(
                InputMediaPhoto(
                    media=FSInputFile(image_path)
                )
            )

    else:

        media.append(
            InputMediaPhoto(
                media=FSInputFile("images/color_sets/soon.jpg")
            )
        )

    return media


# ---------- COLOR COMBINATIONS ----------
def get_color_images(first: str, second: str, third: str):

    folder_name = f"{first}_{second}_{third}"
    folder_path = f"images/color_sets/{folder_name}"

    media = []

    if os.path.exists(folder_path):

        for image_name in os.listdir(folder_path):

            image_path = f"{folder_path}/{image_name}"

            media.append(
                InputMediaPhoto(
                    media=FSInputFile(image_path)
                )
            )

    else:

        media.append(
            InputMediaPhoto(
                media=FSInputFile("images/color_sets/soon.jpg")
            )
        )

    return media