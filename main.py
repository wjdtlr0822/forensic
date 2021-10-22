import readdrive #드라이브를 512바이트씩 읽음
import drivechoice # 드라이브선택
import mbrcheck #mbr의 마지막 부분을 확인 55aa
import lbastart # lbastart지점을 확인 후 반환 01 00 00 00
import checkbinary # start:end을 지정하면 그 부분의 binary값을 읽음
import partitionread # sector2 부분의 partition값을 읽어옴
import partition_print # partitionread에서 받은 값을 print함
import find_MFT #partition에서 찾은 vbr주소 값에서 mft,mft_mirr 주소를 찾음.
import gui
import gui2
import tkinter

if __name__ == '__main__':

    partition_num=0
    partition_guid=[]
    partition_uniqueid=[]
    partition_firstlba=[]
    partition_lastlba=[]
    partition_Aflag=[]
    partition_name=[]
    mft_address=[]
    mftmirr_address=[]


    filename=drivechoice.drivechoice()
    binary=readdrive.readfile(filename,0)

    if mbrcheck.mbrcheck(binary):
        print("mbr true")
    else:
        print("mbr false")


    #0번섹터에서 lba start - gpt 시작위치
    lbastart=lbastart.findlbs(binary)
    print("LBASTART : ",lbastart)


    #1번섹터에서 partition lba start위치 찾기
    binary = readdrive.readfile(filename, lbastart)  # 1번섹터
    plbastart=checkbinary.checkbinary_int(binary,72,80) #파티션 엔트리 lba
    sizeofp=checkbinary.checkbinary_int(binary,84,88) # 단일 파티션 항목 크기
    ptentryn=checkbinary.checkbinary_int(binary,80,84)  #파티션 엔트리 개수
    print("Partition lba : ",plbastart,"\nsize of partition table entry : ",sizeofp,"\nnumber of partition table entry : ",ptentryn)


    #2번섹터 (파티션들 있는 섹터)
    binary=readdrive.readfile(filename,plbastart)#2번섹터

    a=0

    for i in range(0,ptentryn+1):
        ptguid,unpguid,firstlba,lastlba,Aflag,pname=partitionread.partitionread(binary,a)
        if ptguid==b'':
            break
        print('\n',i + 1, '번째 파티션 입니다.')
        partition_print.partition_print(ptguid,unpguid,firstlba,lastlba,Aflag,pname)

        a=a+ptentryn
        partition_num=partition_num+1
        name=''
        for i in pname.decode('utf-8'):
            if i.isalpha():
                name=name+i

        partition_guid.append(ptguid.hex())
        partition_uniqueid.append(unpguid.hex())
        partition_firstlba.append(firstlba)
        partition_lastlba.append(lastlba)
        partition_Aflag.append(Aflag)
        partition_name.append(name)


    for i in partition_firstlba:
        binary=readdrive.readfile(filename,i) #vbr주소
        mft,mftmirr=find_MFT.find_mft(binary)
        mft_address.append(i+mft*8)
        mftmirr_address.append(i+mftmirr*8)

    # gui.gui(partition_guid,partition_uniqueid,partition_firstlba,partition_lastlba,partition_Aflag,partition_name, mft_address,mftmirr_address)
    gui2.gui(partition_guid,partition_uniqueid,partition_firstlba,partition_lastlba,partition_Aflag,partition_name, mft_address,mftmirr_address,partition_num)