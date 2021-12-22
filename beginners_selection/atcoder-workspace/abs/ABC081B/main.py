#!/usr/bin/env python3
import sys

MOD = 2  # type: int


def solve(N: int, A: "List[int]"):
    count = 0
    flag = 0
    while True:
        for i, a in enumerate(A):
            if a%2 == 0:
                A[i] = a/2
            else:
                flag = 1
                break

        if flag == 1:
            break

        count += 1


    print(count)
    return


# Generated by 2.11.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
