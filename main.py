import math
from node import Node
from minimax import Minimax

class Main:
    def __init__(self):
        self.tree = []

    def build_tree(self):
        scores = [3, 5, 2, 9, 12, 5, 23, 23]
        
        treeDepth = int(math.log(len(scores), 2))
        self.tree = self.create_tree(scores, treeDepth)
        return scores, treeDepth

    def create_tree(self, scores, depth):
        tree = []
        current_level = scores.copy()

        for level in range(depth + 1):
            tree.append(current_level)
            next_level = []

            # Determine the next level values based on minimax
            for i in range(0, len(current_level), 2):
                if level % 2 == 0:  # Maximizing level
                    if i + 1 < len(current_level):
                        next_level.append(max(current_level[i], current_level[i + 1]))
                    else:
                        next_level.append(current_level[i])
                else:  # Minimizing level
                    if i + 1 < len(current_level):
                        next_level.append(min(current_level[i], current_level[i + 1]))
                    else:
                        next_level.append(current_level[i])
                        
            current_level = next_level
        
        return tree

    def print_tree(self):
        for level in self.tree:
            print("Level {}: {}".format(self.tree.index(level), level))

    def run(self):
        scores, treeDepth = self.build_tree()
        self.print_tree()  # Print the built tree
        minimax = Minimax()
        optimal_value = minimax.minimax(0, 0, True, scores, treeDepth)
        print("The optimal value is:", optimal_value)

if __name__ == "__main__":
    main = Main()
    main.run()
