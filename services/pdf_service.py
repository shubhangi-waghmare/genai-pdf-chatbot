import os
import shutil


def save_uploaded_file(uploaded_file, data_folder="data"):
    """
    Save uploaded PDF into data folder.
    """

    os.makedirs(data_folder, exist_ok=True)

    file_path = os.path.join(data_folder, uploaded_file.name)

    with open(file_path, "wb") as f:
        shutil.copyfileobj(uploaded_file, f)

    return file_path