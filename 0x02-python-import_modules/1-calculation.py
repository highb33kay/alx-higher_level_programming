#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

def main():
    a = 10
    b = 5

    sum_ab = add(a, b)
    print(f"{a} + {b} = {sum_ab}")

    diff_ab = sub(a, b)
    print(f"{a} - {b} = {diff_ab}")

    prod_ab = mul(a, b)
    print(f"{a} * {b} = {prod_ab}")

    quot_ab = div(a, b)
    print(f"{a} / {b} = {quot_ab}")

if __name__ == "__main__":
    main()
