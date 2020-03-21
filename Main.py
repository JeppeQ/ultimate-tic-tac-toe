from Board import Board
from Player import Player

if __name__ == '__main__':
  for i in range(1000):
    board = Board()
    player1 = Player(board, 'x')
    player2 = Player(board, 'o')

    while True:
      move = player1.move()
      action = board.playerAction(player1.mark, move)
      if action == -1 or action == 1:
        print ("player1", action)
        break

      move = player2.move()
      action = board.playerAction(player2.mark, move)
      if action == -1 or action == 1:
        print ("player2", action)
        break
    
      board.printBoard()
      print ('-------------------------------------')
      print ('')

