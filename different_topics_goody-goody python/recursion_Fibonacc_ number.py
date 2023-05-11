N = int(input())
print(N)
def fib_rec(N, f = []):

    f = [1, 1]
    for i in range(2, N):
        f.append(f[i - 1] + f [i- 2])
    return f

print(fib_rec(N))