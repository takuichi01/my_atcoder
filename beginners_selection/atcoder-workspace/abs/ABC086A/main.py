#!/usr/bin/env python3
import sys


def solve(a: int, b: int):
    if (a*b)%2 == 0:
        print("Even")
    else:
        print("Odd")
    return


# Generated by 2.11.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    solve(a, b)

if __name__ == '__main__':
    main()