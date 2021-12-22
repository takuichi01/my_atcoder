import bisect


N, Q = (int(x) for x in input().split())

A = list(map(int, input().split()))
A.sort()

x = [ int(input()) for _ in range(Q) ]

for i in range(Q):
    if x[i] <= A[N-1]:
        print(N-bisect.bisect_left(A, x[i]))
    else:
        print(0)


