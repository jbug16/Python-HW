class Counter:
    def __init__(self):
        self._strokes = ""

    def getValue(self):
        return self._strokes

    def click(self):
        if len(self._strokes) > self._limit:
            print("Limit Exceeded")
        else:
            self._strokes += '|'

    def reset(self):
        self._strokes = ""
    
    def setLimit(self, maximum):
        self._limit = maximum