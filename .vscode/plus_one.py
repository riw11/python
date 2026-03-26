def plus(digits):
    digits[-1] += 1
    for i in range(len(digits) - 1,-1,-1):
        if digits[0] > 9:
            digits[0] = 0
            digits.insert(0, 1)
        elif digits[i] > 9:
            digits[i] = 0
            digits[i - 1] += 1
    return digits
digits = [9, 9, 9, 9, 9]
hasil = plus(digits)
print(hasil)