import tkinter
from random import randint
class myApp():
    def __init__(self,root):
        self.r=root
        self.f1 = tkinter.Frame(self.r)
        self.f1.pack(side='top')
        self.exclick=tkinter.Button(self.f1,text='End',font='Arial 12 ',command=self.endbutton,bg = 'red', width=43)
        self.exclick.grid(row=0,column=2)
        self.stclick=tkinter.Button(self.f1,text='Start',font='Arial 12',command=self.startbutton,bg='green',width=43)
        self.stclick.grid(row=0,column=1)
        self.canvas = tkinter.Canvas(self.r, width=800, height=800,bg='darkgrey')
        self.canvas.pack()
        self.canvas.create_rectangle(0,0,250,250,fill='darkgreen',width='3')   #Crossroads
        self.canvas.create_rectangle(550,0,820,250,fill='darkgreen',width='3')
        self.canvas.create_rectangle(0,550,250,800,fill='darkgreen',width='3')
        self.canvas.create_rectangle(550,550,820,800,fill='darkgreen',width='3') 
        self.canvas.create_line(400,0,400,250,dash=(35,35),fill='white') #Dash lines
        self.canvas.create_line(400,550,400,800,dash=(35,35),fill='white')
        self.canvas.create_line(0,400,250,400,dash=(35,35),fill='white')
        self.canvas.create_line(550,400,800,400,dash=(35,35),fill='white')
        rec_1=self.canvas.create_rectangle(200,140,250,250,fill='black')    #Traffic Light Boxes       
        rec_2=self.canvas.create_rectangle(550,140,600,250,fill='black')
        rec_3=self.canvas.create_rectangle(200,550,250,660,fill='black')
        rec_4=self.canvas.create_rectangle(550,550,600,660,fill='black')
        self.cir1_1=self.canvas.create_oval(210,150,240,180,fill='#330000') #Traffic Lights
        self.cir2_1=self.canvas.create_oval(210,180,240,210,fill='#331f00')
        self.cir3_1=self.canvas.create_oval(210,210,240,240,fill='#001a09')
        self.cir1_2=self.canvas.create_oval(560,150,590,180,fill='#330000')
        self.cir2_2=self.canvas.create_oval(560,180,590,210,fill='#331f00')
        self.cir3_2=self.canvas.create_oval(560,210,590,240,fill='#001a09')
        self.cir1_3=self.canvas.create_oval(210,560,240,590,fill='#330000')
        self.cir2_3=self.canvas.create_oval(210,590,240,620,fill='#331f00')
        self.cir3_3=self.canvas.create_oval(210,620,240,650,fill='#001a09')
        self.cir1_4=self.canvas.create_oval(560,560,590,590,fill='#330000')
        self.cir2_4=self.canvas.create_oval(560,590,590,620,fill='#331f00')
        self.cir3_4=self.canvas.create_oval(560,620,590,650,fill='#001a09')
        self.timespressed=0 #Times the start button has been pressed
        self.count = 0      #Timer
        self.now = 0        #specific moment the traffic lights pattern commences
    def startbutton(self):
        """Συνάρτηση για την αλληλεπίδραση του χρήστη με κουμπί που του επιτρέπει την έναρξη του προγράμματος"""
        if self.timespressed < 1: #if the button is pressed more than once it stops working
            self.run_periodically(self.tick, 1000)
            self.timespressed += 1
    def endbutton(self):
        """Συνάρτηση για την αλληλεπίδραση του χρήστη με κουμπί που του επιτρέπει την λήξη του προγράμματος"""
        self.r.destroy() 
    def run_periodically(self,tick, ms):
        """Συνάρτηση που καλεί περιοδικά τον εαυτό της με αποτέλεσμα την δημιουργία ενός εικονικού χρονομέτρου"""
        tick()
        root.after(ms, self.run_periodically, tick, ms) #calls itself every 1 second
    def tick(self):
        """Συνάρτηση χρονομέτρου και λειτουργίας φαναριών"""
        global what_happened
        self.count += 1 #a second is added in the digital timer
        if self.now == 0 or (self.count - self.now) == 14:  #First state of the pattern
            self.now=self.count
            self.yellow_off(self.cir2_2,self.cir2_3)
            self.red_off(self.cir1_1,self.cir1_4)
            self.green_on(self.cir3_1,self.cir3_4)
            self.red_on(self.cir1_2,self.cir1_3)
            what_happened='green1'
        elif self.count == self.now + 5:     #Second state of the pattern
            self.green_off(self.cir3_1,self.cir3_4)
            self.yellow_on(self.cir2_1,self.cir2_4)
            what_happened='yellow1'
        elif self.count == self.now + 7:    #Third state of the pattern
            self.yellow_off(self.cir2_1,self.cir2_4)
            self.red_on(self.cir1_1,self.cir1_4)
            self.red_off(self.cir1_2,self.cir1_3)
            self.green_on(self.cir3_2,self.cir3_3)
            what_happened='green2'
        elif self.count == self.now + 12:   #Fourth state of the pattern   
            self.green_off(self.cir3_2,self.cir3_3)
            self.yellow_on(self.cir2_2,self.cir2_3)
            what_happened='yellow2'
        if (self.count % 8) == 0 or self.count==1:      #Car generator for every 8s
            r1 = randint(0,1)
            r2 = randint(0,1)
            r3 = randint(0,1)
            r4 = randint(0,1)
            self.car=Cars(self.canvas,r1,r2,r3,r4)  #Class Cars instance
    def green_on(self,cir1,cir2):
        """Πράσινο φανάρι ανοιχτό"""
        self.canvas.itemconfig(cir1,fill='green')
        self.canvas.itemconfig(cir2,fill='green')
    def yellow_on(self,cir1, cir2):
        """Κίτρινο φανάρι ανοιχτό"""
        self.canvas.itemconfig(cir1,fill='orange')
        self.canvas.itemconfig(cir2,fill='orange')
    def red_on(self,cir1, cir2):
        """Κόκκινο φανάρι ανοιχτό"""
        self.canvas.itemconfig(cir1,fill='red')
        self.canvas.itemconfig(cir2,fill='red')       
    def green_off(self,cir1,cir2):
        """Πράσινο φανάρι κλειστό"""
        self.canvas.itemconfig(cir1,fill='#001a09')
        self.canvas.itemconfig(cir2,fill='#001a09')
    def yellow_off(self,cir1, cir2):
        """Κίτρινο φανάρι κλειστό"""
        self.canvas.itemconfig(cir1,fill='#331f00')
        self.canvas.itemconfig(cir2,fill='#331f00')
    def red_off(self,cir1, cir2):
        """Κόκκινο φανάρι κλειστό"""
        self.canvas.itemconfig(cir1,fill='#330000')
        self.canvas.itemconfig(cir2,fill='#330000')
class Cars():
    def __init__(self, canvas, r1, r2, r3, r4):
        global l1,l2,l3,l4
        ran1=randint(0,6)   #Randomly selects a type of car
        ran2=randint(0,6)
        ran3=randint(0,6)
        ran4=randint(0,6)
        self.canvas = canvas
        self.photo1=tkinter.PhotoImage(file=l1[ran1]) #Import images
        self.photo2=tkinter.PhotoImage(file=l2[ran2])
        self.photo3=tkinter.PhotoImage(file=l3[ran3])
        self.photo4=tkinter.PhotoImage(file=l4[ran4])
        self.car1=self.canvas.create_line(560,0,561,0,fill='darkgreen') #In case a car is not created, a small, negligible line is created 
        self.car2=self.canvas.create_line(240,560,239,561,fill='darkgreen') 
        self.car3=self.canvas.create_line(240,0,239,0,fill='darkgreen')
        self.car4=self.canvas.create_line(240,0,239,0,fill='darkgreen')
        if r1 == 1:
            self.car1 = canvas.create_image(0,475,image=self.photo1)
        if r2 == 1:
            self.car2 = canvas.create_image(325,0,image=self.photo2)
        if r3 == 1:
            self.car3 = canvas.create_image(800,325,image=self.photo3)
        if r4 == 1:
            self.car4 = canvas.create_image(475,800,image=self.photo4)
        self.move_car()
    def move_car(self):
        global what_happened
        """Συνάρτηση που καθορίζει την κίνηση των αυτοκινήτων"""
        if what_happened == 'green1':   #Vertical Green
            if 350<=self.canvas.coords(self.car1)[0]<=525 and 500<=self.canvas.coords(self.car4)[1]<=600: #Car accelerates so as to avoid a collision
                self.canvas.move(self.car1,4,0)
            elif 225<=self.canvas.coords(self.car3)[0]<=400 and 150<=self.canvas.coords(self.car2)[1]<=250:
                self.canvas.move(self.car3,-4,0)
            else:
                self.canvas.move(self.car2, 0, 3)   #Car moves normally
                self.canvas.move(self.car4, 0, -3)
                if self.canvas.coords(self.car1)[0] <= 150:     
                    self.canvas.move(self.car1, 3, 0)
                elif self.canvas.coords(self.car1)[0] >= 250:
                    self.canvas.move(self.car1, 5, 0)
                if self.canvas.coords(self.car3)[0] <= 550: 
                    self.canvas.move(self.car3, -5, 0)
                elif self.canvas.coords(self.car3)[0] >= 650:
                    self.canvas.move(self.car3, -3, 0)
        elif what_happened == 'green2': #Horizontal Green
            if 350<=self.canvas.coords(self.car2)[1]<=525 and 500<=self.canvas.coords(self.car3)[0]<=600:   #Car accelerates so as to avoid collision
                self.canvas.move(self.car2,0,4)
            elif 225<=self.canvas.coords(self.car4)[1]<=400 and 150<=self.canvas.coords(self.car1)[0]<=250:
                self.canvas.move(self.car4,0,-4)
            else:
                self.canvas.move(self.car1, 3, 0)   #Car moves normally
                self.canvas.move(self.car3, -3, 0)
                if self.canvas.coords(self.car2)[1] <= 150 :
                    self.canvas.move(self.car2, 0, 3)
                elif self.canvas.coords(self.car2)[1] >= 250:
                    self.canvas.move(self.car2, 0, 5)
                if self.canvas.coords(self.car4)[1] <= 550: 
                    self.canvas.move(self.car4, 0, -5)
                elif self.canvas.coords(self.car4)[1] >= 650:
                    self.canvas.move(self.car4, 0, -3)
        elif what_happened == 'yellow1':    #Vertical Yellow
            if (250<self.canvas.coords(self.car1)[0]<600 or 200<self.canvas.coords(self.car3)[0]<500) and (150<self.canvas.coords(self.car2)[1]<250 or 550<self.canvas.coords(self.car4)[1]<650)  :
                pass #Stops at yellow if it's neccessary              
            else:
                self.canvas.move(self.car2,0,3)     #Car moves normally
                self.canvas.move(self.car4,0,-3)
                if self.canvas.coords(self.car1)[0] <= 150 or self.canvas.coords(self.car1)[0] >= 250:
                    self.canvas.move(self.car1, 3, 0)
                if self.canvas.coords(self.car3)[0] <= 500 or self.canvas.coords(self.car3)[0] >= 650:
                    self.canvas.move(self.car3, -3, 0)
        elif what_happened == 'yellow2':    #Horizontal Yellow       
            if (250<self.canvas.coords(self.car2)[1]<600 or 200<self.canvas.coords(self.car4)[1]<500) and (150<self.canvas.coords(self.car1)[0]<250 or 550<self.canvas.coords(self.car3)[0]<650):
                pass #Stops at yellow if it's neccessary               
            else:
                self.canvas.move(self.car1,3,0) #Car moves normally
                self.canvas.move(self.car3,-3,0)
                if self.canvas.coords(self.car2)[1] <= 150 or self.canvas.coords(self.car2)[1] >= 250:
                    self.canvas.move(self.car2, 0, 3)
                if self.canvas.coords(self.car4)[1] <= 500 or self.canvas.coords(self.car4)[1] >= 650:
                    self.canvas.move(self.car4, 0, -3)        
        self.canvas.after(10, self.move_car)    #Calls itself every 10 ms


        
l1=["./car1.1.gif","./car2.1.gif","./car3.1.gif","./car4.1.gif","./car5.1.gif","./car6.1.gif","./car7.1.gif"] #Types of car for every direction
l2=["./car1.2.gif","./car2.2.gif","./car3.2.gif","./car4.2.gif","./car5.2.gif","./car6.2.gif","./car7.2.gif"]
l3=["./car1.3.gif","./car2.3.gif","./car3.3.gif","./car4.3.gif","./car5.3.gif","./car6.3.gif","./car7.3.gif"]
l4=["./car1.4.gif","./car2.4.gif","./car3.4.gif","./car4.4.gif","./car5.4.gif","./car6.4.gif","./car7.4.gif"]        
what_happened = ''
###====================myApp instance====================###
root=tkinter.Tk(className='ΠΡΟΣΟΜΟIΩΣΗ ΛΕΙΤΟΥΡΓΙΑΣ ΕΝΟΣ ΦΩΤΕΙΝΟΥ ΣΗΜΑΤΟΔΟΤΗ : ΟΜΑΔΑ Ο36')
myapp=myApp(root)
root.mainloop()
