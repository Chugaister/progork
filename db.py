from models import *


class Database:

    def __init__(self, source: str):
        self.__source = source
        self.__items = []
        self.load()

    def load(self):
        self.__items = []
        with open(self.__source, "r") as file:
            for line in file:
                self.__items.append(Worker.deserialize(line))

    def save(self):
        with open(self.__source, "w") as file:
            for item in self.__items:
                file.write(item.serialize() + "\n")

    def get_all(self):
        return self.__items

    def insert(self, item: Worker):
        item.id = max(item.id for item in self.__items) + 1
        self.__items.append(item)

    def delete(self, id_: int):
        for item in self.__items:
            if item.id == id_:
                self.__items.remove(item)
                return

    def get_file_content(self):
        content = ""
        for item in self.__items:
            content += item.serialize() + "\n"
        return content

