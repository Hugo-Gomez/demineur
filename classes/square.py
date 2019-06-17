class Square:

    def __init__(self):
        self.value = "."
        self.content = 0

    def setContent(self, content):
        self.content = content

    def revealContent(self):
        self.value = self.content

    def setBomb(self):
        self.content = "B"

    def isBomb(self):
        return self.content == "B" 