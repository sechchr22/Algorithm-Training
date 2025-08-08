"""
Writte the fibonacci series till 8
    0, 1, 1, 2, 3, 5, 8
"""

def fibonacci_series(series: int) -> list:
    fib = [0, 1]
    for i in range(1, series + 1):
        fib.append(fib[i-1] + fib[i])
    return fib

if __name__ == "__main__":
    print(fibonacci_series(5))