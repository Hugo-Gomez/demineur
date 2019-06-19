class Square:

    def __init__(self):
        self.value = "."
        self.content = 0

    def incrContent(self):
        if not self.content == "B":
            self.content += 1

    def setBomb(self):
        self.content = "B"

    def isBomb(self):
        return self.content == "B"

    def dig(self):
        self.value = self.content