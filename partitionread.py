import checkbinary


def partitionread(binary,sizeofp):

    ptguid=binary[0+sizeofp:16+sizeofp]
    unpguid=binary[16+sizeofp:32+sizeofp]
    firstlba=checkbinary.checkbinary_int(binary,32+sizeofp,40+sizeofp)
    lastlba=checkbinary.checkbinary_int(binary,40+sizeofp,48+sizeofp)
    Aflag=checkbinary.checkbinary_int(binary,48+sizeofp,56+sizeofp)
    pname=binary[56+sizeofp:128+sizeofp]

    return ptguid,unpguid,firstlba,lastlba,Aflag,pname