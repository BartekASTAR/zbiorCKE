def dec2bin(decimal):
    if decimal == 0:
        return "0"
    binary = ""
    while decimal > 0:
        r = decimal % 2
        binary = str(r) + binary
        decimal = decimal//2
    return binary
