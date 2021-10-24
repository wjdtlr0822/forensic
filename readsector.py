

def readfile(filename,start):
    # with open(filename,'rb+') as f:
    #     string =f.readlines()
    #     print(string)
    #     print(binascii.b2a_hex(string))

    # binary=[]
    # print("filename : " ,filename)
    # with open(filename,'rb+') as f:
    #     for line in f:
    #         binary.append(binascii.b2a_hex(line))

    with open(filename,'rb+') as f:
        f.seek(start*512)
        binary=f.read(512)

    return binary