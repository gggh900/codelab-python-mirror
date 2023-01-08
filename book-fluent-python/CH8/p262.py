class Bird:
    pass

class Duck(Bird):
    def quack(self):
        print('Quack')

# alert has no type hints so checked ignores it.

def alert(birdie):
    birdie.quack()

# alert_duck takes one arg of type duck.

def alert_duck(birdie: Duck)->None:
    birdie.quack()

# alert_bird takes one arg of type bird.

def alert_bird(birdie: Bird)->None:
    birdie.quack()

# Daffy is a duck so it can call quack with no issue.
# So both alert_duck, alert_bird should work.
# in case of alert, parameter is passed as birdie with no type specified.
# if object passed is a Duck, then it work.

daffy=Duck()
alert(daffy)
alert_duck(daffy)
alert_bird(daffy)

# Woody is a bird so no quack defined.
# alert runs into error because woody is bird and no
# quack() defined.

woody=Bird()
alert(woody)
alert_duck(woody)
alert_bird(woody)
