import hashlib
import random
from tkinter import *
from tkinter import messagebox
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


# 1. Fonction de connexion
def Login():
    id = entry_id.get()
    pwd = entry_pwd.get()
    state = 0

    if id == "" or pwd == "":
        messagebox.showerror("Erreur", "L'entrée est vide, veuillez réessayer.")
    else:
        dir_path = os.getcwd()
        file_path = dir_path + '\\' + "Id_Pwd_Salage_Chiffrersha512.txt"
        if os.path.exists(file_path):
            filesize = os.path.getsize("Id_Pwd_Salage_Chiffrersha512.txt")
            if filesize != 0:
                with open("Id_Pwd_Salage_Chiffrersha512.txt", 'r') as f:
                    for line in f:
                        id_ver = line.strip('\n').split()[0]
                        pwd_ver = line.strip('\n').split()[1]

                        if id == id_ver and pwd == pwd_ver:
                            state = 1
                f.close()

        if state == 1:
            messagebox.showinfo("Succès", "Connexion avec succès.")
        else:
            messagebox.showerror("Erreur", "Échec de la connexion. L'utilisateur n'existe pas ou le mot de passe est incorrect, veuillez réessayer.")


# 2. Fonction d'enregistrement
def Register():
    id = entry_id.get()
    pwd = entry_pwd.get()

    state = 0

    if id == "" or pwd == "":
        messagebox.showerror("Erreur", "L'entrée est vide, veuillez réessayer.")
    else:
        dir_path = os.getcwd()
        file_path = dir_path + '\\' + "Id_Pwd_Salage_Chiffrersha512.txt"
        if not os.path.exists(file_path):
            f = open("Id_Pwd_Salage_Chiffrersha512.txt", "w")
            f.close()

        with open("Id_Pwd_Salage_Chiffrersha512.txt", 'r') as f:
            filesize = os.path.getsize("Id_Pwd_Salage_Chiffrersha512.txt")
            if filesize != 0:
                for line in f:
                    id_ver = line.strip('\n').split()[0]
                    pwd_ver = line.strip('\n').split()[1]

                    if id == id_ver:
                        state = 1
        f.close()

        if state == 1:
            messagebox.showwarning("Info", "Échec de l'enregistrement. L'utilisateur existe déjà.")
        else:
            f = open("Id_Pwd_Salage_Chiffrersha512.txt", "a+")
            pwd_chiffrer_sha512 = Chiffrer_sha512(pwd) # Chiffrer avec sha512
            chaine_id_salage = Salage(id)
            new_info_1 = id + "    " + pwd + "    " + chaine_id_salage + "    " + pwd_chiffrer_sha512
            f.write(new_info_1 + '\n')  # Écrire du mot de passe chiffré avec sha512 dans un fichier « Id_Pwd_Salage_Chiffrersha512.txt »
            f.close()
            messagebox.showinfo("Succès", "Enregistrement avec succès.")


# salage/salt: renforcer le système avec une chaîne comprenant le login et une partie fixe.
def Salage(id):
    salage = ''.join([chr(random.randint(48, 122)) for i in range(20)])     # salt
    chaine_id_salage = id + salage
    return chaine_id_salage


# 3. Fonction de cryptage du mot de passe avec sha512
def Chiffrer_sha512(pwd):
    return hashlib.sha512(pwd.encode()).hexdigest()


# 3. Fonction de cryptage du fichier
def Chiffrer_AES256():
    filename = entry_chiffrer.get()
    pwd = entry_pwd.get()

    try:
        # Chiffrer avec l'algorithme AES256
        key = pad(pwd.encode('utf-8'), AES.block_size * 2, style='pkcs7')
        cipher = AES.new(key, AES.MODE_EAX)
        with open(filename, mode='rb') as f:
            data = f.read()
            ciphertext, tag = cipher.encrypt_and_digest(data)
            f.close()
        file_out = open("Chiffrer_AES256_" + filename, "wb")
        [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
        messagebox.showinfo("Succès", "Chiffrer avec succès!")
    except Exception as e:
        messagebox.showerror("Error", e)

# 4. Fonction de décryptage du fichier
def Dechiffrer_AES256():
    filename = entry_dechiffrer.get()
    pwd = entry_pwd.get()

    try:
        key = pad(pwd.encode('utf-8'), AES.block_size * 2, style='pkcs7')
        with open(filename, "rb") as file_in:
            nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]
            cipher = AES.new(key, AES.MODE_EAX, nonce)
            data = cipher.decrypt_and_verify(ciphertext, tag)
            file_in.close()
        with open("Dechiffrer_AES256_" + filename, "w") as f:
            f.write(str(data, encoding="utf-8"))
            f.close()
    except Exception as e:
        messagebox.showerror("Error", e)
    else:
        messagebox.showinfo("Succès", "Déchiffrer avec succès")




fenetre = Tk()
fenetre.title('Chiffrement')
sw = fenetre.winfo_screenwidth()
sh = fenetre.winfo_screenheight()
ww = 390
wh = 450
x = (sw - ww) / 2
y = (sh - wh) / 2
fenetre.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

lab0 = Label(fenetre, text = "Bienvenue", font=("Times New Roman", 30, "bold"), fg="red")

frame_label_1 = Frame(fenetre)
frame_label_1.grid(row=1, column=0, sticky='w')
lab_id = Label(frame_label_1, text = 'Identifiant ou Adresse de messagerie')
entry_id = Entry(frame_label_1, font=(20), bg=('white'))
lab_pwd = Label(frame_label_1, text='Mot de passe')
entry_pwd = Entry(frame_label_1, font=(20), bg=('white'),show='*')
lab1 = Label(frame_label_1, text="", font=(50))

lab0.grid(column=0, row=0, ipadx=80, ipady=10)
lab_id.grid(column=0, row=2, sticky='w')
entry_id.grid(column=0, row=3, sticky='w', ipadx=110, ipady=10)
lab_pwd.grid(column=0, row=4, sticky='w')
entry_pwd.grid(column=0, row=5, sticky='w', ipadx=110, ipady=10)
lab1.grid(column=0, row=6, ipadx=80, ipady=1)

frame_button_1 = Frame(fenetre)
frame_button_1.grid(row=2, column=0, sticky='w')
B_register = Button(frame_button_1, text='S\'enregister', width=26, height=2, bg=('lightblue'), command=Register).grid(column=0, row=0)
B_login = Button(frame_button_1, text='Identification', width=26,height=2, bg=('lightblue'), command=Login).grid(column=1, row=0)

frame_label_2 = Frame(fenetre)
frame_label_2.grid(row=3, column=0, sticky='w')

lab2 = Label(frame_label_2, text="", font=(50))
lab_chiffrer = Label(frame_label_2, text = 'Nom de fichier à chiffrer')
entry_chiffrer = Entry(frame_label_2, font=(20), bg=('white'))
B_encrypt = Button(frame_label_2, text='Chiffrer ', width=13, height=2, bg=('lightblue'), command=Chiffrer_AES256).grid(column=1, row=2)

lab_dechiffrer = Label(frame_label_2, text='Nom de fichier à déchiffrer')
entry_dechiffrer = Entry(frame_label_2, font=(20), bg=('white'))
B_decrypt = Button(frame_label_2, text='Déchiffrer ', width=13, height=2, bg=('lightblue'), command=Dechiffrer_AES256).grid(column=1, row=4)

lab2.grid(column=0, row=0, ipadx=80, ipady=1)
lab_chiffrer.grid(column=0, row=1, sticky='w')
entry_chiffrer.grid(column=0, row=2, sticky='w', ipadx=60, ipady=10)
lab_dechiffrer.grid(column=0, row=3, sticky='w')
entry_dechiffrer.grid(column=0, row=4, sticky='w', ipadx=60, ipady=10)

fenetre.mainloop()
