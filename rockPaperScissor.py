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
    def __init__(self) -> None:
        self.points = 0
        self.choice = ""

class GameRound:
    def __init__(self, participant1, participant2) -> None:
        self.player1 = participant1
        self.player2 = participant2
    def playRound(self):
        if self.player1.choice.lower() == 'rocks' and self.player2.choice.lower() == 'scissors':
            print('Player 1 wins this round')
            self.player1.points += 1
        elif self.player1.choice.lower() == 'rocks' and self.player2.choice.lower() == 'paper':
            print('Player 2 wins this round')
            self.player2.points += 1
        elif self.player1.choice.lower() == 'rocks' and self.player2.choice.lower() == 'rocks':
            print('Its a draw')
        elif self.player1.choice.lower() == 'paper' and self.player2.choice.lower() == 'rocks':
            print('Player 1 wins this round')
            self.player1.points += 1
        elif self.player1.choice.lower() == 'paper' and self.player2.choice.lower() == 'scissors':
            print('Player 2 wins this round')
            self.player2.points += 1
        elif self.player1.choice.lower() == 'paper' and self.player2.choice.lower() == 'paper':
            print('Its a draw')
        elif self.player1.choice.lower() == 'scissors' and self.player2.choice.lower() == 'paper':
            print('Player 1 wins this round')
            self.player1.points += 1
        elif self.player1.choice.lower() == 'scissors' and self.player2.choice.lower() == 'rocks':
            print('Player 2 wins this round')
            self.player2.points += 1
        elif self.player1.choice.lower() == 'scissors' and self.player2.choice.lower() == 'scissors':
            print('Its a draw')    

        
class Game:
    def __init__(self) -> None:
        self.endGame = False
        self.participant = Participant()
        self.secondParticipant = Participant()
        self.maxPoints = ''
        self.winner = ''
    def newRound(self):
        clear()
        while self.participant.choice != 'rocks' and self.participant.choice != 'paper' and self.participant.choice != 'scissors':
            self.participant.choice = input("Player 1 choice (rocks|paper|scissors): ")
        clear()
        while self.secondParticipant.choice != 'rocks' and self.secondParticipant.choice != 'paper' and self.secondParticipant.choice != 'scissors':
            self.secondParticipant.choice = input(f"\r\rPlayer 2 choice (rocks|paper|scissors): ")
        round = GameRound(self.participant, self.secondParticipant)
        round.playRound()
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
        
