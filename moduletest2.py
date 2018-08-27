import random
def main():
    x=list(range(25))
    print(x)
    random.shuffle(x)
    print(x)
    random.shuffle(x)
    print(x)
    random.shuffle(x)
    print(x)
    random.shuffle(x)
    print(x)
    
    import datetime
    now=datetime.datetime.now()
    print(now)
    print(now.year,now.month,now.day,now.hour,now.minute,now.second,now.microsecond)
main()