import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    n = int(data[0])
    k = int(data[1])
    
    a = list(map(int, data[2:]))
    
    current_sum = sum(a[:k])
    total_window_sum = current_sum
    
    for i in range(n - k):
        current_sum = current_sum - a[i] + a[i+k]
        total_window_sum += current_sum
        
    result = total_window_sum / (n - k + 1)
    print(f"{result:.10f}")

if __name__ == "__main__":
    solve()
  
