class Duck:
    def __init__(self,color='white'):
        self._color=color
        print('constructor')
    def quack(self):
        print('quaaaccckkk')
    def walk(self):
        return self._color
    def setcolor(self,color):
        self._color=color

def main():
    donald=Duck('yellow')
    frank=Duck()
    print(donald)
    donald.quack()
    donald.walk()
    frank.walk()
    print(donald.get_color())
    donald.setcolor('pink')
    print(donald.get_color())
    print(frank.get_color())
main()
