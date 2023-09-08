from customtkinter import *
from PIL import Image

main = CTk()
main.title("Login Page")
main.config(bg="white")
main.resizable(False, False)

bg_img = CTkImage(dark_image=Image.open("bg1.jpg"), size=(500, 500))

bg_lab = CTkLabel(main, image=bg_img, text="")
bg_lab.grid(row=0, column=0)

frame1 = CTkFrame(main,fg_color="#D9D9D9", bg_color="white", height=350, width=300,corner_radius=20)
frame1.grid(row=0, column=1,padx=40)

title = CTkLabel(frame1,text="Welcome Back! \nLogin to Account",text_color="black",font=("",35,"bold"))
title.grid(row=0,column=0,sticky="nw",pady=30,padx=10)

usrname_entry = CTkEntry(frame1,text_color="white", placeholder_text="Username", fg_color="black", placeholder_text_color="white",
                         font=("",16,"bold"), width=200, corner_radius=15, height=45)
usrname_entry.grid(row=1,column=0,sticky="nwe",padx=30)

passwd_entry = CTkEntry(frame1,text_color="white",placeholder_text="Password",fg_color="black",placeholder_text_color="white",
                         font=("",16,"bold"), width=200,corner_radius=15, height=45, show="*")
passwd_entry.grid(row=2,column=0,sticky="nwe",padx=30,pady=20)

cr_acc = CTkLabel(frame1,text="Create Account!",text_color="black",cursor="hand2",font=("",15))
cr_acc.grid(row=3,column=0,sticky="w",pady=20,padx=40)

l_btn = CTkButton(frame1,text="Login",font=("",15,"bold"),height=40,width=60,fg_color="#0085FF",cursor="hand2",
                  corner_radius=15)
l_btn.grid(row=3,column=0,sticky="ne",pady=20, padx=35)

main.mainloop()