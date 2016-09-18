from Tkinter import *
import tkMessageBox
from PIL import ImageTk,Image
import random
import time
global level1
class game():
    def level(self,a):
        #map1=[[None]*10]*10
        #for i in range(10):
        #    for j in range(10):
        #        map1[i][j]=random.randint(0,1)

        #0=character, 1=path, 2=wall, 3=water, 4=key, 5=sword, 6=monster, 7=door, 8=boat
        if a ==1:
            map1=  [[2,2,2,2,2,2,2,2,2,2],
                    [0,1,1,1,1,2,2,2,2,2],
                    [2,2,2,2,1,2,2,2,2,2],
                    [2,2,2,2,1,2,2,2,2,2],
                    [2,2,2,2,1,2,2,2,2,2],
                    [2,2,2,2,1,2,2,2,2,2],
                    [2,2,2,2,1,2,2,2,2,2],
                    [2,2,2,2,1,2,2,2,2,2],
                    [2,2,2,2,1,2,2,2,2,2],
                    [2,2,2,2,4,1,1,1,1,7]]

        if a==2:
            map1=  [[1,2,2,2,2,2,2,2,2,2],
                    [0,2,2,2,2,2,2,2,2,2],
                    [1,2,2,2,2,2,2,2,2,2],
                    [1,3,3,1,1,4,1,2,2,2],
                    [1,3,3,2,2,2,1,2,2,2],
                    [1,3,3,2,2,2,1,2,2,2],
                    [1,3,3,2,2,2,1,2,2,2],
                    [1,3,3,2,2,2,1,2,2,2],
                    [1,3,3,2,2,2,1,2,2,2],
                    [8,3,3,2,2,2,1,1,1,7]]

        if a==3:
            map1=  [[1,2,2,2,2,2,2,2,2,2],
                    [0,2,2,2,2,2,2,2,2,2],
                    [1,2,2,2,2,2,2,2,2,2],
                    [1,2,2,2,2,2,2,2,2,2],
                    [5,1,1,1,6,2,2,2,2,2],
                    [2,2,2,2,1,1,2,2,2,2],
                    [2,2,2,2,2,1,1,2,2,2],
                    [2,3,3,2,2,2,1,1,2,2],
                    [2,3,3,2,2,2,2,1,1,2],
                    [2,3,3,2,2,2,2,2,1,7]]
        return map1

    def __init__(self,window):
        #print random.randint(0,1)
        #make my screen dimensions work

        self.width=1200#The value of the width
        self.height=600#The value of the height of the window
        self.window=window
        self.window.title('Level 1')

        #center window if not full screen
        #ws = self.window.winfo_screenwidth()#This value is the width of the screen
        #hs = self.window.winfo_screenheight()#This is the height of the screen
        # calculate position x, y
        #x = (ws/2) - (self.width/2)
        #y = (hs/2) - (self.height/2)
        #self.window.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))

        #fullscreen
        w, h = self.window.winfo_screenwidth(), root.winfo_screenheight()
        self.window.overrideredirect(1)
        self.window.geometry("%dx%d+0+0" % (w, h))
        #the first two parameters are width and height of the window. The last two parameters are x and y screen coordinates.
        #http://zetcode.com/gui/tkinter/introduction/


        self.window.focus_set() # <-- move focus to this widget
        self.window.bind("<Escape>", lambda e: e.widget.quit())
        self.game=Frame(self.window)
        self.game.pack(side='right')# left frame for gameplay
        self.comlist=[]
        self.userinp=Frame(self.window)
        self.userinp.pack(side='left')#right side for input from user


        self.inst=Frame(self.userinp)
        tkMessageBox.showinfo('Rules of the game', '''Rules:
        Try to use the correct commands to reach your target:
        So what is your target?
        Reach the door at the end.
        But do not forget to collect the key!!!
        Try to use the special functions to speed up the game!
        Have fun!''')


        #self.inst.pack(side='left')#instructions
        #self.inst=Label(text='Rules:Try to use the correct commands to reach your target: So what is your target? \nReach the door at the end? But do not forget to collect the key!!!\n Try to use the special functions to speed up the game!\n Have fun!')
        #self.inst.pack()
        self.scroll=Scrollbar(self.userinp)
        self.ta=Text(self.userinp)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.ta.pack()
        self.ta.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.ta.yview)

        self.window.after(1, lambda: window.focus_force())

        #bind keyboard keys
        self.window.bind('<Return>',self.start)
        self.window.bind('<Left>',self.left)
        self.window.bind('<Right>',self.right)
        self.window.bind('<Down>',self.down)
        self.window.bind('<Up>',self.up)

        Button(self.userinp, text='Up',command=self.up).pack(side='left',pady=5,padx=5)
        Button(self.userinp, text='Down',command=self.down).pack(side='left',pady=5,padx=5)
        Button(self.userinp, text='Left',command=self.left,).pack(side='left',pady=5,padx=5)
        Button(self.userinp, text='Right',command=self.right).pack(side='left',pady=5,padx=5)
        Button(self.userinp, text='RightUntilWall',command=self.rightUntilWall).pack(side='left',pady=5,padx=5)
        #Button(self.userinp, text='Pickup Item',command=self.pick).pack(side='left',pady=5,padx=5)
        #Button(self.userinp, text='Drop Item',command=self.drop).pack(side='left',pady=5,padx=5)
        Button(self.userinp, text='Repeat commands',command=self.rep).pack(side='left',pady=5,padx=5)

        Button(self.userinp, text='Undo',command=self.undo).pack(side='left',pady=5,padx=5)
        Button(self.userinp, text='Start!!!',command=self.start).pack(side='left',pady=5,padx=5)
        Button(self.userinp, text='Quit!',command=self.quit).pack(side='left',pady=5,padx=5)



        self.nextLevel=1
        self.map=self.level(self.nextLevel)
        #0=character, 1=path, 2=wall, 3=water, 4=key, 5=sword, 6=monster, 7=door, 8=boat
        self.img=['Link.gif','grey.jpg','brown.jpg','water.gif','key.gif','Linksword.gif','monster.gif', 'door.gif','boat.gif']
        self.pic=[[None]*10]*10
        self.im=[[None]*10]*10
        self.grids=[[None]*10]*10
        self.backpack={'key':False,'boat':False}
        self.gen()#generate map
        #self.window.mainloop()#start loop

    def gen(self):
        #self.map=self.level(self.nextLevel)
        #print 'gen ',self.map
        for i in range(10):#rows
            for j in range(10):#columns
                #print i,j
                self.im[i][j]=Image.open(self.img[self.map[i][j]])#open image
                self.pic[i][j]=ImageTk.PhotoImage(self.im[i][j])#store image in photoimage
                self.grids[i][j]=Label(self.game,image=self.pic[i][j],borderwidth=0)#add photoimage to label
                self.grids[i][j].image=self.pic[i][j] #keep a reference
                self.grids[i][j].grid(row=i+1,column=j+1)#place label at specific coordinate
    def up(self,event=''):
        self.repeat('up')
        for i in range (self.entryValue()):
            self.comlist.append('up')
        self.ta.delete(1.0,END)
        for x in self.comlist:
            self.ta.insert(END,x+'\n')
        print self.comlist
    def down(self,event=''):
        self.repeat('down')
        for i in range (self.entryValue()):
            self.comlist.append('down')
        self.ta.delete(1.0,END)
        for x in self.comlist:
            self.ta.insert(END,x+'\n')
        print self.comlist
    def left(self,event=''):
        self.repeat('left')
        for i in range (self.entryValue()):
            self.comlist.append('left')
        self.ta.delete(1.0,END)
        for x in self.comlist:
            self.ta.insert(END,x+'\n')
        print self.comlist
    def right(self,event=''):
        self.repeat('right')
        for i in range (self.entryValue()):
            self.comlist.append('right')
        self.ta.delete(1.0,END)
        for x in self.comlist:
            self.ta.insert(END,x+'\n')
        print self.comlist
    def pick(self):
        self.comlist.append('pick')
        self.ta.delete(1.0,END)
        for x in self.comlist:
            self.ta.insert(END,x+'\n')
        print self.comlist
    def drop(self):
        self.comlist.append('drop')
        self.ta.delete(1.0,END)
        for x in self.comlist:
            self.ta.insert(END,x+'\n')
        print self.comlist
    def rightUntilWall(self,event=''):
        self.comlist.append('rightUntilWall')
        self.ta.delete(1.0,END)
        for x in self.comlist:
            self.ta.insert(END,x+'\n')
    def leftUntilWall(self,event=''):
        self.comlist.append('leftUntilWall')
        self.ta.delete(1.0,END)
        for x in self.comlist:
            self.ta.insert(END,x+'\n')
    def downUntilWall(self,event=''):
        self.comlist.append('downUntilWall')
        self.ta.delete(1.0,END)
        for x in self.comlist:
            self.ta.insert(END,x+'\n')
    def upUntilWall(self,event=''):
        self.comlist.append('upUntilWall')
        self.ta.delete(1.0,END)
        for x in self.comlist:
            self.ta.insert(END,x+'\n')
    def repeat(self,dir):
        self.w=popupWindow(self.window,dir)
        self.window.wait_window(self.w.top)
        print 'w.value',self.entryValue()
    def rep(self,dir=''):
        self.w=popupWindow1(self.window)
        self.window.wait_window(self.w.top)
        print 'w.value',self.entryValue()
        comm=self.comlist[-self.entryValue():]
        print comm
        self.comlist.extend(comm)
        self.ta.delete(1.0,END)
        for x in self.comlist:
            self.ta.insert(END,x+'\n')
        print self.comlist

    def entryValue(self):
        return self.w.value

    def undo(self,event):
        self.comlist.pop()
        self.ta.delete(1.0,END)
        for x in self.comlist:
            self.ta.insert(END,x+'\n')
    def start(self,event=''):
        a,b=1,0
        self.error=0
        if self.comlist!=[]:
            i=0
            while i<len(self.comlist):
                #print 'iterating movements'
                print self.backpack
                if self.level(self.nextLevel)[a][b] in [1,3]:
                    self.map[a][b]= self.level(self.nextLevel)[a][b] #reset to normal terrain after moving
                if self.level(self.nextLevel)[a][b] in [4,8,0]:
                    self.map[a][b]= 1 #reset to normal terrain after moving
                if self.comlist[i]=='down':
                    if self.map[a+1][b]!=2:
                        a+=1
                        i+=1
                    else:
                        self.error=1
                elif self.comlist[i]=='up':
                    if self.map[a-1][b]!=2:
                        a-=1
                        i+=1
                    else:
                        self.error=1
                elif self.comlist[i]=='left':
                    if self.map[a][b-1]!=2:
                        b-=1
                        i+=1
                    else:
                        self.error=1
                elif self.comlist[i]=='right':
                    if self.map[a][b+1]!=2:
                        b+=1
                        i+=1
                    else:
                        self.error=1
                elif self.comlist[i]=='pick':
                    pass
                    i+=1
                elif self.comlist[i]=='drop':
                    pass
                    i+=1
                elif self.comlist[i]=='rightUntilWall':
                    #if i want right until finish point and wall, use not in [2]
                    if self.map[a][b+1] not in [2,7]: # not wall or door
                        b+=1
                        self.comlist.insert(i+1,'rightUntilWall')# add element to the list in the next index to repeat move
                        i+=1
                        print self.comlist
                        print i
                    else:
                        i+=1
                elif self.comlist[i]=='leftUntilWall':
                    #if i want right until finish point and wall, use not in [2]
                    if self.map[a][b-1] not in [2,7]: # not wall or door
                        b-=1
                        self.comlist.insert(i+1,'rightUntilWall')# add element to the list in the next index to repeat move
                        i+=1
                        print self.comlist
                        print i
                    else:
                        i+=1
                elif self.comlist[i]=='downUntilWall':
                    #if i want right until finish point and wall, use not in [2]
                    if self.map[a+1][b] not in [2,7]: # not wall or door
                        a+=1
                        self.comlist.insert(i+1,'downUntilWall')# add element to the list in the next index to repeat move
                        i+=1
                        print self.comlist
                        print i
                    else:
                        i+=1
                elif self.comlist[i]=='upUntilWall':
                    #if i want right until finish point and wall, use not in [2]
                    if self.map[a-1][b] not in [2,7]: # not wall or door
                        a-=1
                        self.comlist.insert(i+1,'upUntilWall')# add element to the list in the next index to repeat move
                        i+=1
                        print self.comlist
                        print i
                    else:
                        i+=1
                else:
                    pass
                #self.map=self.level(self.nextLevel)

                if self.level(self.nextLevel)[a][b]==3 and not self.backpack['boat']:
                    self.error=1
                    tkMessageBox.showwarning('ERROR', 'You cannot cross the river without a boat!!!')
                if self.level(self.nextLevel)[a][b]==7 and not self.backpack['key']:
                   self.error=1
                   tkMessageBox.showwarning('ERROR','You cannot open the door without a key!!!')
                if self.error==1:
                    a,b=1,0
                    break
                else:
                    self.map[a][b]=0 # update new location of player
                    self.window.after(50,self.move(a,b))

                #while traversing the while loop, show a pop up whenever a key or boat is picked up
                if self.level(self.nextLevel)[a][b] ==4:
                	self.backpack['key']=True
                	tkMessageBox.showinfo('Wohoo!', 'You collected a key!!!')

                if self.level(self.nextLevel)[a][b] ==8:
                	self.backpack['boat']=True
                	tkMessageBox.showinfo('Wohoo!', 'You collected a boat!!!')


            if self.error==1 or (self.map[9][9]!=0 and self.map[1][0]!=0):                              #siyuan i added it again  # Viren, i deleted (self.map[9][9]!=0 and self.map[1][0]!=0) or -Siyuan
                print 'error'
                self.backpack={'key':False,'boat':False}
                self.reset()
                #if player uses right until wall accidentally for completion
            #else:
            #print 'Error'
            #self.backpack={'key':False,'boat':False}
            #self.reset()

        else:
            tkMessageBox.showwarning('Codes missing', 'Where is your code bro?')

    def reset(self):
        tkMessageBox.showwarning('Error', 'Sorry, you have to restart bro!')
        self.map=self.level(self.nextLevel)
        self.ta.delete(1.0,END)#empty text
        self.gen()
        self.comlist=[]
        print 'reset'

    def move(self,a,b):
        self.gen()
        if self.map[9][9]==0 and self.backpack['key']:
            tkMessageBox.showinfo('Yay!', 'Completed Level!!!')
            self.backpack={'key':False,'boat':False}     #reset inventory items
            self.nextLevel+=1                            #increase level
            self.map=self.level(self.nextLevel)          #load next level
            self.comlist=[]                              #clear commands list
            self.ta.delete(1.0,END)                      #empty text widget
            self.move(1,0)                               #move to starting position
            self.error=0                                 #clear error
            self.window.title('Level '+str(self.nextLevel))
        self.window.update()
    def quit(self):
        tkMessageBox.showinfo('Thank you.', 'Thank you for playing the game.\nHope that you have learnt some\nimportant skills.\n\n\nThis game was created by:\n\n\nPin Yaw\nKevin\nJunXian\nSiyuan\nPavithren ')
        self.window.destroy()
class popupWindow(object):
    def __init__(self,master,dir):
        top=self.top=Toplevel(master)
        self.dir=dir
        top.title(dir)
        top.bind('<Return>',self.cleanup)
        self.l=Label(top,text="How many times should I repeat " + dir  +  "?")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.e.focus()                      #set focus on entry widget so that user doesn't have to click on entry
        self.o=Button(top,text='Once only',command=self.once)
        #self.u=Button(top,text='Move Until wall',command=lambda: self.until)
        self.b=Button(top,text='Ok',command=self.cleanup)
        #self.u.pack(fill=BOTH)
        self.b.pack(fill=BOTH)
        self.o.pack(fill=BOTH)
        self.untilwall=0

    def cleanup(self,event=''):
        try:
            self.value=int(self.e.get())
            self.err=0
        except ValueError:
            self.err=1
            tkMessageBox.showwarning('ERROR','Enter numbers only!!!')
            self.e.focus()
        if not self.err:
            self.top.destroy()
    def once(self):
        self.value=1
        self.top.destroy()
    def until(self):
        if self.dir=='left':
            self.leftUntilWall()
        if self.dir=='right':
            self.rightUntilWall()
        if self.dir=='down':
            self.downUntilWall()
        if self.dir=='up':
            self.upUntilWall()
        self.top.destroy()

class popupWindow1(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        top.title('Repeat last commands')
        top.bind('<Return>',self.cleanup)
        self.l=Label(top,text="Repeat the last")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.e.focus()                      #set focus on entry widget so that user doesn't have to click on entry
        self.l2=Label(top,text=" commands")
        self.l2.pack()

        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack(fill=BOTH)
        self.untilwall=0

    def cleanup(self,event=''):
        try:
            self.value=int(self.e.get())
            self.err=0
        except ValueError:
            self.err=1
            tkMessageBox.showwarning('ERROR','Enter numbers only!!!')
            self.e.focus()
        if not self.err:
            self.top.destroy()
    def once(self):
        self.value=1
        self.top.destroy()

if __name__ == "__main__":
    root=Tk()
    m=game(root)
    root.mainloop()
#game()
