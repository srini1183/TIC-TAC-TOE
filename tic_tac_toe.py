from tkinter import *


def check(a,b,c,t):
    if a == t and b == t and c == t:
        return True
    else:
        return False    


def verify():
    t1 = buttons[0]['text']
    t2 = buttons[1]['text']
    t3 = buttons[2]['text']
    t4 = buttons[3]['text']
    t5 = buttons[4]['text']
    t6 = buttons[5]['text']
    t7 = buttons[6]['text']
    t8 = buttons[7]['text']
    t9 = buttons[8]['text']

    if check(t1,t2,t3,"X") or check(t2,t5,t8,"X") or check(t1,t5,t9,"X") or check(t1,t4,t7,"X") or check(t3,t6,t9,"X") or check(t3,t5,t7,"X") or check(t4,t5,t6,"X") or check(t7,t8,t9,"X"):
        for button in buttons:
            button.destroy()

        l = Label(root,text = "X won the game")
        b = Button(root,text = "Restart",relief = RIDGE,padx = 20,pady = 20,command = create_game)
        l.grid(row = 0,column = 1)
        b.grid(row = 1,column = 1)
    elif check(t1,t2,t3,"O") or check(t2,t5,t8,"O") or check(t1,t5,t9,"O") or check(t1,t4,t7,"O") or check(t3,t6,t9,"O") or check(t3,t5,t7,"O") or check(t4,t5,t6,"O") or check(t7,t8,t9,"O"):       
        for button in buttons:
            button.destroy()
        l = Label(root,text = "O won the game")
        b = Button(root,text = "Restart",relief = RIDGE,padx = 20,pady = 20,command = create_game)
        l.grid(row = 0,column = 1)
        b.grid(row = 1,column = 1)
    else:
        if count == 9:
            for button in buttons:
                button.destroy()
        
            l = Label(root,text = "Draw!")
            b = Button(root,text = "Restart",relief = RIDGE,padx = 20,pady = 20,command = create_game)
            l.grid(row = 0,column = 1)
            b.grid(row = 1,column = 1)
        else:
            pass

def click(num):
    global buttons
    global x_o
    global count
    buttons[num-1]['text'] = "X" if x_o == 1 else "O"
    buttons[num-1]['state'] = DISABLED
    buttons[num-1]['padx'] = buttons[num-1]['padx'] - 5
    x_o = 1-x_o
    count = count + 1
    verify()
            


def create_game():
    global buttons
    global x_o
    x_o = 1
    count = 0
    buttons = None
    bt1 = Button(root,text="",fg = "#000000",relief = RAISED,padx = 50,pady = 50,command = lambda : click(1))
    bt1.grid(row = 0,column = 0)
    bt2 = Button(root,text="",relief = RAISED,fg = "#000000",padx = 50,pady = 50,command = lambda : click(2))
    bt2.grid(row = 0,column = 1)
    bt3 = Button(root,text="",relief = RAISED,fg = "#000000",padx = 50,pady = 50,command = lambda : click(3))
    bt3.grid(row = 0,column = 2)

    bt4 = Button(root,text="",fg = "#000000",relief = RAISED,padx = 50,pady = 50,command = lambda : click(4))
    bt4.grid(row = 1,column = 0)
    bt5 = Button(root,text="",fg = "#000000",relief = RAISED,padx = 50,pady = 50,command = lambda : click(5))
    bt5.grid(row = 1,column = 1)
    bt6 = Button(root,text="",fg = "#000000",relief = RAISED,padx = 50,pady = 50,command = lambda : click(6))
    bt6.grid(row = 1,column = 2)

    bt7 = Button(root,text="",fg = "#000000",relief = RAISED,padx = 50,pady = 50,command = lambda : click(7))
    bt7.grid(row = 2,column = 0)
    bt8 = Button(root,text="",fg = "#000000",relief = RAISED,padx = 50,pady = 50,command = lambda : click(8))
    bt8.grid(row = 2,column = 1)
    bt9 = Button(root,text="",fg = "#000000",relief = RAISED,padx = 50,pady = 50,command = lambda : click(9))
    bt9.grid(row = 2,column = 2)

    buttons = [bt1,bt2,bt3,bt4,bt5,bt6,bt7,bt8,bt9]



if __name__ == "__main__":
    buttons = None
    x_o = 1
    count = 0
    root = Tk()
    root.resizable(False,False)
    root.option_add('*Font', 'lucida 10 bold')
    root.title('TIC TAC TOE')
    #root.geometry("330x350")
    create_game()
    root.mainloop()
