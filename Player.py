import random
import time
import copy
import operator

class Player:

  def __init__(self, board, mark, strategy = 'random'):
    self.board = board
    self.strategy = strategy
    self.mark = mark
    self.oppMark = 'o' if mark == 'x' else 'x'

  def move(self):
    if self.strategy == 'mc':
      return self.mcMove()
    elif self.strategy == 'random':
      return self.randomMove()

  def randomMove(self):
    legalMoves = self.board.legalMoves()
    if len(legalMoves) > 0:
      return random.choice(legalMoves)
    else:
      return 0

  def mcMove(self):
    legalMoves = self.board.legalMoves()

    scores = {}
    for move in legalMoves:
      scores[str(move)] = 0

    start = int(round(time.time() * 1000))
    while True:
      for move in legalMoves:
        boardCopy = copy.deepcopy(self.board)
        res = boardCopy.playerAction(self.mark, move)
        if res == 1:
          return move
        elif res == -1:
          scores[str(move)] = -100
          legalMoves.remove(move)
        else:
          scores[str(move)] += self.treeSearch(boardCopy)
        if int(round(time.time() * 1000)) - start > 98:
          break

    return int(max(scores.items(), key=operator.itemgetter(1))[0])

  def treeSearch(self, board, iterations = 4):
    legalMoves = board.legalMoves()
    # Opponent Moves
    res = board.playerAction(self.oppMark, random.choice(legalMoves))
    if res == 1:
      return -1
    if res == -1:
      return 100
    
    legalMoves = board.legalMoves()
    res = board.playerAction(self.mark, random.choice(legalMoves))
    if res == 1:
      return 100
    if res == -1:
      return -1
    
    if iterations > 0:
      iterations -= 1
      return self.treeSearch(board, iterations)
    else:
      return board.valuePosition(self.mark, self.oppMark)
    
