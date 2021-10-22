from tkinter import *

def gui(partition_guid,partition_uniqueid,partition_firstlba,partition_lastlba,partition_Aflag,partition_name, mft_address,mftmirr_address):
    gui = Tk()
    gui.title("결과 창")
    gui.geometry("800x600")

    for i,d in enumerate(partition_guid):
        label=Label(
            gui,
            text='partiton'+str(i))
        label2=Label(
            gui,
            text=f'partition_guid : {partition_guid[i].hex()} \npartition_uniqueid : {partition_uniqueid[i].hex()}\npartition_firstlba : {partition_firstlba[i]}\npartition_lastlba : {partition_lastlba[i]}\npartition_Aflag : {partition_Aflag[i]}\npartition_name : {partition_name[i]}\nmft_address : {mft_address[i]}\nmftmirr_address : {mftmirr_address[i]}'
        )
        label.pack()
        label2.pack()


    # for i,d in enumerate(partition_guid):
    #     treeview = tkinter.ttk.Treeview(gui, columns=["one", "two", "three"], displaycolumns=["one", "two", "three"])
    #     treeview.pack()
    #
    #     treeview.column("#1", width=100, anchor="center")
    #     treeview.heading("one", text="partition1", anchor="center")

    gui.mainloop()
