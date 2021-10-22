from tkinter import *

def drivechoice():

    gui=Tk()
    gui.title("drive 선택")
    gui.geometry("800x600")
    drive = []
    lbl = Label(gui, text="드라이브 선택")
    lbl.pack()

##드라이브 find
    for i in range(0, 10):
        try:
            if open('\\\\.\\PhysicalDrive' + str(i), 'rb'):
                print(str(i) + ' : PhysicalDrive' + str(i) + '\n')
                drive.append('\\\\.\\PhysicalDrive' + str(i))
        except:
            break

    # for i in range(0,len(drive)):
    #     globals()['button_{}'.format(i)]=Button(
    #         gui,width=640,height=5,bg="yellow",
    #         text=drive[i+1],
    #         command=lambda x=drive[i+1:] button_event(x)).pack()



    # for i,d in enumerate(drive):
    #     btn=Button(
    #         width=640,
    #         height=5,
    #         text=drive[i],
    #         command=lambda x=d: on_click(x),
    #     )
    #     btn.pack()


    ###드라이버 선택
    for i, d in enumerate(drive):
        btn = Button(
            width=640,
            height=5,
            text=drive[i],
            command=lambda x=i: on_click(x),
        )
        btn.pack()


    def on_click(i):
        global choice
        choice=i
        gui.quit()


    gui.mainloop()
    drivename=drive[int(choice)]
    print("choice : " ,choice)
    return drivename