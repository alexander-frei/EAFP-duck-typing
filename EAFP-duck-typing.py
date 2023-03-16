#----------------------------------------
#  Corey Scheafer: EAFP and duck-typing:
#  https://www.youtube.com/watch?v=x3v9zMX1s4s
#----------------------------------------


#------------------------------
#  Own example: stopwatch => laptime
#------------------------------
class stopwatch:
    def __init__(self,start=None,end=None):
        self.start= start
        self.end = end
    def laptime(self):
        try:
            return self.end-self.start
        except TypeError:
            return "Stopwatch still running."


#--------------------
#  Example participants:
#--------------------
Alice = stopwatch(0,120)
Bob = stopwatch(30)

print("Alice laptime:",Alice.laptime())
print("Bob laptime:",Bob.laptime())