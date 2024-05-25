
class TooTiny(Exception):
    pass

class TooYoung(Exception):
    pass

class TooOld(Exception):
    pass

age = 15

try:
    if age < 7:
        raise TooTiny
    elif age < 18:
        raise TooYoung
    elif age > 100:
        raise TooOld
    else:
        print("You cast your valuable vote....")
except TooTiny:
    print("Too very young to cast the vote....")
except TooYoung:
    print("Too young to cast the vote.....")
except TooOld:
    print("Too Old to cast the vote...")
finally:
    print("Completed the process of voting.....")
