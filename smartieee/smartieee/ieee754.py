
def mulmod(result):
    if result < 1:
        return 0
    else:
        return 1


def binaryfloat_splitter(number):
    innnn = len(str(int(number)))
    result = str(number)[innnn+1:]
    return result


class IEEE754:
    def __init__(self, number, precision):
        self.number = number
        self.precision = precision

    def sign(self):
        if self.number > 0:
            return 0
        else:
            return 1

    @staticmethod
    def binary(number):
        zet = ''
        num = abs(int(number))
        while num > 0:
            zet = str(num % 2) + zet
            num = num // 2
        return zet

    def binary_float(self):
        zet = ''
        num = abs(self.number) - abs(int(self.number))
        while not num == 0 and num < 1:
            num *= 2
            zet = str(mulmod(num)) + zet
            num = abs(num) - abs(int(num))
        return str(zet)[::-1]

    def exponent_32bit(self):
        test_num = len(self.binary(self.number)) - 1
        bias32 = 127
        exponent = bias32 + test_num
        binary_exponent = self.binary(exponent)
        return binary_exponent

    def exponent_64bit(self):
        test_num = len(self.binary(self.number)) - 1
        bias64 = 1023
        exponent = bias64 + test_num
        binary_exponent = self.binary(exponent)
        return binary_exponent

    def mantissa_32bit(self):
        alles = self.binary(self.number) + self.binary_float()
        zeros = (23 - len(alles)) * '0'
        after_point = alles[slice(1, None)] + zeros
        return after_point[slice(23)]

    def mantissa_64bit(self):
        alles = self.binary(self.number) + self.binary_float()
        zeros = (53 - len(alles)) * '0'
        after_point = alles[slice(1, None)] + zeros
        return after_point[slice(52)]

    def __str__(self):
        if self.precision == 32:
            return f'{self.sign()} {self.exponent_32bit()} {self.mantissa_32bit()}'
        elif self.precision == 64:
            return f'{self.sign()} {self.exponent_64bit()} {self.mantissa_64bit()}'
        else:
            raise ValueError('Incorrect precision!')


