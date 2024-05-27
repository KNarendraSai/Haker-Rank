T = int(input().strip())
for _ in range(T):
    n_A = int(input().strip())
    A = set(map(int, input().strip().split()))
    n_B = int(input().strip())
    B = set(map(int, input().strip().split()))
    if A.issubset(B):
        print(True)
    else:
        print(False)
