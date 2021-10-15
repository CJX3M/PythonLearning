from os import system, name

class clearNotSupported(Exception):
  print('Clear not supoprted')

def clear():
  try:
      if name == 'nt':
          _ = system('cls')
      elif name == 'posix':
          _ = system('clear')
  except:
    raise clearNotSupported()


class Participant:
    def __init__(self, name) -> None:
        self.name = name
        self.points = 0
        self.choice = ""
        self.switcher = {
            "rocks": 0,
            "paper": 1,
            "scissors": 2,
            "lizard": 3,
            "spock": 4
        }
    def choose(self):
        self.choice = ''
        while self.choice.lower() not in self.switcher.keys():
            self.choice = input(f"{self.name} choice ({'|'.join(self.switcher.keys())}): ")

    def toNumericalChoice(self):
        return self.switcher[self.choice]

    def increaseScore(self):
        self.points += 1

class GameRound:
    def __init__(self, participant1, participant2) -> None:
        self.rules = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [-1, 1, 1, -1, 0]
        ]
        participant1.choose()
        clear()
        participant2.choose()
        result = self.compareChoices(participant1, participant2)
        winner = ''
        if result == -1:
            winner = participant2.name
            participant2.increaseScore()
        elif result == 1:
            winner = participant1.name
            participant1.increaseScore()

        print(f"{winner} wins this round")

    def compareChoices(self, player1, player2):
        return self.rules[player1.toNumericalChoice()][player2.toNumericalChoice()]
    def getResult(self, result):
        res = {
            0: 'draw',
            1: 'win',
            -1: "loss"
        }
        return res[result]
        

        
class Game:
    def __init__(self) -> None:
        self.endGame = False
        self.participant = Participant('Player 1')
        self.secondParticipant = Participant('Player 2')
        self.maxPoints = ''
        self.winner = ''
    def newRound(self):
        GameRound(self.participant, self.secondParticipant)        
        if self.participant.points == self.maxPoints:
            self.endGame = True
            self.winner = 'Player 1'
        elif self.secondParticipant.points == self.maxPoints:
            self.endGame = True
            self.winner = 'Player 2'
        else: 
            print(f'Current Score: \n Player 1: {self.participant.points}\n Player 2: {self.secondParticipant.points}')
            if self.participant.points > self.secondParticipant.points:
                print('Player 1 its winning')
            elif self.participant.points == self.secondParticipant.points:
                print('Game its even')
            else:
                print('Player 2 its winning')
            self.participant.choice = ''
            self.secondParticipant.choice = ''
            input('Press enter for the next round')
    def playGame(self):
        while not self.maxPoints.isnumeric():
            self.maxPoints = input('Please set the ammount of points to win: ')
        self.maxPoints = int(self.maxPoints)
        while not self.endGame:
            self.newRound()
        input(f'{self.winner} its the winner!')

game = Game()
game.playGame()
        
