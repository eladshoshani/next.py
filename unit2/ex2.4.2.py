class BigThing:
    def __init__(self, something):
        self.thing = something

    def size(self):
        if isinstance(self.thing, int) or isinstance(self.thing, float):
            return self.thing
        return len(self.thing)


class BigCat(BigThing):

    def __init__(self, somthing, weight):
        super().__init__(somthing)
        self.weight = weight

    def size(self):
        if self.weight > 20:
            return "Very Fat"
        elif self.weight > 15:
            return "Fat"
        else:
            return "OK"


my_thing = BigThing("balloon")
print(my_thing.size())

cutie = BigCat("mitzy", 22)
print(cutie.size())
