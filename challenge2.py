#challeng2.2

class player:
  def play(self):
    print("the player is playing cricket.")

class batsman(player):
  def play(self):
    print("the batsman is batting.")

class bowler(player):
  def play(self):
    print("the bowler is bowling.")

Batsman = batsman()
Bowler = bowler()

Batsman.play()
Bowler.play()