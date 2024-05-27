A = set(map(int, input().strip().split()))
N = int(input().strip())
is_strict_superset = True
for _ in range(N):
    current_set = set(map(int, input().strip().split()))
    if not (A > current_set):
        is_strict_superset = False
        break
print(is_strict_superset)
