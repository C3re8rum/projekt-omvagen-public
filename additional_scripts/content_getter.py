import requests
import os

from zipfile import ZipFile
import shutil

def setup_folder():
    files = os.listdir("content")

    for f in files:
        path = f"content/{f}"

        if f == 'index.md':
            continue

        if (os.path.isdir(path)):
            shutil.rmtree(path)
            continue
        os.remove(path)

def download_data():
    url = "https://github.com/C3re8rum/ProjektOmvagen/archive/refs/tags/v0.1.0-alpha.zip"
    query_parameters = {"downloadformat": "zip"}

    response = requests.get(url, params=query_parameters)
    return response

def save_data(response):
    with open("content/data.zip", "wb") as data:
        data.write(response.content)
def unzip():
    with ZipFile("content/data.zip", 'r') as zObject:
        zObject.extractall("content")

def move_files():
    source = "content/ProjektOmvagen-Public"
    destination = "content"

    allFiles = os.listdir(source)
    for f in allFiles:
        src_path = os.path.join(source, f)
        dst_path = os.path.join(destination, f)
        shutil.move(src_path, dst_path)
def cleanup():
    shutil.rmtree("content/ProjektOmvagen-Public")
    os.remove("content/data.zip")

def main():
    setup_folder()
    data = download_data()
    save_data(data)
    unzip()
    move_files()
    cleanup()


if __name__ == '__main__':
    main()