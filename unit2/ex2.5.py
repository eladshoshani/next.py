# exercise 2.5
# by: Elad Shoshani
# 25.04.2020


class Animal:
    """A class that represents an animal in our zoo"""
    zoo_name = "Hayaton"  # Class attribute - the Zoo name

    def __init__(self, name, hunger=0):
        """
        Creating and initializing class type variable (Animal)
        :param name: The name of the animal
        :param hunger: The amount of hunger of the animal (Default - 0)
        :type name: str
        :type hunger: int
        """
        self._name = name
        self._hunger = hunger

    def get_name(self):
        """
        gets the _name attribute
        :return: The name of the animal
        :rtype: str
        """
        return self._name

    def is_hungry(self):
        """
        Checks whether the animal (self) is hungry (if _hunger is bigger than 0)
        :return: True if the animal is hungry
        :rtype: bool
        """
        return self._hunger > 0

    def feed(self):
        """
        Reduces the hunger by 1.
        :return: None
        """
        self._hunger -= 1

    def talk(self):
        """A method that prints the sound the animal makes (each animal and its sound)"""
        self.talk()


class Dog(Animal):
    """
    A class that represents a dog type animal
    """

    def talk(self):
        """prints the sound a dog does"""
        print('woof woof')

    def fetch_stick(self):
        """The special method for the dog type animal"""
        print('There you go, sir!')


class Cat(Animal):
    """
    A class that represents a cat type animal
    """

    def talk(self):
        """prints the sound a cat does"""
        print('meow')

    def chase_laser(self):
        """The special method for the cat type animal"""
        print('Meeeeow')


class Skunk(Animal):
    """
    A class that represents a skunk type animal
    """

    def __init__(self, name, hunger=0, stink_count=6):
        """
        Creating and initializing skunk type variable
        :param name: The name of the skunk
        :param hunger: The amount of hunger of the skunk (Default - 0)
        :param stink_count: How stinky the skunk is (Default - 6)
        :type name: str
        :type hunger: int
        :type stink_count: int
        """
        super().__init__(name, hunger)  # the name and hunger level initialization is the same as in other animals
        self._stink_count = stink_count

    def talk(self):
        """prints the sound a skunk does"""
        print('tsssss')

    def stink(self):
        """The special method for the skunk type animal"""
        print('Dear lord!')


class Unicorn(Animal):
    """
    A class that represents a unicorn type animal
    """

    def talk(self):
        """prints the sound a unicorn does"""
        print('Good day, darling')

    def sing(self):
        """The special method for the unicorn type animal"""
        print('I’m not your toy...')


class Dragon(Animal):
    """
    A class that represents a dragon type animal
    """

    def __init__(self, name, hunger=0, color="Green"):
        """
        Creating and initializing dragon type variable
        :param name: The name of the dragon
        :param hunger: The amount of hunger of the dragon (Default - 0)
        :param color: The color of the dragon (Default - "Green")
        :type name: str
        :type hunger: int
        :type color: str
        """
        super().__init__(name, hunger)  # the name and hunger level initialization is the same as other animals
        self._color = color

    def talk(self):
        """prints the sound a dragon does"""
        print('Raaaawr')

    def breath_fire(self):
        """The special method for the dragon type animal"""
        print('$@#$#@$')


def main():
    """
    The main function that demonstrates the "zoo" operation
    """
    # Create all the animal variables requested:
    zoo_lst = []
    dog = Dog('Brownie', 10)
    zoo_lst.append(dog)

    cat = Cat('Zelda', 3)
    zoo_lst.append(cat)

    skunk = Skunk('Stinky')
    zoo_lst.append(skunk)

    unicorn = Unicorn('Keith', 7)
    zoo_lst.append(unicorn)

    dragon = Dragon('Lizzy', 1450)
    zoo_lst.append(dragon)

    dog2 = Dog('Doggo', 80)
    zoo_lst.append(dog2)

    cat2 = Cat('Kitty', 80)
    zoo_lst.append(cat2)

    skunk2 = Skunk('Stinky Jr.', 80)
    zoo_lst.append(skunk2)

    unicorn2 = Unicorn('Clair', 80)
    zoo_lst.append(unicorn2)

    dragon2 = Dragon('McFly', 80)
    zoo_lst.append(dragon2)

    for animal in zoo_lst:
        if animal.is_hungry():
            # print the animal's class name and the animal name:
            print(animal.__class__.__name__, animal.get_name())
            while animal.is_hungry():  # feed the animal until it is not hungry
                animal.feed()
        animal.talk()  # let each animal talk

        # use special method:
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        else:  # animal is a Dragon
            animal.breath_fire()

    print(Animal.zoo_name)  # Print the zoo name at the end of the program


if __name__ == '__main__':
    main()
