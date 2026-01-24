import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return
    it = iter(data)
    try:
        n = int(next(it))
        d = int(next(it))
        p = sorted([int(next(it)) for _ in range(n)])
    except StopIteration: return

    l, r, w = 0, n - 1, 0
    while l <= r:
        sz = (d // p[r]) + 1
        if r - l + 1 >= sz:
            w += 1
            r -= 1
            l += sz - 1
        else:
            break
    print(w)

if __name__ == "__main__":
    solve()