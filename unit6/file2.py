# ex6.2.5
from file1 import GreetingCard


class BirthdayCard(GreetingCard):
    def __init__(self, _sender_age=0):
        self._sender_age = _sender_age

    def greeting_msg(self):
        super().greeting_msg()
        print('Happy birthday %d' % self._sender_age)
