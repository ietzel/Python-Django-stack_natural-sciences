class Rover:
  def __init__(self, name):
    self.name = name

r1 = Rover("Driver")
r2 = Rover("Flier")
r3 = Rover("Slitherer")
r4 = Rover("Hopper")
r5 = Rover("Crawler")
r6 = Rover("6")

print(getattr(r1,'name'), ", ", getattr(r2,'name'), ", ", getattr(r3,'name'), ", ", getattr(r4,'name'), ", ", getattr(r5,'name'), ", and ", getattr(r6,'name'), " meet up for the cave exploration mission.")
print("The first one drives the other 5 to the cavity, and hoists them down.")
print("They find traces of water, and a big place for settlement.")
print("Findings reported...")
