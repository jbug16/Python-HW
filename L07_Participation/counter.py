class Counter:
    def __init__(self):
        self._value = 0

    def getValue(self):
        return self._value

    def click(self):
        if self._value > self._limit :
            print("Limit Exceeded")
        else:
            self._value = self._value + 1

    def reset(self):
        self._value = 0
    
    def setLimit(self, maximum):
        self._limit = maximum