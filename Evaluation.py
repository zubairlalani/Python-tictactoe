import enum

class Evaluation(enum.Enum) :
    NoWinner = 1
    XWins = 2
    OWins =  3
    UnreachableState = 4
