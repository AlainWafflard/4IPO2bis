class CountDown:

    def __init__(self,  start, stop):
        self.start = start
        self.target = stop
        pass

    def __iter__(self):
        self.counter = self.start
        # self.target = 0
        return self

    def __next__(self):
        self.counter -= 1
        if self.counter <= self.target:
            raise StopIteration
        return self.counter


# initialization du CountDown à 5
o = CountDown(15, 8)
my_iter = iter(o)
# print(o)

while True:
    try:
        # iteration
        i = next(my_iter)
        print(i)
    except StopIteration:
        # quand i atteint 0
        print("Go !")
        break

