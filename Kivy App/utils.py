class Utils:

    def __init__(self) -> None:
        self.counter = 0

    def updateOnClick(self):
        self.counter += 1
        print(self.counter)