from collections import defaultdict

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        matching = {"L":"R", "D":"U"}
        movement = defaultdict(int)
        
        for move in moves:
            if move in ["R", "U"]:
                movement[move] += 1
            else:
                movement[matching[move]] -= 1

        return False if movement['R'] or movement['U'] else True