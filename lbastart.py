def findlbs(binary):
    value=int.from_bytes(binary[454:458],byteorder='little')
    return value
