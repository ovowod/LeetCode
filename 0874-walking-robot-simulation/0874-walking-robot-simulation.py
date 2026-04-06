class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y, ans = 0, 0, 0
        cur = "North"
        obst_set = {tuple(o) for o in obstacles}

        for c in commands:
            if c == -1:
                if cur == "North": cur = "East"
                elif cur == "East": cur = "South"
                elif cur == "South": cur = "West"
                elif cur == "West": cur = "North"
            elif c == -2:
                if cur == "North": cur = "West"
                elif cur == "West": cur = "South"
                elif cur == "South": cur = "East"
                elif cur == "East": cur = "North"
            else:
                for _ in range(c):
                    nx, ny = x, y
                    if cur == "North": ny += 1
                    elif cur == "East": nx += 1
                    elif cur == "South": ny -= 1
                    else: nx -= 1

                    if (nx, ny) in obst_set:
                        break

                    x, y = nx, ny
                    ans = max(ans, x*x + y*y)

        return ans