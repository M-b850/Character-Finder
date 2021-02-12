"""
Functions are here
"""


class Search:
    def __init__(self, holychar, text):
        self.holychar = holychar
        self.text = text
        self.length = len(self.holychar)

    def Check_Char(self, counter):
        if counter == self.length:
            return True

    def Go_Char(self, counter):
        if counter <= self.length-1:
            return self.holychar[counter]

    def Find_Char(self, counter=0):
        for char in self.text:
            current_main_char = self.Go_Char(counter)
            if current_main_char == char:
                counter += 1
                if self.Check_Char(counter):
                    return True
            else:
                counter = 0
                pass
