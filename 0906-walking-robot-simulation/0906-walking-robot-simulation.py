class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        x = y = 0
        max_dist = 0
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        d = 0
        obs = set(map(tuple, obstacles))
        
        for cmd in commands:
            if cmd == -2:
                d = (d + 3) % 4
            elif cmd == -1:
                d = (d + 1) % 4
            else:
                for _ in range(cmd):
                    nx, ny = x + dirs[d][0], y + dirs[d][1]
                    if (nx, ny) in obs:
                        break
                    x, y = nx, ny
                    max_dist = max(max_dist, x*x + y*y)
        return max_dist
