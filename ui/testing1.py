# from tkinter import *
# from tkinter.ttk import Notebook, Frame
# from tkinter.messagebox import *
# from services.services import Services
#
#
# servicii: Services = Services()
# servicii_dict = servicii.stoc_bilete
#
#
#
#
# def selecteaza_bilet() -> None:
#     if not(cnp_tf.get().isnumeric()):
#         showerror(title="Eroare!", message=f"Eroare la campul CNP")
#         cnp_tf.delete(0, END)
#         cnp_tf.focus()
#     else:
#         nume_tf.config(state="disabled")
#         prenume_tf.config(state="disabled")
#         cnp_tf.config(state="disabled")
#         email_tf.config(state="disabled")
#         label_selecteaza.grid(column=0, row=6)
#         inapoi_butt.grid(column=0, row=5, pady=20)
#         label_aiselect.config(text="Ai selectat")
#         label_aiselect.grid(column=0, row=7)
#         optiuni.grid(column=1, row=6)
#
#
# def inapoi_func() -> None:
#
#     nume_tf.config(state="normal")
#     prenume_tf.config(state="normal")
#     cnp_tf.config(state="normal")
#     email_tf.config(state="normal")
#     label_selecteaza.grid_forget()
#     inapoi_butt.grid_forget()
#     optiuni.grid_forget()
#     label_aiselect.grid_forget()
#     label_selectia.grid_forget()
#
# def afisare_bilet(*args) -> None:
#     label_selectia.config(text="")
#     label_selectia.config(text=f"{value_inside.get()}")
#     label_selectia.grid(column=1, row=7)
#
#
#
# #---------------------------------------------------------------------------------------------------#
# root: Tk = Tk()
# root.resizable(False, False)
# root.title(string="Bilete la spectacol")
# root.config(pady=20, padx=20)
#
# img: PhotoImage = PhotoImage(file="./ui_pic/buy_ticket.png")
#
# tabcontrol: Notebook = Notebook(root)
#
# tab1: Frame = Frame(tabcontrol)
# tab2: Frame = Frame(tabcontrol)
# tab3: Frame = Frame(tabcontrol)
# tab4: Frame = Frame(tabcontrol)
# tabcontrol.add(tab1, text="Cumpara ticket")
# tabcontrol.add(tab2, text="Editeaza")
# tabcontrol.add(tab3, text="Valideaza ticket")
# tabcontrol.add(tab4, text="Admin")
# tabcontrol.pack(expand=1, fill="both")
# #---------------------------------------------------------------------------------------------------#
# # TABUL CUMPARA ticket column 0
# canvas = Canvas(tab1, height=200, width=250)
# canvas.create_image(70, 70, image=img)
# canvas.grid(column=1, row=0, rowspan=1, columnspan=2)
# Label(tab1, text="Nume").grid(column=0, row=1, pady=3, padx=3)
# Label(tab1, text="Prenume").grid(column=0, row=2, pady=3, padx=3)
# Label(tab1, text="CNP").grid(column=0, row=3, pady=3, padx=3)
# Label(tab1, text="Email").grid(column=0, row=4, pady=3, padx=3)
# label_selecteaza: Label = Label(tab1, text="Selecteaza ticket")
# label_aiselect: Label = Label(tab1, text="")
# #---------------------------------------------------------------------------------------------------#
# # TABUL CUMPARA ticket column 1
#
# nume_tf: Entry = Entry(tab1, width=20)
# nume_tf.grid(column=1, row=1, pady=3)
# prenume_tf: Entry = Entry(tab1, width=20)
# prenume_tf.grid(column=1, row=2, pady=3)
# cnp_tf: Entry = Entry(tab1, width=20)
# cnp_tf.grid(column=1, row=3, pady=3)
# email_tf: Entry = Entry(tab1, width=20)
# email_tf.grid(column=1, row=4, pady=3)
# selecteaza_butt: Button = Button(tab1, text="Selecteaza bilet",background="green", width=20, command=selecteaza_bilet)
# selecteaza_butt.grid(column=1, row=5, pady=10)
# inapoi_butt: Button = Button(tab1, text="<-- Inapoi", background="red", width=10, command=inapoi_func)
# inapoi_butt.grid_forget()
# value_inside: StringVar = StringVar(root)
# value_inside.set("Selecteaza Ticket")
# value_inside.trace("w", afisare_bilet)
# optiuni :OptionMenu = OptionMenu(tab1, value_inside, *servicii_dict.keys())
# optiuni.configure(relief="raised")
# label_selectia: Label = Label(tab1, text="")
#
#
# #---------------------------------------------------------------------------------------------------#
# # TABUL EDITEAZA
#
# Label(tab2, text="Serie ticket").grid(column=0, row=1, pady=3)
# edi_serieTicket: Entry = Entry(tab2, width=20)
# edi_serieTicket.grid(column=1, row=1, pady=3)
# Label(tab2, text="CNP").grid(column=0, row=2, pady=3)
# edi_cnp: Entry = Entry(tab2, width=20)
# edi_cnp.grid(column=1, row=2, pady=3)
# #---------------------------------------------------------------------------------------------------#
# # TABUL VALIDEAZA
# Label(tab3, text="CNP").grid(column=0, row=1, pady=3)
# val_cnp: Entry = Entry(tab3, width=20)
# val_cnp.grid(column=1, row=1, pady=3)
# Label(tab3, text="Serie ticket").grid(column=0, row=2, pady=3)
# val_serieTicket: Entry = Entry(tab3, width=20)
# val_serieTicket.grid(column=1, row=2, pady=3)
# #---------------------------------------------------------------------------------------------------#
#
# root.mainloop()

a:int = int()

print(a)