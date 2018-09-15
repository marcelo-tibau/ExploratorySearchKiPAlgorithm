#Exploratory Search KiP Algorithm
  
class NoChoicesLeft(Error): pass

def choose(*choices):
    for choice in choices:
        try:
            return choice()
        except NoChoicesLeft:
            continue

