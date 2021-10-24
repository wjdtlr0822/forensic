import readsector #드라이브를 512바이트씩 읽음
import drivechoice # 드라이브선택
import mbrcheck #mbr의 마지막 부분을 확인 55aa
import checkbinary # start:end을 지정하면 그 부분의 binary값을 읽음
import partitionread # partition값을 읽어옴
import find_MFT #partition에서 찾은 vbr주소 값에서 mft,mft_mirr 주소를 찾음.
import gui2

if __name__ == '__main__':

    partition_num=0
    partition_guid=[]
    partition_uniqueid=[]
    vbraddress=[]
    partition_lastlba=[]
    partition_Aflag=[]
    partition_name=[]
    mft_address=[]
    mftmirr_address=[]


    filename=drivechoice.drivechoice()
    binary=readsector.readfile(filename, 0)

    if mbrcheck.mbrcheck(binary):
        print("mbr true")
    else:
        print("mbr false")

    #0번섹터에서 lba start - gpt 시작위치
    lbastart=checkbinary.checkbinary_int(binary,454,458)


    #lbastart번섹터에서 partition lba start위치 찾기
    binary = readsector.readfile(filename, lbastart)  # 1번섹터
    plbastart=checkbinary.checkbinary_int(binary,72,80) #파티션 엔트리 lba
    sizeofp=checkbinary.checkbinary_int(binary,84,88) # 단일 파티션 항목 크기
    ptentryn=checkbinary.checkbinary_int(binary,80,84)  #파티션 엔트리 개수


    #2번섹터 (파티션들 있는 섹터)
    # binary=readdrive.readfile(filename,plbastart)#2번섹터

    break_for=True #2중 for문 나가기 위해.
    sec_parnum=ptentryn/int(512/sizeofp) #한 섹터에 파티션이 몇개가 들어가는지

    for j in range(plbastart,int(sec_parnum+plbastart)):
        a = 0 #partition entry 크기만큼 더해서 다음 값을 읽음
        if break_for == False:
            break
        binary = readsector.readfile(filename, j)  # j섹터 읽기

        for i in range(0,int(512/sizeofp)):
            ptguid,unpguid,firstlba,lastlba,Aflag,pname=partitionread.partitionread(binary,a)
            if firstlba==0:
                break_for=False
                break

            a=a+sizeofp
            partition_num=partition_num+1
            name=''
            try:
                for i in pname.decode('utf-8'):
                    if i.isalpha():
                        name=name+i
            except:
                name="no find partition name"
            partition_guid.append(ptguid.hex())
            partition_uniqueid.append(unpguid.hex())
            vbraddress.append(firstlba)
            partition_lastlba.append(lastlba)
            partition_Aflag.append(Aflag)
            partition_name.append(name)


    for i in vbraddress:
        binary=readsector.readfile(filename, i) #vbr주소
        mft,mftmirr=find_MFT.find_mft(binary)
        mft_address.append(i+mft*8)
        mftmirr_address.append(i+mftmirr*8)

    # gui.gui(partition_guid,partition_uniqueid,vbraddress,partition_lastlba,partition_Aflag,partition_name, mft_address,mftmirr_address)
    gui2.gui(partition_guid,partition_uniqueid,vbraddress,partition_lastlba,partition_Aflag,partition_name, mft_address,mftmirr_address,partition_num)