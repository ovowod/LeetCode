class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted([[positions[i], healths[i], directions[i], i] for i in range(len(positions))])
        arr = []
        
        for p, h, d, i in robots:
            if d == "R":
                arr.append([p, h, d, i])

            else:
                while arr and arr[-1][2] == "R" and h > 0:
                    if arr[-1][1] < h:
                        arr.pop()
                        h -= 1
                    elif arr[-1][1] > h:
                        arr[-1][1] -= 1
                        h = 0
                    else:
                        arr.pop()
                        h = 0
                if h > 0:
                    arr.append([p, h, d, i])
        
        return [i for _, i, _, _ in sorted(arr, key=lambda x: x[-1])]