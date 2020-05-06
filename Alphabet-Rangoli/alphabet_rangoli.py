# Display an alphabet rangoli of size n

def get_chars(n, i):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    str_slice = alphabet[i:n]
    return str_slice[::-1] + str_slice[1:]

def create_line(n, i=0):
    rows = (n*2)-1
    columns = (rows*2)-1
    chars = get_chars(n, i)
    inner_part = '-'.join(chars)
    dashes = int((columns - len(inner_part))/2)
    outer_part = '-' * dashes
    return outer_part + inner_part + outer_part

def create_rangoli(n):
    rangoli = []
    for i in range(0,n):
        full_line = create_line(n, i)
        rangoli.append(full_line)
    return rangoli[::-1] + rangoli[1:]

def print_rangoli(size):
    for row in create_rangoli(size):
        print(str(row))

if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
