from tkinter import *
import tkinter.ttk
def gui(partition_guid,partition_uniqueid,partition_firstlba,partition_lastlba,partition_Aflag,partition_name, mft_address,mftmirr_address,partition_num):
    gui = Tk()
    gui.title("결과 창")
    gui.geometry("1800x700")
    num=[]

    lbl = tkinter.Label(gui, text="Partition 별 결과")
    lbl.pack()

    for i in range(partition_num):
        num.append(i)
    treeview = tkinter.ttk.Treeview(gui, columns=num, displaycolumns=num)
    treeview.pack()

    for i,d in enumerate(partition_name):
        treeview.column(i, width=200, anchor="center")
        treeview.heading(i, text='partition'+str(i), anchor="center")

    treelist=[]
    treename=["partition_guid","partition_uniqueid","partition_firstlba","partition_lastlba","partition_Aflag","partition_name","mft_address","mftmirr_address"]
    treelist.append(partition_guid)
    treelist.append(partition_uniqueid)
    treelist.append(partition_firstlba)
    treelist.append(partition_lastlba)
    treelist.append(partition_Aflag)
    treelist.append(partition_name)
    treelist.append(mft_address)
    treelist.append(mftmirr_address)
    for i in range(len(treelist)):
        treeview.insert('','end',text=treename[i],values=treelist[i],iid=str(i)+"번")
    gui.mainloop()
