from Evaluation import Evaluation

class TicTacToeBoard :
    ROWS = 3
    COLUMNS = 3
    
    def __init__(self, board):
        if board == None or board == "" or len(board) != self.ROWS * self.COLUMNS :
            raise ValueError("Invalid board provided")
        
        self.board = board.lower()
        self.rows = []
        self.cols = []
        self.XTurnAmount = self._count_turn_amount('x')
        self.OTurnAmount = self._count_turn_amount('o')
    
    def evaluate(self) :
        if self._is_unreachable_state() :
            return Evaluation.UnreachableState
        
        winner = self._check_horizontal_winner()
        if winner == Evaluation.NoWinner :
            winner = self._check_vertical_winner()
            if winner == Evaluation.NoWinner :
                winner = self._check_diagonal()
                if winner == Evaluation.NoWinner :
                    winner = self._check_anti_diagonal()
                    if winner == Evaluation.NoWinner :
                        return Evaluation.NoWinner
        
        if self._is_unreachable_state_winner(winner) :
            return Evaluation.UnreachableState
        
        return winner
    
    def _check_horizontal_winner(self) :
        self.rows = self._create_row_array()
        return self._determine_row_col_winner(self.rows)
    
    def _check_vertical_winner(self) :
        self.cols = self._create_col_array()
        return self._determine_row_col_winner(self.cols)
    
    def _check_diagonal(self) :
        row_position = 0
        direction = 1
        diagonal = self._create_diagonal(row_position, direction)
        return self._determine_diagonal_winner(diagonal)
    
    def _check_anti_diagonal(self) :
        row_position = self.COLUMNS-1
        direction = -1
        anti_diagonal = self._create_diagonal(row_position, direction)
        return self._determine_diagonal_winner(anti_diagonal)
    
    def _determine_row_col_winner(self, row_or_col) :
        winner = None
        
        for curr_row_or_col in row_or_col :
            if curr_row_or_col == 'xxx' :
                if winner == None :
                    winner = Evaluation.XWins
                else : 
                    winner = Evaluation.UnreachableState
            elif curr_row_or_col == 'ooo' :
                if winner == None :
                    winner = Evaluation.OWins
                else :
                    winner = Evaluation.UnreachableState
        
        if winner == None :
            winner = Evaluation.NoWinner
        
        return winner
    
    def _determine_diagonal_winner(self, diagonal) :
        if diagonal == 'xxx' :
            return Evaluation.XWins
        elif diagonal == 'ooo' :
            return Evaluation.OWins
        
        return Evaluation.NoWinner
    
    def _create_diagonal(self, row_position, diagona_dir) :
        diagonal = ""
        
        for current_row in self.rows :
            for i in range(len(current_row)) :
                if i == row_position :
                    diagonal += str(current_row[i])
                    break
            row_position += diagona_dir
        
        return diagonal
    
    def _create_row_array(self) :
        row_array = []
        start_of_row_index = 0
        row_index = 0
        
        while start_of_row_index < len(self.board) :
            row_array.append(self.board[start_of_row_index : start_of_row_index + self.ROWS])
            row_index += 1
            start_of_row_index += self.ROWS
        
        return row_array
            
    def _create_col_array(self) :
        current_col = ""
        col_array = []
        
        for i in range(self.ROWS) :
            for j in range(len(self.board)) :
                if j % self.COLUMNS == i :
                    current_col += str(self.board[j])
            col_array.append(current_col)
            current_col = ""
        
        return col_array
    
    def _is_unreachable_state_winner(self, winner) :
        if winner == Evaluation.XWins and self.XTurnAmount != self.OTurnAmount + 1 :
            return True
        elif winner == Evaluation.OWins and self.XTurnAmount != self.OTurnAmount :
            return True
        return False
    
    def _is_unreachable_state(self) :
        if (self.XTurnAmount - self.OTurnAmount) > 1 or self.OTurnAmount > self.XTurnAmount :
            return True
        return False
        
    def _count_turn_amount(self, player) :
        turn_count = 0
        for c in self.board :
            if c == player :
              turn_count += 1
        return turn_count
        
    def get_board(self) :
        return self.board
    
    def set_board(self, board) :
        self.board = board.lower()
        self.rows = []
        self.cols = []
        self.XTurnAmount = self._count_turn_amount('x')
        self.OTurnAmount = self._count_turn_amount('o')
        
    def get_row_arr(self) :
        return self._create_row_array()
    
    def get_col_arr(self) :
        return self._create_col_array()
    
    def get_diagonal(self) :
        return self._create_diagonal(0, 1)
    
    def get_anti_diagonal(self) :
        return self._create_diagonal(self.ROWS-1, -1)


test = TicTacToeBoard("xoo-x---x")
print(test.evaluate())

board = TicTacToeBoard("---------")
board_list = ['-', '-', '-', '-', '-', '-', '-','-', '-']

isRunning = True
current_player = 'x'
while isRunning :
    print(board_list[0] + " | " + board_list[1] + " | "+board_list[2])
    print(board_list[3] + " | " + board_list[4] + " | "+board_list[5])
    print(board_list[6] + " | " + board_list[7] + " | "+board_list[8])
    print("\n")
    
    position = int(input("Press 1-9: "))
    if board_list[position-1] == '-' :
        board_list[position-1] = current_player
        current_board = ""
        current_board = current_board.join(board_list)
        board.set_board(current_board)
    
        if board.evaluate() == Evaluation.XWins :
            print("X Wins!")
            isRunning = False
        elif board.evaluate() == Evaluation.OWins :
            print("O Wins!")
            isRunning = False
        elif board.evaluate() == Evaluation.NoWinner and '-' not in current_board:
            print("NO WINNER!")
            isRunning = False
        elif board.evaluate() == Evaluation.UnreachableState :
            print("Unreachable State!")
            isRunning = False
        else :
            isRunning = True
        
        if current_player == 'x' :
            current_player = 'o'
        else :
            current_player = 'x'
    


