import re

class Parser(object):
    def __init__(self, fname):
        self.fname = fname
        self.fhandle = open(self.fname, 'r')

        self.regex = re.compile('([A-Za-z0-9\\\'"\\(\\)]+|[,.?!:;]+)') 
        self.buffer = []

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.fhandle.close()

    def next(self):
        while not len(self.buffer):
            next_line = self.fhandle.readline()
            if next_line == "":
                return None

            self.buffer = self.regex.findall(next_line)

        return self.buffer.pop(0)

if __name__ == '__main__':
    with Parser("test.txt") as p:
        next_word = p.next()
        while next_word != None:
            print(next_word)
            next_word = p.next()

