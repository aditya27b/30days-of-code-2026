def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def g(x, y):
            while y:
                x, y = y, x % y
            return x

        def l(x, y):
            return (x * y) // g(x, y)

        ab, bc, ac = l(a, b), l(b, c), l(a, c)
        abc = l(a, bc)

        lo, hi = 1, min(a, b, c) * n

        while lo < hi:
            m = (lo + hi) // 2
            cnt = (m // a) + (m // b) + (m // c) - (m // ab) - (m // bc) - (m // ac) + (m // abc)
            
            if cnt < n:
                lo = m + 1
            else:
                hi = m
        
        return lo