def find_mft(binary):
    return int.from_bytes(binary[48:56], byteorder='little'), int.from_bytes(binary[56:64], byteorder='little')