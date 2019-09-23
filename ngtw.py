
binary = [0] * 8

binary2 = [1, 0, 0, 0, 0, 1, 0, 1]

res = int("".join(str(x) for x in binary2), 2)

print("Binary Number Opcode", bin(res >> 5), "\n")

res2 = map(int, list(bin((1 << 8) + res))[-8:])

print("Back to Decimal", *res2)


