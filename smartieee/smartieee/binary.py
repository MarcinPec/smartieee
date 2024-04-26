def mulmod(result):
    if result < 1:
        return 0
    else:
        return 1


def binaryfloat_splitter(number):
    innnn = len(str(int(number)))
    result = str(number)[innnn+1:]
    return result


class DecBin:
    def __init__(self, number):
        self.number = number

    def decimal_2_binary(self):
        zet = ''
        num = abs(int(self.number))
        while num > 0:
            zet = str(num % 2) + zet
            num = num // 2
        return zet

    def decimal_2_binary_float(self):
        zet = ''
        num = abs(self.number) - abs(int(self.number))
        while not num == 0 and num < 1:
            num *= 2
            zet = str(mulmod(num)) + zet
            num = abs(num) - abs(int(num))
        return str(zet)[::-1]

    def __str__(self):
        dec = abs(self.number) - abs(int(self.number))
        if dec > 0:
            return f'{self.decimal_2_binary()}.{self.decimal_2_binary_float()}'
        elif dec == 0:
            return f'{self.decimal_2_binary()}'


class BinDec:
    def __init__(self, number):
        self.number = number

    def binary_2_decimal(self):
        decimal = 0
        decimal_str = str(int(self.number))
        lenght = len(decimal_str)
        for i in range(lenght):
            bit = int(decimal_str[lenght - 1 - i])
            decimal = decimal + bit * (2 ** i)
        return decimal

    def binary_2_decimal_float(self):
        decimal_float = 0.0
        float_part = binaryfloat_splitter(self.number)
        for i, digit in enumerate(float_part):
            decimal_float = decimal_float + int(digit) * (2 ** -(i + 1))
        return str(decimal_float)[2:]

    def __str__(self):
        dec = abs(self.number) - abs(int(self.number))
        if dec > 0:
            return f'{self.binary_2_decimal()}.{self.binary_2_decimal_float()}'
        elif dec == 0:
            return f'{self.binary_2_decimal()}'


