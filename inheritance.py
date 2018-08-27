class Animal:
    def talk(self):print('i have somthing to say')
    def walk(self):print('hi i am walking here')
    def clothes(self):print('i have nice clothes')
class Duck(Animal):
    def quack(self):
        print('quack')
    def walk(self):
        super().walk()
        print('walk like a duck')
class Dog(Animal):
    def clothes(self):
        print('i have brown fur')
def main():
    donald=Duck()
    donald.quack()
    donald.walk()
    donald.clothes()
    fido=Dog()
    fido.walk()
    fido.clothes()
main()
