import tkinter
from window2 import menu


def GET():
    global userbox, passbox, error
    S1 = userbox.get()
    S2 = passbox.get()

    if (S1 == 'san1' and S2 == '123'):
        menu()
    elif (S1 == 'san2' and S2 == '123'):
        menu()
    else:
        error = tkinter.Label(
            bottomframe, text="FAVOR DIGITAR NOME DE USUÁRIO E SENHA CORRETA.", fg="red", font="bold")
        error.pack()


def Entry():
    global userbox, passbox, login, topframe, bottomframe, image_1
    root = tkinter.Tk()
    root.geometry("600x600")
    topframe = tkinter.Frame(root)
    topframe.pack()

    bottomframe = tkinter.Frame(root)
    bottomframe.pack()

    heading = tkinter.Label(
        topframe, text=" SISTEMA HOSPITALAR", fg='#43B6FE', font='Timer 16 bold italic')

    username = tkinter.Label(topframe, text="Usuário: ")
    userbox = tkinter.Entry(topframe)

    password = tkinter.Label(bottomframe, text="Senha: ")
    passbox = tkinter.Entry(bottomframe)

    login = tkinter.Button(bottomframe, text="LOGIN",
                           font='arial 8 bold', command=GET)

    root.wm_iconbitmap(r'C:\\Git\\repos\\SisHospitar\\icones\\senha.ico')
    image = tkinter.PhotoImage(
        file="C:\\Git\\repos\\SisHospitar\\img\\login.png")
    image = image.subsample(1, 1)
    labelimg = tkinter.Label(image=image, height="380", width="450")
    labelimg.pack()

    heading.pack()
    username.pack()
    userbox.pack()
    password.pack()
    passbox.pack()
    login.pack()
    root.title("Sistema Hospitalar: LOGIN: ")

    root.mainloop()


Entry()
