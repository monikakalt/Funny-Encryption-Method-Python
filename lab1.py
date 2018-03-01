from itertools import islice


class FunnyEncryptionMethod:
    def __init__(self, number):
        self.number = number
        self.X1 = 0
        self.X2 = 0
        self.B1 = 0
        self.B2 = 0
        self.__x = 99
        self._x = 99
    def calc(self):
        self.X1 = FunnyEncryptionMethod(self.number).convert_to_binary()
        self.B1 = FunnyEncryptionMethod(self.B1).count_ones(self.X1)
        self.X2 = FunnyEncryptionMethod(self.number).convert_from_hex()
        self.B2 = FunnyEncryptionMethod(self.B2).count_ones(self.X2)
        try:
            f = open("results.txt", "a")
            f.write(str(self.B1) + ' ' + str(self.B2) + "\n")
            f.close
        except Exception:
            print("Could not save the file")

    # converts from decimal to binary
    def convert_to_binary(self):
        x1 = f'{int(self.number):08b}'
        return x1

    # convert from hex to binary
    def convert_from_hex(self):
        integer = int(self.number, 16)
        spec = '{fill}{align}{width}{type}'.format(fill='0', align='>', width=42, type='b')
        x2 = format(integer, spec)
        return x2

    # calculates b1 and b2
    def count_ones(self, a):
        ones = 0
        for i in a:
            if int(i) == 1:
                ones += 1
        return ones


class Child(FunnyEncryptionMethod):
    def __init__(self, number, letter):
        self.__x = 2
        self._x = 2
        FunnyEncryptionMethod.__init__(self, number)
        self.letter = letter


numbers = []

c = Child(42,'l');
#f = FunnyEncryptionMethod(5)
print(c._FunnyEncryptionMethod__x);
print(c._Child__x);
with open('lab1.txt', 'r') as fin:
    for N in islice(fin, 1, None):
        numbers.append(N)


def main(numbers):
    for num in numbers:
        n = FunnyEncryptionMethod(num)
        n.calc()


main(numbers)
