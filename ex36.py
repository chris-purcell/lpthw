from sys import exit

# Set up the initial room
def start():
  print "You stand in a room with 3 exits."
  print "You can go left or right down the corridors or open the door."
  print "Choose your fate!"
  next = raw_input("> ")

  if "left" in next:
    print "You go left."
    left_corridor()

  elif "right" in next:
    print "You go right."
    right_corridor()

  elif "door" in next:
    print "You open the door."
    first_door()

  else:
    dead("You stand there frozen until you starve.")

def left_corridor():
  print "You see another door here and the corridor ends."
  print "Do you open the door or go back?"
  next = raw_input("> ")

  if "door" in next:
    print "You open the door."
    second_door()

  elif "back" in next:
    print "You go back."
    start()

  else:
    dead("You stand around until you starve.")

def right_corridor():
  print "You see another door here and the corridor ends."
  print "Do you open the door or go back?"
  next = raw_input("> ")

  if "door" in next:
    print "You open the door."
    third_door()

  elif "back" in next:
    print "You go back."
    start()

  else:
    dead("You stand around until you are eaten by a grue.")

def first_door():
  print "This is the treasure room!"
  print "How much do you take?"
  next = raw_input("> ")
  if next.isdigit():
    how_much = int(next)
  else:
    print "You were supposed to choose a number, dorf!"
    dead("You starve due to your inability to choose.")

  if how_much < 50:
    print "You are spared for keeping your greed in check."
    exit(0)
  else:
    dead("You stare in awe at the endless wealth until you starve.")

def second_door():
  dead("Eaten.")

def third_door():
  dead("Idled.")

def dead(why):
  print why,("That sucked!")

start()
