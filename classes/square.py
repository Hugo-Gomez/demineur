class Square:

    def __init__(self):
        self.value = "."
        self.content = 0

    def increment_content(self):
        if not self.content == "B":
            self.content += 1

    def set_bomb(self):
        self.content = "B"

    def is_bomb(self):
        return self.content == "B"

    def dig(self):
        self.value = self.content

    def mark(self):
        if self.value == "@":
            self.value = "."
        else:
            self.value = "@"
