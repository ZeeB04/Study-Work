from tkinter import *
import hashlib, uuid
import os
import json

def main():

    global infoDict
    infoDict = {}

    global root
    root = Tk()
    root.geometry("1000x800")
    root.title("Password Saver 1.1")
    root.resizable(False, False)

    canvas = Canvas(width=300, height=200, bg='black')
    canvas.pack(expand=YES, fill=BOTH)
    canvas1 = Canvas(width = 87, height= 73)
    canvas1.place(x= 450, y = 180)

    global bgImage

    bgImage = PhotoImage(file= "Assets/bg.png")
    logoImage = PhotoImage(file="Assets/smol.png")

    canvas1.create_image(47,40, image=logoImage)
    canvas.create_image(1,1, image=bgImage, anchor="nw")
    canvas.create_text(500, 310, text= "Welcome To The Password Saver App", font="Calibri 18", fill = "white")
    canvas.create_text(500,350,text= "Are you a returning user or a new user?", font="Calibri 18", fill = "white")

    Button(text="Returning",height = 3, width = 17,font = "Calibri 14", command= userLogin).place(x=310,y=400)
    Button(text="New",height = 3, width = 17,font = "Calibri 14", command = createScreen2).place(x=510,y=400)

    root.mainloop()

def createScreen2():

    global screen1
    screen1 = Toplevel()
    screen1.geometry("400x400")
    screen1.title("Registration")
    screen1.resizable(False, False)

    global canvas2

    canvas2 = Canvas(screen1,width = 300, height= 300)

    canvas2.pack(expand=YES, fill = BOTH)
    canvas2.create_image(1, 1, image=bgImage, anchor="nw")
    canvas2.create_text(200, 20, text="Please Enter Your Details Below:", fill = "white", font= "Calibri 14")
    canvas2.create_text(200, 100, text= "Enter a Username:", fill = "white", font= "Calibri 12")
    canvas2.create_text(200, 180, text= "Enter a Password:", fill = "white", font= "Calibri 12")
    canvas2.create_text(200, 240, text= "Re-Enter Password", fill = "white", font= "Calibri 12")

    global username
    global password
    global password1
    global usernameEntry
    global passwordEntry
    global passwordEntry2

    username = StringVar()
    password = StringVar()
    password1 = StringVar()

    usernameEntry = Entry(canvas2, width = 40, justify = "center", textvariable= username)
    usernameEntry.place(x= 80, y= 120)
    passwordEntry = Entry(canvas2, width = 40, justify = "center", textvariable = password, show= "*")
    passwordEntry.place(x= 80, y= 200)
    passwordEntry2 = Entry(canvas2, width = 40, justify = "center", textvariable = password1, show= "*")
    passwordEntry2.place(x= 80, y= 260)
    
    Button(canvas2,text= "Register", width = 12, height = 3, command= registerUser).place(x= 150, y= 290)


def registerUser():

    registeredUsername = username.get()
    registeredPassword = password.get()
    passwordCheck = password1.get()

    
    if registeredPassword == passwordCheck:
        registeredPassword = hashlib.sha512(registeredPassword.encode('utf-8') + registeredUsername.encode('utf-8')).hexdigest()
        infoDict[registeredUsername]=registeredPassword
        with open("Files/data", "w+") as outfile:
            json.dump(infoDict, outfile)
        usernameEntry.delete(0, END)
        passwordEntry.delete(0, END)
        passwordEntry2.delete(0, END)
        canvas2.create_text(200, 370, text = "Registration successful", fill = "green", font = "Calibri 11")
    else:
        regError()

def regError():

    global regErrorPrompt
    regErrorPrompt = Toplevel()
    regErrorPrompt.geometry("200x100")
    regErrorPrompt.title("Error")
    regErrorPrompt.resizable(False, False)
    canvas4 = Canvas(regErrorPrompt,width = 300, height= 300)
    canvas4.pack(expand=YES, fill = BOTH)
    canvas4.create_image(1, 1, image=bgImage, anchor="nw")
    canvas4.create_text(100, 20, text= "Password Doesn't Match", fill="white", font= "Calibri")
    Button(canvas4, text= "OK",width = 10, command= regErrorPrompt.destroy).place(x=60, y=50)

def userLogin():

    global screen2
    screen2 = Toplevel()
    screen2.geometry("400x400")
    screen2.title("Registration")
    screen2.resizable(False, False)

    canvas3 = Canvas(screen2,width = 300, height= 300)
    canvas3.pack(expand=YES, fill = BOTH)
    canvas3.create_image(1, 1, image=bgImage, anchor="nw")
    canvas3.create_text(200, 20, text="Please Enter Your Details Below:", fill = "white", font= "Calibri 14")
    canvas3.create_text(200, 100, text= "Enter a Username:", fill = "white", font= "Calibri 12")
    canvas3.create_text(200, 180, text= "Enter a Password:", fill = "white", font= "Calibri 12")

    global usernameVerify
    global passwordVerify
    global usernameLogin
    global passwordLogin

    usernameVerify = StringVar()
    passwordVerify = StringVar()

    usernameLogin = Entry(canvas3, width = 40, justify = "center", textvariable= usernameVerify)
    usernameLogin.place(x= 80, y= 120)
    passwordLogin = Entry(canvas3, width = 40, justify = "center", textvariable = passwordVerify, show= "*")
    passwordLogin.place(x= 80, y= 200)

    Button(canvas3,text= "Login", width = 12, height = 3, command= loginVerify ).place(x= 150, y= 250)

def passwordNotFound():

    global screen4
    screen4 = Toplevel(screen2)
    screen4.geometry("200x100")
    screen4.title("Error")
    screen4.resizable(False, False)
    canvas4 = Canvas(screen4,width = 300, height= 300)
    canvas4.pack(expand=YES, fill = BOTH)
    canvas4.create_image(1, 1, image=bgImage, anchor="nw")
    canvas4.create_text(100, 20, text= "Invalid Password", fill="white", font= "Calibri")
    Button(canvas4, text= "OK",width = 10, command= screen4.destroy).place(x=60, y=50)


def usernameNotFound():

    global screen5
    screen5 = Toplevel(screen2)
    screen5.geometry("200x100")
    screen5.title("Error")
    screen5.resizable(False, False)
    canvas5 = Canvas(screen5,width = 300, height= 300)
    canvas5.pack(expand=YES, fill = BOTH)
    canvas5.create_image(1, 1, image=bgImage, anchor="nw")
    canvas5.create_text(100, 20, text= "Invalid Username", fill="white", font= "Calibri")
    Button(canvas5, text= "OK",width = 10, command= screen5.destroy).place(x=60, y=50)

def loginVerify():

    global userVerify
    global displayUser

    userVerify = usernameVerify.get()
    passVerify = passwordVerify.get()
    usernameLogin.delete(0, END)
    passwordLogin.delete(0, END)

    passVerify = hashlib.sha512(passVerify.encode('utf-8') + userVerify.encode('utf-8')).hexdigest()

    with open("Files/data") as jsonFile:
        data = json.load(jsonFile)
    if userVerify in data:
        if passVerify in data[userVerify]:
            loginSuccess()
            displayUser = userVerify
        else:
            passwordNotFound()
    else:
        usernameNotFound()

def loginSuccess():

    global displayUser
    screen2.destroy()
    displayUser = userVerify
    session()

def session():

    global displayUser
    global useEntry
    global pwEntry
    global username

    screen6 = Toplevel()
    screen6.geometry("400x400")
    screen6.title("Password Saver 1.0 Session")
    screen6.resizable(False, False)

    canvas6 = Canvas(screen6,width=300, height=200, bg='black')
    canvas6.pack(expand=YES, fill=BOTH)
    canvas6.create_image(1,1, image=bgImage, anchor="nw")
    canvas6.create_text(310,25,text="Welcome "+displayUser+"!",font= "Calibri 14", fill="white")
    Button(canvas6, text= "Logout", width= 10, command= root.destroy).place(x=10, y= 15)

    global pwUse
    global pWord
    pwUse = StringVar()
    pWord = StringVar()
    createFile = open("Files/"+displayUser, "a+")
    createFile.close()
    f = open("Files/"+displayUser, "r")


    canvas6.create_text(130, 78, text="Enter what the password is for:", font= "Calibri 14", fill="white")
    useEntry = Entry(canvas6, width= 63, textvariable=pwUse)
    useEntry.place(x= 10,y= 100)
    Button(canvas6, text= "Save", width= 10, command= saveDetails).place(x=310, y=68)
    canvas6.create_text(155, 140, text="Enter the password you want to save:", font= "Calibri 14", fill="white")
    pwEntry = Entry(canvas6, width=63, show="*", textvariable= pWord)
    pwEntry.place(x=10, y=160)
    displayDetails = Label(canvas6,text= "".join(f),width= 53, height= 13)
    displayDetails.place(x=13, y= 185)

def saveDetails():

    passUse = pwUse.get()
    usePass = pWord.get()

    # usePass = hashlib.sha512(usePass.encode('utf-8') + passUse.encode('utf-8')).hexdigest()
    #
    # userDict[passUse]=usePass


    with open("Files/"+displayUser, "a+") as outfile:
        json.dump(passUse+" | "+usePass, outfile)
        outfile.write("\n")
    useEntry.delete(0, END)
    pwEntry.delete(0, END)

    savePrompt = Toplevel()
    savePrompt.geometry("150x100")
    savePrompt.title("Saved!")
    savePrompt.resizable(False,False)

    canvasPrompt = Canvas(savePrompt,width = 300, height= 300)
    canvasPrompt.pack(expand=YES, fill = BOTH)
    canvasPrompt.create_image(1, 1, image=bgImage, anchor="nw")
    canvasPrompt.create_text(75, 20, text= "Details Saved", fill="white", font= "Calibri")
    Button(canvasPrompt, text= "OK",width = 10, command= savePrompt.destroy).place(x=35, y=50)

main()

