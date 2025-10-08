with open("samdesk.txt") as fin:
    lines = fin.read().strip().split("\n")

n = len(lines)
m = len(lines[0])
# print(lines)
# Generate all directions
dd = []
for dx in range(-1, 2):
    for dy in range(-1, 2):
        if dx != 0 or dy != 0:
            dd.append((dx, dy))

# dd = [(-1, -1), (-1, 0), (-1, 1),
#       (0, -1),           (0, 1),
#       (1, -1), (1, 0), (1, 1)]

def has_xmas(i, j, d):
    dx, dy = d
    for k, x in enumerate("XMAS"):
        ii = i + k * dx
        jj = j + k * dy
        if not (0 <= ii < n and 0 <= jj < m):
            return 0
        if lines[ii][jj] != x:
            return 0
    return 1

# Count up every cell and every direction
ans = 0
for i in range(n):
    for j in range(m):
        for d in dd:
            ans += has_xmas(i, j, d)


print(ans)
