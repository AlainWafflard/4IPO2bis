class Observer:
    """ observateur """

    def __init__(self, observable):
        observable.subscribe(self)

    def notify( self, observable, *args, **kwargs ):
        print ('Got', args, kwargs, 'From', observable)


class Observable:
    """ sujet """

    def __init__(self):
        self.observer_l = []

    def subscribe(self, observer):
        self.observer_l.append(observer)

    def notify_observer_l(self, *args, **kwargs):
        for obs in self.observer_l:
            obs.notify(self, *args, **kwargs)

    def unsubscribe(self, observer):
        self.observer_l.remove(observer)


# observer_pattern.py

"""
Demonstrating the Observer pattern implementation
"""
# Initializing the subject
subject = Observable()

# Initializing two observers with the subject object
observer1 = Observer(subject)
observer2 = Observer(subject)

# The following message will be notified to 2 observers
subject.notify_observer_l('This is the 1st broadcast',
                         kw='From the Observer')
subject.unsubscribe(observer2)

# The following message will be notified to just 1 observer since
# the observer has been unsubscribed
subject.notify_observer_l('This is the 2nd broadcast',
                         kw='From the Observer')

