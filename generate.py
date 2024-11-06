import os
import json

BASE_URL = "https://raw.githubusercontent.com/ajuniezeng/IconHole/main/"


def get_file_names(directory):
    file_names = []
    for entry in os.scandir(directory):
        if entry.is_file():
            file_names.append(entry.name)
    return file_names


def insert_icon(type):
    path = f"./{type}"
    data = {"name": "IconHole", "description": f"{type} icons", "icons": []}
    file_names = get_file_names(path)
    file_names.sort()
    for i in range(len(file_names)):
        data["icons"].append(
            {
                "name": file_names[i].split(".")[0],
                "url": BASE_URL + type + "/" + file_names[i],
            }
        )
    with open(f"./{type}.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    insert_icon("round")
    insert_icon("square")
    print("Update successfully!")
