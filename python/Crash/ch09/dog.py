class Dog:
    """Models a pet dog"""
    def __init__(self, name):
        """
        Creates a new dog.
        :param name: Name of dog.
        """
        self.name = name
        self.age = 0

    def add_years(self, years=1):
        if years >= 0:
            self.age += years
        else:
            print("Cannot go back in time!")

    def show(self):
        """Introduces the dog"""
        print(f"{self.name} is {self.age} year(s) old")

    def sit(self):
        """Simulate sitting"""
        print(f"{self.name} is sitting")

    def rollover(self):
        """Simulate rolling over"""
        if self.age < 10:
            print(f"{self.name} is rolling over")
        else:
            print(f"{self.name} is too old to roll over")


if __name__ == "__main__":
    ruca = Dog("Ruca")
    ruca.add_years(9)
    ruca.show()
    ruca.sit()
    ruca.rollover()

    ruca.add_years()
    ruca.show()
    ruca.sit()
    ruca.rollover()

    ruca.add_years(-1)
    ruca.show()
