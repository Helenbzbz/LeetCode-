# We keep a record on rows and cols and if we have a player1 we add 1 or we will -1 if we get -3 or 3 this marks a win

class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.horiz = [0]*n
        self.vert = [0]*n
        self.diag1 = 0
        self.diag2 = 0

    def move(self, row: int, col: int, player: int) -> int:
        n=self.n
        move = 1
        if player == 2:
            move = -1
        self.horiz[col]+= move
        self.vert[row]+= move
        
        if row == col:
            self.diag1 += move
        if row+col == (n-1):
            self.diag2 += move
            
        if abs(self.horiz[col]) == n or abs(self.vert[row]) == n or abs(self. diag1)==n or abs(self.diag2)==n:
            return player
        return 0
        
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
