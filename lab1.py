from itertools import islice

numbers = []

def read_file():
    try:
        with open('lab1.txt', 'r') as f:
            first_line = f.readline()
        with open('lab1.txt', 'r') as fin:
            for N in islice(fin, 1, None):
               numbers.append(N)
        f.close()
    except Exception:
        print("Could not read a file")

read_file()

def convert_to_binary(n):
    b = f'{int(n):08b}'
    return b

def count_ones(b):
    ones = 0
    for i in b:
        if int(i) == 1:
            ones += 1
    return ones

def convert_from_hex(n):
    integer = int(n,16)
    spec = '{fill}{align}{width}{type}'.format(fill='0', align='>', width=42, type='b')
    h = format(integer, spec)
    return h

def save_file(b1, b2):
    try:
        f = open("results.txt", "a")
        f.write(str(b1) + ' ' + str(b2) + "\n")
        f.close
    except Exception:
        print("Could not save the file")

def main(numbers):
    for n in numbers:
      X1 = convert_to_binary(n)
      b1 = count_ones(X1)
      X2 = convert_from_hex(n)
      b2 = count_ones(X2)
      save_file(b1, b2)

main(numbers)