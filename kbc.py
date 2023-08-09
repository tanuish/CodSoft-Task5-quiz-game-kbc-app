from tkinter import *
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3

engine=pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

mixer.init()
mixer.music.load('kbc.mp3')
mixer.music.play()
#function for running the question 
 
def select(event):
    
    #for removing call button
    call_button.place_forget()
    
    # for removing pole from game 
    
    # prograss bar removing 
    ProgressbarA.place_forget()
    ProgressbarB.place_forget()
    ProgressbarC.place_forget()
    ProgressbarD.place_forget()
    
    # label removing
    
    Progressbar_labelA.place_forget()
    Progressbar_labelB.place_forget()
    Progressbar_labelC.place_forget()
    Progressbar_labelD.place_forget() 
    
    b= event.widget
    value =b["text"]
    
    for i in range(15):
            
        if value==correct_answer[i]:
            
            if value==correct_answer[14]:
                
                #fun for close button 
            
                def close_fun():
                    root2.destroy()
                    root.destroy()
                
                #fun for try again 
                
                def play_again():
                    button_50.config(state=NORMAL,image=image_50)
                    button_audiancepole.config(state=NORMAL,image=image_audiancepole)
                    button_phoneafriend.config(state=NORMAL,image=image_phoneafriend)
                    root2.destroy()
                    que_area.delete(1.0,END)
                    que_area.insert(END,question[0])
                    
                    #option
                    button_optionA.config(text=option1[0]) 
                    button_optionB.config(text=option2[0]) 
                    button_optionC.config(text=option3[0]) 
                    button_optionD.config(text=option4[0]) 
                    
                    amount_lebel.config(image=image_amount)
                    
                    #music of kbc
                    
                mixer.music.stop()
                mixer.music.load('Kbcwon.mp3')
                mixer.music.play()     
                
                root2 =Toplevel()
                root2.overrideredirect(True)
                root2.config(bg="black") 
                root2.geometry('500x400+140+30')
                root2.title('you won 0 pound')
                wrong_img_logo=Label(root2,image=image_kbc,bd=0)
                wrong_img_logo.pack(pady=30)
                    
                #win label 
                WIN_label =Label(root2,text="YOU WIN",font=('arial',40,'bold'),bg='black',fg='white')
                WIN_label.pack()
                    
                # PLAY again button 
                    
                playagain_button = Button(root2,text="play again",font=("arial",20,'bold'),fg='white',bg='black',activebackground='black',activeforeground="white",bd=0,cursor="hand2",command=play_again)
                playagain_button.pack()
                    
                #close button 
                close_button = Button(root2,text="close",font=("arial",20,'bold'),fg='white',bg='black',activebackground='black',activeforeground="white",bd=0,cursor="hand2",command=close_fun)
                close_button.pack()
                    
                #sad image
                happyimage =PhotoImage(file='happy.png')
                happy_label=Label(root2,image=happyimage,bg='black')
                happy_label.place(x=30,y=280)
                    
                happyimage1 =PhotoImage(file='happy.png')
                happy_label1=Label(root2,image=happyimage1,bg='black')
                happy_label1.place(x=400,y=280)
                    
                    
                    
                root2.mainloop()
                break    

                
                
            
            que_area.delete(1.0,END)
            que_area.insert(END,question[i+1])
            
            button_optionA.config(text=option1[i+1])
            button_optionB.config(text=option2[i+1])
            button_optionC.config(text=option3[i+1])
            button_optionD.config(text=option4[i+1])
            amount_lebel.config(image=amount_image_list[i])
            
        if value  not in correct_answer:
            
            # for wrong answer 
            
            #fun for close button 
            
            def close_fun():
                root1.destroy()
                root.destroy()
            
            #fun for try again 
            
            def try_again():
                
                button_50.config(state=NORMAL,image=image_50)
                button_audiancepole.config(state=NORMAL,image=image_audiancepole)
                button_phoneafriend.config(state=NORMAL,image=image_phoneafriend)
                
                root1.destroy()
                que_area.delete(1.0,END)
                que_area.insert(END,question[0])
                
                #option
                button_optionA.config(text=option1[0]) 
                button_optionB.config(text=option2[0]) 
                button_optionC.config(text=option3[0]) 
                button_optionD.config(text=option4[0]) 
                
                amount_lebel.config(image=image_amount)
                    
            
            root1 =Toplevel()
            root1.overrideredirect(True) 
            root1.config(bg="black") 
            root1.geometry('500x400+140+30')
            root1.title('you won 0 pound')
            wrong_img_logo=Label(root1,image=image_kbc,bd=0)
            wrong_img_logo.pack(pady=30)
            
            #lose label 
            lose_label =Label(root1,text="You Lose",font=('arial',40,'bold'),bg='black',fg='white')
            lose_label.pack()
            
            # try again button 
            
            tryagain_button = Button(root1,text="try again",font=("arial",20,'bold'),fg='white',bg='black',activebackground='black',activeforeground="white",bd=0,cursor="hand2",command=try_again)
            tryagain_button.pack()
            
            #close button 
            close_button = Button(root1,text="close",font=("arial",20,'bold'),fg='white',bg='black',activebackground='black',activeforeground="white",bd=0,cursor="hand2",command=close_fun)
            close_button.pack()
            
            #sad image
            sadimage =PhotoImage(file='sad.png')
            sad_label=Label(root1,image=sadimage,bg='black')
            sad_label.place(x=30,y=280)
            
            sadimage1 =PhotoImage(file='sad.png')
            sad_label1=Label(root1,image=sadimage,bg='black')
            sad_label1.place(x=400,y=280)
            
            
            
            root1.mainloop()
            break
            
# function for 50-50 lifeline

def fun_5050():
    button_50.config(image=image_50X,state=DISABLED)
    if que_area.get(1.0,'end-1c')==question[0]:
        
        button_optionB.config(text=" ")
        button_optionC.config(text=" ")
    
    if que_area.get(1.0,'end-1c')==question[1]:
        
        button_optionA.config(text=" ")
        button_optionC.config(text=" ")
    
    if que_area.get(1.0,'end-1c')==question[2]:
        
        button_optionB.config(text=" ")
        button_optionA.config(text=" ")
        
    if que_area.get(1.0,'end-1c')==question[3]:
        
        button_optionB.config(text=" ")
        button_optionC.config(text=" ") 
        
    if que_area.get(1.0,'end-1c')==question[4]:
        
        button_optionB.config(text=" ")
        button_optionC.config(text=" ")
    
    if que_area.get(1.0,'end-1c')==question[5]:
        
        button_optionD.config(text=" ")
        button_optionC.config(text=" ")
    
    if que_area.get(1.0,'end-1c')==question[6]:
        
        button_optionB.config(text=" ")
        button_optionA.config(text=" ")
        
    if que_area.get(1.0,'end-1c')==question[7]:
        
        button_optionB.config(text=" ")
        button_optionC.config(text=" ")
        
    if que_area.get(1.0,'end-1c')==question[8]:
        
        button_optionB.config(text=" ")
        button_optionC.config(text=" ")
        
    if que_area.get(1.0,'end-1c')==question[9]:
        
        button_optionD.config(text=" ")
        button_optionC.config(text=" ")
        
    if que_area.get(1.0,'end-1c')==question[10]:
        
        button_optionB.config(text=" ")
        button_optionC.config(text=" ")
        
    if que_area.get(1.0,'end-1c')==question[11]:
        
        button_optionB.config(text=" ")
        button_optionD.config(text=" ")
        
    if que_area.get(1.0,'end-1c')==question[12]:
        
        button_optionB.config(text=" ")
        button_optionC.config(text=" ")
        
    if que_area.get(1.0,'end-1c')==question[13]:
        
        button_optionA.config(text=" ")
        button_optionC.config(text=" ")
        
    if que_area.get(1.0,'end-1c')==question[14]:
        
        button_optionB.config(text=" ")
        button_optionC.config(text=" ")

# aduiance pole fun 

def aduiancepole_fun():
    button_audiancepole.config(image=image_audiancepoleX,state=DISABLED)
    # for pole of auduiance pole
    
    ProgressbarA.place(x=580,y=190)
    ProgressbarB.place(x=620,y=190)
    ProgressbarC.place(x=660,y=190)
    ProgressbarD.place(x=700,y=190)        
    
    # fole logo of audiance pole
    
    Progressbar_labelA.place(x=580,y=320)
    Progressbar_labelB.place(x=620,y=320)
    Progressbar_labelC.place(x=660,y=320)
    Progressbar_labelD.place(x=700,y=320)
    
    # for correct answer process 
    
    if  que_area.get(1.0,'end-1c')==question[0]:
        ProgressbarA.config(value=75)
        ProgressbarB.config(value=20)
        ProgressbarC.config(value=10)
        ProgressbarD.config(value=45)
        
    if  que_area.get(1.0,'end-1c')==question[1]:
        ProgressbarA.config(value=25)
        ProgressbarB.config(value=90)
        ProgressbarC.config(value=45)
        ProgressbarD.config(value=22)
        
    if  que_area.get(1.0,'end-1c')==question[2]:
        ProgressbarA.config(value=49)
        ProgressbarB.config(value=30)
        ProgressbarC.config(value=80)
        ProgressbarD.config(value=20)
        
    if  que_area.get(1.0,'end-1c')==question[3]:
        ProgressbarA.config(value=60)
        ProgressbarB.config(value=20)
        ProgressbarC.config(value=10)
        ProgressbarD.config(value=90)
        
    if  que_area.get(1.0,'end-1c')==question[4]:
        ProgressbarA.config(value=75)
        ProgressbarB.config(value=20)
        ProgressbarC.config(value=10)
        ProgressbarD.config(value=45)
        
    if  que_area.get(1.0,'end-1c')==question[5]:
        ProgressbarA.config(value=65)
        ProgressbarB.config(value=90)
        ProgressbarC.config(value=10)
        ProgressbarD.config(value=45)
        
    if  que_area.get(1.0,'end-1c')==question[6]:
        ProgressbarA.config(value=65)
        ProgressbarB.config(value=20)
        ProgressbarC.config(value=90)
        ProgressbarD.config(value=45)
        
    if  que_area.get(1.0,'end-1c')==question[7]:
        ProgressbarA.config(value=55)
        ProgressbarB.config(value=20)
        ProgressbarC.config(value=10)
        ProgressbarD.config(value=95)                            
        
    if  que_area.get(1.0,'end-1c')==question[8]:
        ProgressbarA.config(value=55)
        ProgressbarB.config(value=20)
        ProgressbarC.config(value=10)
        ProgressbarD.config(value=85)
        
    if  que_area.get(1.0,'end-1c')==question[9]:
        ProgressbarA.config(value=95)
        ProgressbarB.config(value=20)
        ProgressbarC.config(value=10)
        ProgressbarD.config(value=45)
        
    if  que_area.get(1.0,'end-1c')==question[10]:
        ProgressbarA.config(value=75)
        ProgressbarB.config(value=20)
        ProgressbarC.config(value=10)
        ProgressbarD.config(value=45)
        
    if  que_area.get(1.0,'end-1c')==question[11]:
        ProgressbarA.config(value=55)
        ProgressbarB.config(value=20)
        ProgressbarC.config(value=80)
        ProgressbarD.config(value=45)
        
    if  que_area.get(1.0,'end-1c')==question[12]:
        ProgressbarA.config(value=75)
        ProgressbarB.config(value=20)
        ProgressbarC.config(value=10)
        ProgressbarD.config(value=45)
        
    if  que_area.get(1.0,'end-1c')==question[13]:
        ProgressbarA.config(value=65)
        ProgressbarB.config(value=20)
        ProgressbarC.config(value=10)
        ProgressbarD.config(value=95)
        
    if  que_area.get(1.0,'end-1c')==question[14]:
        ProgressbarA.config(value=55)
        ProgressbarB.config(value=20)
        ProgressbarC.config(value=10)
        ProgressbarD.config(value=85)

# function for phonea friend lifeline
 
def phonelifeline_fun() :
    mixer.music.load('calling.mp3')
    mixer.music.play()
    
    button_phoneafriend.config(image=image_phoneafriendX,state=DISABLED)
    call_button.place(x=70,y=260)

#function for phone click of phone a friend life line     
        
def phoneclick_fun():
    for i in range(15):
        if que_area.get(1.0,'end-1c')==question[i]:
            engine.say(f'the answer is {correct_answer[i]}')
            engine.runAndWait()
            

            
  #question 
question = ["1 Which of the following is the first calculating device?",
            "2 Who invented mechanical calculator called Pascaline?",
            "3 Who among the following considered as the 'father of artificial intelligence'?",
            "4 Which was the world's first successful electronic computer?",
            "5 Who among the following used the term computer worm for the first time?",
            "6 Which was first virus detected on ARPANET, ?",
            "7 Select the example of application software of computer ?",
            "8 Which of the following is also called translator?",
            "9 How the quality of printer is measured?",
            "10 Name the person who had written the first worm written for computer i.e. The Morris worm?",
            "11 Which are the two of the most commonly used languages for CGI Common Gateway Interface scripts?",
            "12 Which of these is not a programming language?",
            "13 What does the command prompt uses?",
            "14 Which out of the following can be called as modifiers?",
            "15 Which out the following is a scripting language?"]

option1=["Abacus","Charles Babbage","Charles Babbage","PARAM","John Brunner","Exe Flie","Ms Word","Data representation",
         "Alphabet per strike","Robert Tappan ","Perl and C++","BASIC","Command Line Interface",
         "Keys Num Lock, Backspace, and Tab", "Java"]


option2 =["Calculator","Blaise Pascal","Lee De Forest","CRAY-1","Alan Turing","Creeper Virus","Ms Excel","MS-DOS",
          "Words per Inch","Charles Alderton","Java & C++","COBOL","Graphical User Interface",
          "Keys, Page Up , Page Down, Print SC","Python"]


option3 =["Turing Machine","Alan Turing","John McCarthy","Pascaline","John McCarthy","Peeper Virus","Both A and B",
          "Operating System","Strike per Inch","George Bangs","C & Java","BNF","Text User Interface TUI","Keys Tab, caps lock , End",
          "Lisp"]

option4 = ["Pascaline","Lee De Forest","JP Eckert","ENIAC","JP Eckert",
           "Trozen horse","MS-DOS","Language Processor","Dots per Inch","William Beldue","Perl  & Java","FORTRAN","N O A",
           "Keys Alt, Shift, or Ctrl","All of the above"]

correct_answer =["Abacus","Blaise Pascal","John McCarthy","ENIAC","John Brunner","Creeper Virus","Both A and B","Language Processor","Dots per Inch","Robert Tappan ",
                "Perl and C++","BNF","Command Line Interface","Keys Alt, Shift, or Ctrl","All of the above"]




root=Tk()
root.title('K.B.C')
root.geometry('1270x652+0+0')
root.config(bg="black")

# frame 
#left frame

left_frame = Frame(root,bg='black',padx=90) 
left_frame.grid(row=0,column=0)

#left top frame

top_left_frame =Frame(left_frame,bg='black',pady=15)
top_left_frame.grid(row=0,column=0)

#left centre frame 

centre_left_frame = Frame(left_frame,bg='black',pady=15)
centre_left_frame.grid(row=1,column=0)

# left bottom frame

bottom_left_frame = Frame(left_frame)
bottom_left_frame.grid(row=2,column=0)

## Right frame 
right_frame = Frame(root,padx=50,pady=25,background='black')
right_frame.grid(row=0,column=1) 

#lifeline
# 50-50 

image_50 = PhotoImage(file="50-50.png")

image_50X=PhotoImage(file="50-50-X.png")

#button for 50 50 
button_50 =Button(top_left_frame,image=image_50,bg='black',bd=0,activebackground='black',width=180,height=80,command=fun_5050)
button_50.grid(row=0,column=0)

# auduence pole 

image_audiancepole =PhotoImage(file='audiencePole.png')

image_audiancepoleX =PhotoImage(file='audiencePoleX.png')

button_audiancepole =Button(top_left_frame,image=image_audiancepole,bg='black',bd=0,activebackground='black',
                            width=180,height=80,command=aduiancepole_fun)
button_audiancepole.grid(row=0,column=1)

# phoneafriend 

image_phoneafriend =PhotoImage(file='phoneAFriend.png')

image_phoneafriendX =PhotoImage(file='phoneAFriendX.png')

button_phoneafriend =Button(top_left_frame,image=image_phoneafriend,bg='black',bd=0,activebackground='black',
                            width=180,height=80,command=phonelifeline_fun)
button_phoneafriend.grid(row=0,column=2)

#call button and img

call_image = PhotoImage(file='phone.png')

call_button = Button(root,image=call_image,bd=0,bg="black",activebackground="black",cursor='hand2',command=phoneclick_fun)

# kbc logo 
image_kbc =PhotoImage(file='center.png')
kbc_lebel =Label(centre_left_frame,image=image_kbc,bg='black',width=310,height=210)
kbc_lebel.grid(row=0,column=0)

# amount poll 

image_amount =PhotoImage(file='Picture0.png')
image_amount1 =PhotoImage(file='Picture1.png')
image_amount2 =PhotoImage(file='Picture2.png')
image_amount3 =PhotoImage(file='Picture3.png')
image_amount4 =PhotoImage(file='Picture4.png')
image_amount5 =PhotoImage(file='Picture5.png')
image_amount6 =PhotoImage(file='Picture6.png')
image_amount7 =PhotoImage(file='Picture7.png')
image_amount8 =PhotoImage(file='Picture8.png')
image_amount9 =PhotoImage(file='Picture9.png')
image_amount10 =PhotoImage(file='Picture10.png')
image_amount11 =PhotoImage(file='Picture11.png')
image_amount12 =PhotoImage(file='Picture12.png')
image_amount13 =PhotoImage(file='Picture13.png')
image_amount14 =PhotoImage(file='Picture14.png')
image_amount15 =PhotoImage(file='Picture15.png')

amount_image_list =[image_amount1,image_amount2,image_amount3,image_amount4,image_amount5,image_amount6,image_amount7,image_amount8,image_amount9,image_amount10,image_amount11,image_amount12,image_amount13,image_amount14,image_amount15]
amount_lebel =Label(right_frame,image=image_amount,bg='black')
amount_lebel.grid(row=0,column=0)

#question platform 
que_image = PhotoImage(file='lay.png')
que_label = Label(bottom_left_frame,image=que_image,bg='black')
que_label.grid(row=0,column=0)

# queation area fitted 
que_area =Text(bottom_left_frame,font=("arials",18,"bold"),width=34,height=2,wrap="word",bg="black",fg="white",bd=0)
que_area.place(x=70,y=10) 
que_area.insert(END,question[0])

# option 

#lableA
labelA =Label(bottom_left_frame,text="A:",bg="black",fg="white",font=("arial",16,"bold"))
labelA.place(x=50,y=110)

# option A button
button_optionA =Button(bottom_left_frame,text=option1[0],font=("arial",16,"bold"),fg="white",bg="black",
                       bd=0,activebackground="black",activeforeground="white")
button_optionA.place(x=90,y=105)


# lableB
labelB =Label(bottom_left_frame,text="B:",bg="black",fg="white",font=("arial",16,"bold"))
labelB.place(x=330,y=110)

#option B button 
button_optionB = Button(bottom_left_frame,text=option2[0],font=("arial",16,'bold'),bg="black",fg="white",bd=0,
                        activebackground="black",activeforeground="white")
button_optionB.place(x=360,y=105)

# label C
labelC =Label(bottom_left_frame,text="C:",font=("arial",16,"bold"),bg="black",fg="white")
labelC.place(x=50,y=190)

#option c button 
button_optionC =Button(bottom_left_frame,text=option3[0],fg="white",bg="black",bd=0,font=('arial',16,"bold"),activebackground="black",activeforeground="white",)
button_optionC.place(x=80,y=185)

# labelD
labelD =Label(bottom_left_frame,text="D:",font=("arial",16,"bold"),fg="white",bg="black")
labelD.place(x=330,y=190)

# button_optionD
button_optionD=Button(bottom_left_frame,text=option4[0],fg="white",bg="black",bd=0,font=('arial',16,'bold'),activebackground='black',activeforeground="white")
button_optionD.place(x=360,y=185)



# button bind

button_optionA.bind("<Button-1>",select)
button_optionB.bind("<Button-1>",select)
button_optionC.bind("<Button-1>",select)
button_optionD.bind("<Button-1>",select)

# for audiance poll 4 poll a,b,c,d 

ProgressbarA=Progressbar(root,orient=VERTICAL,length=120)
ProgressbarB=Progressbar(root,orient=VERTICAL,length=120)
ProgressbarC=Progressbar(root,orient=VERTICAL,length=120)
ProgressbarD=Progressbar(root,orient=VERTICAL,length=120)

#label logo of audiance poll 
Progressbar_labelA=Label(root,text="A",font=('arial',20,"bold"),fg='white',bg='black')
Progressbar_labelB=Label(root,text="B",font=('arial',20,"bold"),fg='white',bg='black')
Progressbar_labelC=Label(root,text="C",font=('arial',20,"bold"),fg='white',bg='black')
Progressbar_labelD=Label(root,text="D",font=('arial',20,"bold"),fg='white',bg='black')


root.mainloop()