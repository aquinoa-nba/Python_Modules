#!/usr/bin/env python3

class Intern:
    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.Name = name

    def __str__(self):
        return self.Name

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return self.Coffee()


if __name__ == '__main__':
    person1 = Intern()
    person2 = Intern('Mark')
    print(person1)
    print(person2)
    print(person2.make_coffee())
    try:
        person1.work()
    except Exception as exc:
        print(exc)
