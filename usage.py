from db import Database
from models import Worker


def test1():
    print("test1")
    db = Database("data.txt")
    workers = db.get_all()
    print(workers)
    print("**FILE**\n", db.get_file_content(), "**FILE**\n\n")


def test2():
    print("test2")
    db = Database("data.txt")
    db.insert(Worker(id_=80, name="Oleh", salary=1000))
    print("**FILE**\n", db.get_file_content(), "**FILE**\n\n")


def test3():
    print("test3")
    db = Database("data.txt")
    db.delete(2)
    print("**FILE**\n", db.get_file_content(), "**FILE**\n\n")


def test4():
    print("test4")
    db = Database("data.txt")
    first = db.get_all()[0]
    first.name = "Noname"
    print("**FILE**\n", db.get_file_content(), "**FILE**\n\n")


def test5():
    print("test5")
    db = Database("data.txt")
    print(db.sort_by("salary"))


def main():
    test1()
    test2()
    test3()
    test4()
    test5()


if __name__ == "__main__":
    main()
