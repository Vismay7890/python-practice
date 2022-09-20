# Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
import random
tick = []
print("Generating 1000 random numbers:")
for i in range(0,1000):
    tick.append(random.randrange(1000000000,9999999999))
win = random.sample(tick,2)
print("Lucky winners are : ",win)