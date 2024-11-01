# minimax.py
import math

class Minimax:
    def __init__(self):
        pass

    def minimax(self, curDepth, nodeIndex, maxTurn, scores, targetDepth):
        # Base case: if the target depth is reached, return the value of the current node (leaf node)
        if curDepth == targetDepth:
            return scores[nodeIndex]

        # If it's maximizer's turn, choose the maximum of the two child nodes
        if maxTurn:
            return max(self.minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
                       self.minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))

        # If it's minimizer's turn, choose the minimum of the two child nodes
        else:
            return min(self.minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
                       self.minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))
    