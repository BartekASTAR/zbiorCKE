import string
def dec2base(decimal, base):
    if decimal == 0:
        return "0"
    number = ""
    digits = [str(i) for i in range(10)] + [letter for letter in string.ascii_uppercase]
    while decimal > 0:
        r = decimal % base
        number = digits[r] + number
        decimal = decimal//base
    return number

print(dec2base(13,16))