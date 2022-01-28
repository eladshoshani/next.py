# exercise 5.4
# by: Elad Shoshani
# 24.04.2020


class IdLengthError(Exception):
    """
    A class used to represent an error which says that an ID number is not in the appropriate length.
    """

    def __init__(self, arg):
        """
        Creating and initializing class type variable.
        :param arg: The argument that caused the error
        :type: int
        """
        self._arg = arg

    def __str__(self):
        """Returns a String that describes the error.
        When the exception is thrown, the string returned from the method is printed to the screen.
        :return: A String that describes the error
        :rtype: str
        """
        return "Provided argument %d is not with 9 digits." % self._arg

    def get_arg(self):
        """Returns the variable attribute (Which should not be accessed directly outside the class).
        :return: The variable attribute
        :rtype: int
        """
        return self._arg


def check_id_valid(id_number):
    """
    function that check if an id_number is valid
    :param id_number: The number checked for being a valid ID Number
    :type: int
    :return: True if id_number is a valid ID Number and False otherwise
    :rtype: bool
    :raise: ValueError: If the entered parameter is not an integer
    :raise: IdLengthError: if the entered integer is not with 9 digits
    """

    # check for possibles errors:
    if not isinstance(id_number, int):  # not a number
        raise ValueError('An integer must be entered')
    if len(str(id_number)) != 9:  # not 9 digits
        raise IdLengthError(id_number)  # raising the error and print an appropriate message

    # Calculate the sum after the change in even and odd indexes separately:
    sum_of_new_id_number = sum([int(x) for x in str(id_number)[::2]])
    sum_of_new_id_number += sum([(2 * int(x)) % 9 for x in str(id_number)[1::2]])
    return sum_of_new_id_number % 10 == 0  # returns True if the sum is divided by 10


class IDIterator:
    """
    A class for creating iterators that create valid ID numbers
    """

    def __init__(self, id_number):
        """
        Creating and initializing class type variable
        :param id_number: Id number to initialize the _id attribute
        :type: int
        """
        self._id = id_number  # initializing the _id attribute

    def __iter__(self):
        """ returns the object that triggered the method (he's an iterator - Iterator Protocol)
        Iterator Protocol
        :return: The object that triggered the method
        :rtype: IDIterator
        """
        return self

    def __next__(self):
        """ Returns the next valid ID number and updates _id to it.
        :return: The next valid ID number each time in the range between _id (inclusive) and 999999999.
        :rtype: int
        :raise: StopIteration: If we passed 999999999 in search for the next valid id number.
        """
        for i in range(self._id + 1, 999999999 + 1):
            if check_id_valid(i):
                self._id = i
                return self._id

        # Raise StopIteration exception (because the are not any more valid ID numbers in the range):
        raise StopIteration()


def id_generator(id_number):
    """
    creating iterators that create valid ID numbers
    :param id_number: The number to generate from the id_numbers
    :type: int
    :return: a generator that creates valid ID numbers
    :rtype: generator
    """
    for i in range(id_number, 999999999 + 1):
        if check_id_valid(i):
            yield i  # returning the valid id_number


def main():
    """
    The main function that demonstrates the operation of the IDIterator class and the id_generator function.
    """
    id_iter = IDIterator(123456780)  # creating an iterator and in
    for i in range(10):  # print 10 times (using the iterator)
        print(next(id_iter))

    print("\nnow with the generator:\n")

    id_gen = id_generator(123456780)
    for i in range(10):  # print 10 times (using the generator)
        print(next(id_gen))


if __name__ == '__main__':
    main()
