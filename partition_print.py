import struct

def partition_print(ptguid,unpguid,firstlba,lastlba,Aflag,pname):


    print("ptguid : ",ptguid.hex())
    print("unguid : ", unpguid.hex())
    print("firstlba : ", firstlba)
    print("lastlba : ", lastlba)
    print("Aflag : ", Aflag)
    print("pname : ",end='')
    for i in pname.decode('utf-8'):
        if i.isalpha():
            print(i,end='')
    print()