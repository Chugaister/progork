from __future__ import annotations


class Error(Exception):
    pass


class Worker:

    def __init__(self, id_: int, name: str, salary: int):
        self.__classname = type(self).__name__
        self.__id = None
        self.__name = None
        self.__salary = None
        self.id = id_
        self.name = name
        self.salary = salary

    def serialize(self) -> str:
        return f"{self.__classname},{self.__id},{self.__name},{self.salary}"

    @classmethod
    def deserialize(cls, string: str):
        classname, id, name, salary = string.split(",")
        return eval(f"{classname}({int(id)}, '{name}', {int(salary)})")

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise Error(f"Expected {int} for attribute id, got {type(value)}")
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Error(f"Expected {str} for attribute name, got {type(value)}")
        self.__name = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, int):
            raise Error(f"Expected {int} for attribute salary, got {type(value)}")
        self.__salary = value

    def __str__(self):
        return self.serialize()

    def __repr__(self):
        return self.serialize()


class Delivery(Worker):
    pass


class NonDelivery(Worker):
    pass
