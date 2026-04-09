binary = int(input())

def bin2dec(binary):
    decimal = 0
    power = 0
    while binary > 0:
        digit = binary % 10
        decimal += digit*(2**power)
        binary //= 10
        power+=1
    return decimal

print(bin2dec(binary))