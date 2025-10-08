with open("samdesk.txt") as fin:
    lines = fin.read().strip().split("\n")

n = len(lines)
m = len(lines[0])


def has_xmas(i, j):
    if not (1 <= i < n - 1 and 1 <= j < m - 1):
        return 0
    if lines[i][j] != "A":
        return 0

    # Check both diagonals
    diag_1 = f"{lines[i-1][j-1]}{lines[i+1][j+1]}"
    diag_2 = f"{lines[i-1][j+1]}{lines[i+1][j-1]}"

    if diag_1 in ["MS", "SM"] and diag_2 in ["MS", "SM"]:
        return 1
    else: return 0

ans = 0
for i in range(n):
    for j in range(m):
        ans += has_xmas(i, j)

print(ans)

