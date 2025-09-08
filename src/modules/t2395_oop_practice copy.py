# OOP Pracitce


class Note:
    def __init__(self, title: str, content: str):
        """
        Stores a note and provides methods to print this note.

        Args:
        title: string
        content: string
        """

        self.content_string = content
        self._title = title
        print(f"Note '{self._title}' is created")

        @property
        def title(self):
            return self._title + self.content_string
        
        @title.setter
        def title(self, title):
            if len(title) > 10:
                raise ValueError("Fail!")
            if not isinstance(title, str):
                raise ValueError("Fail!")
            else:
                self._title = title
    

    def printContentByLine(self, range_1:int=None, range_2:int=None) -> None:
        container = self._get_container()

        if range_1 or range_2:  
            print(" ".join(container[range_1:range_2]))
        else:
            print(" ".join(container))

    def printContentByLine2(self, range_1:int, range_2:int | str, range_3:int="5", range_4:int=None) -> None:
        container = self._get_container()

        if range_1 or range_2:  
            print(" ".join(container[range_1:range_2]))
        else:
            print(" ".join(container))
    
    def _get_container(self):
        container = []
        for word in self.content_string.split():
            container.append(word)
        return container


note = Note("Story", "A Long Enaught Story")
note.printContentByLine()
note.printContentByLine(None)
note.content_string = 'new long long story'
note.printContentByLine(1, "test")
note.printContentByLine()
note.printContentByLine()