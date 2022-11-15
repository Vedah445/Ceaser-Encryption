input = input("enter msg: ")

encoded_msg = [chr(ord(c) + 3) for c in input]

print("".join(encoded_msg))