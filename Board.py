FIELDS = 81

class Board:

  def __init__(self):
    self.mainBoard = ['' for i in range(9)]
    self.smallBoards = ['' for i in range(FIELDS)]
    self.activeBoard = -1
    self.winningCombinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

  def playerAction(self, mark, pos):
    legalMoves = self.legalMoves()
    oppMark = 'o' if mark == 'x' else 'x'    
    oppMarks = [i for i in range(9) if self.mainBoard[i] == oppMark]

    if any([True for i in self.winningCombinations if len(set(i) & set(oppMarks)) == 3]):
      return -1

    if len(legalMoves) == 0:
      if self.mainBoard.count(mark) < self.mainBoard.count(oppMark):
        return -1
      else:
        return 1

    if pos not in legalMoves:
      return -1
  
    self.update(mark, pos)    
    playerMarks = [i for i in range(9) if self.mainBoard[i] == mark]
    if any([True for i in self.winningCombinations if len(set(i) & set(playerMarks)) == 3]):
      return 1
    
    if len(legalMoves) == 1:
      if self.mainBoard.count(mark) >= self.mainBoard.count(oppMark):
        return 1
      else:
        return -1
    
    return 0

  def update(self, mark, pos):
    self.smallBoards[pos] = mark
    self.activeBoard = pos % 9

    boardPos = pos // 9 * 9 
    playerMarks = [i for i in range(9) if self.smallBoards[boardPos:boardPos+9][i] == mark]

    if any([True for i in self.winningCombinations if len(set(i) & set(playerMarks)) == 3]):
      self.mainBoard[pos // 9] = mark
      
  def legalMoves(self):
    if self.activeBoard < 0 or self.mainBoard[self.activeBoard] != '':
      return [i for i in range(FIELDS) if self.smallBoards[i] == '' and self.mainBoard[i // 9] == '']
    else:
      return [i for i in range(FIELDS) if self.smallBoards[i] == '' and i // 9 == self.activeBoard]
  
  def printBoard(self):
    smallBoards = [i if i != '' else ' ' for i in self.smallBoards]
    for i in range(0, 9, 3):
      print (" | ".join(smallBoards[i*9:i*9+3]), '   ', " | ".join(smallBoards[(i+1)*9:(i+1)*9+3]), '   ', " | ".join(smallBoards[(i+2)*9:(i+2)*9+3]))
      print (" | ".join(smallBoards[i*9+3:i*9+6]), '   ', " | ".join(smallBoards[(i+1)*9+3:(i+1)*9+6]), '   ', " | ".join(smallBoards[(i+2)*9+3:(i+2)*9+6]))
      print (" | ".join(smallBoards[i*9+6:i*9+9]), '   ', " | ".join(smallBoards[(i+1)*9+6:(i+1)*9+9]), '   ', " | ".join(smallBoards[(i+2)*9+6:(i+2)*9+9]))
      print ("")