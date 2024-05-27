import string
def print_rangoli(size):
   alphabets = string.ascii_lowercase
   lines = []
   for i in range(size):
        pattern = '-'.join(alphabets[size - 1:i:-1] + alphabets[i:size])
        lines.append((pattern).center(4 * size - 3, '-'))
   for line in reversed(lines):
        print(line)
if __name__ == '__main__':

    N = int(input().strip())


    print_rangoli(N)