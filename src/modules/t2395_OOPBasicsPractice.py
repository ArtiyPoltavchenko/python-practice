# OOP Pracitce


class Note:
    def __init__(self, title, content):
        self.content = content
        self.title = title
        print(f"Note '{self.title}' is created")

    def getContent(self):
        return self.content

    def getTitle(self):
        return self.title

    def printContentByLine(self, range_1=None, range_2=None):
        container = []
        for word in self.content.split():
            container.append(word)

        if range_1 or range_2:
            print(" ".join(container[range_1:range_2]))
        else:
            print(" ".join(container))


note = Note("Story", "A Long Enaught Story")
note.printContentByLine()
note.printContentByLine(1, 3)
