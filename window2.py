import tkinter
import sqlite3
import tkinter.messagebox


def menu():
    global root1, button1, button2, button3, button4, button5, button6

    root1 = tkinter.Tk()
    root1.geometry("280x350")
    root1.title("SISTEMA HOSPITALAR: MENU:")
    m = tkinter.Label(root1, text="MENU: ",
                      font='Timer 16 bold italic', fg='#43B6FE')

    button1 = tkinter.Button(
        root1, text="REGISTRAR PACIENTE: ", fg='#43B', font='bold', command=PAT)
    button2 = tkinter.Button(
        root1, text="N° DO QUARTO: ", fg='#43B', font='bold')
    button3 = tkinter.Button(
        root1, text="REGISTRO DE EMPREGADOS:  ", fg='#43B', font='bold')
    button4 = tkinter.Button(root1, text="RESERVAS: ", fg='#43B', font='bold')
    button5 = tkinter.Button(
        root1, text="CONTA DO PACIENTE: ", fg='#43B', font='bold')
    button6 = tkinter.Button(root1, text="SAIR: ", fg='#43B', font='bold')

    m.place(x=75, y=5)

    button1.pack(side=tkinter.TOP)
    button1.place(x=80, y=50)

    button2.pack(side=tkinter.TOP)
    button2.place(x=80, y=100)

    button3.pack(side=tkinter.TOP)
    button3.place(x=80, y=150)

    button4.pack(side=tkinter.TOP)
    button4.place(x=80, y=200)

    button5.pack(side=tkinter.TOP)
    button5.place(x=80, y=250)

    button6.pack(side=tkinter.TOP)
    button6.place(x=80, y=300)

    root1.mainloop()


def PAT():
    rootp = tkinter.Tk()
    rootp.title("FORMULARIO DE CADASTRAMENTO DE PACIENTES: ")

    regform = tkinter.Label(
        rootp, text="FORMULARIO DE CADASTRAMENTRO DE PACIENTES: ", font="arial 16 bold", fg='#43B6FE')

    id = tkinter.Label(rootp, text="ID DO PACIENTE: ",
                       font="arial 8 bold")
    pat_ID = tkinter.Entry(rootp, width=12)

    name = tkinter.Label(rootp, text="NOME COMPLETO DO PACIENTE: ",
                         font="arial 8 bold")
    pat_NAME = tkinter.Entry(rootp, width=50)

    sex = tkinter.Label(rootp, text="SEXO: ",
                        font="arial 8 bold")
    pat_SEX = tkinter.Entry(rootp, width=12)

    dob = tkinter.Label(rootp, text="DATA NASC (YYYY-MM-DD) : ",
                        font="arial 8 bold")
    pat_DOB = tkinter.Entry(rootp, width=12)

    bg = tkinter.Label(rootp, text="TIPO SANGUÍNEO: ",
                       font="arial 8 bold")
    pat_BG = tkinter.Entry(rootp, width=10)

    c1 = tkinter.Label(rootp, text="TELEFONE: ",
                       font="arial 8 bold")
    pat_CONTACT = tkinter.Entry(rootp, width=20)

    c2 = tkinter.Label(rootp, text="CONTATO ALTERNATIVO: ",
                       font="arial 8 bold")
    pat_CONTACTALT = tkinter.Entry(rootp, width=20)

    email = tkinter.Label(rootp, text="E-MAIL: ",
                          font="arial 8 bold")
    pat_EMAIL = tkinter.Entry(rootp, width=50)

    ct = tkinter.Label(rootp, text="EQUIPE DE CONSULTOR / DOUTOR: ",
                       font="arial 8 bold")
    pat_CT = tkinter.Entry(rootp, width=30)

    address = tkinter.Label(rootp, text="ENDEREÇO DO PACIENTE: ",
                            font="arial 8 bold")
    pat_ADDRESS = tkinter.Entry(rootp, width=50)

    regform.pack()
    id.pack()
    pat_ID.pack()
    name.pack()
    pat_NAME.pack()
    sex.pack()
    pat_SEX.pack()
    dob.pack()
    pat_DOB.pack()
    bg.pack()
    pat_BG.pack()
    c1.pack()
    pat_CONTACT.pack()
    c2.pack()
    pat_CONTACTALT.pack()
    email.pack()
    pat_EMAIL.pack()
    ct.pack()
    pat_CT.pack()
    address.pack()
    pat_ADDRESS.pack()

    rootp.mainloop()
