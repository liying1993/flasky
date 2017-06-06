class Word(str):
    def __eq__(self, other):
        return len(self) == len(other)

class Apple(object):
    def __init__(self,name,size):
        self.name = name
        self.size = size
    def __getattr__(self, name):
        return self.name

    def __setattr__(self, name, value):
        self.__dict__[name]= 'apple-{}'.format(value)

if __name__ == "__main__":
    w1 = Word('asd')
    w2 = Word('xxx')
    print('{}=={}?{}'.format(w1,w2,w1==w2))
