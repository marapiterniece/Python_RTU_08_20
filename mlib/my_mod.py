txt = "Quick brown fox"
mlist = [1, 2, 3, 9]

# TODO move add to my utilities module


def add(a, b):
    print(f"adding {a=} and {b=}")
    return a+b

# best to keep Classes in separate module
# big class could have its own file with name such as klase.py


class Klase:
    pass


class Garage:
    def __init__(self, gname="La biblioteca"):
        self.gname = gname
        print(f"Garage initialized! {self.gname=}")


# this will also on import
# print("Running my_mod")

# this will only run when not imported
if __name__ == "__main__":
    # typically you would put tests here
    assert(add(2, 3) == 5)
    print("This will run when my_mod.py is called normally")
    my_gar = Garage()
