
# -----------------------------------------------------------
# Abstarct Observer Class
# -----------------------------------------------------------
class Observer:
  def getState(self):
    pass
    
  def update(self, subject):
    pass


# -----------------------------------------------------------
# Subject Class that keeps track of all the observers
# -----------------------------------------------------------
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, index):
        self._observers.remove(index)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def getState(self):
        pass
        
    def setState(self, state):
        pass