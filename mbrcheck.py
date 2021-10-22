def mbrcheck(binary):
    if hex(binary[510]) == '0x55' and hex(binary[511]) == '0xaa':
        return True
    else:
        return False