def caesar(offset, input_str):
    result = ""

    for char in input_str:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            position = ord(char) - base
            new_position = (position + offset) % 26
            result += chr(base + new_position)
        else:
            result += char

    return result

if __name__ == '__main__':
    print(caesar(3, "abc")) # def
    print(caesar(2, "alta")) # cnvc
    print(caesar(10, "alterraacademy")) # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz")) # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) # mnopqrstuvwxyzabcdefghijkl