## TP1 Menu - Fichiers

import tkinter as tk
from tkinter import filedialog
import Date_Etudiant
import datetime

class Menu(object):

    def ReadFile(self, fn):
        FileList = []
        Etudiant_Info_List = []
        with open(fn, 'r') as f:
            if fn.find("fichetu.csv") == -1:
                print("Ce n'est pas le fichier 'fichetu.csv'. ")
            else:
                for line in f:
                    # Lire le fichier fichetu.csv
                    lineinfo = line.strip('\n').split(';')
                    FileList.append(list(lineinfo))

                    # Obtenir le list d'objets Etudiant
                    etudiant = Date_Etudiant.Etudiant(str(lineinfo[1]), str(lineinfo[0]), Date_Etudiant.Date(str(lineinfo[2])))
                    prenom_nom = str(lineinfo[1]) + " " + str(lineinfo[0])
                    adresse = etudiant.adresselec()
                    age = etudiant.age()
                    Etudiant_Info = prenom_nom + ' --- ' + adresse + ' --- ' + age
                    Etudiant_Info_List.append(Etudiant_Info)

                f.close()

                print("Lecture du fichier 'fichetu.csv': ")
                for x in FileList:
                    print(x)

                print("")
                print("")
                print("Le liste d'objets Etudiant: ")
                print("[ Format: Prenom Nom --- Adresse E-mail --- Age ]")
                for x in Etudiant_Info_List:
                    print(x)

    def WriteFile(self, fn, texte):
        f = open(fn, "a+")
        f.write(texte + '\n')
        f.close()

    def VideFile(self, fn):
        f = open(fn,"r+")
        f.truncate()
        f.close()

    def VerifyDateForm(self, datetime_str):
        try:
            datetime.datetime.strptime(datetime_str, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def WriteForm(self, string_texte):
        FormJuger = False
        string_texte = str(string_texte)
        count_1 = string_texte.count(';')
        count_2 = string_texte.count('/')
        if count_1 == 2 and count_2 == 2:
            string_texte_info = string_texte.strip(' ').split(';')
            if string_texte_info[0].isalpha() and string_texte_info[0].isupper() and string_texte_info[1].isalpha() and string_texte_info[1].isupper():
                if self.VerifyDateForm(string_texte_info[2]):
                    FormJuger = True
                else:
                    print("Erreur de format d'entrée")
            else:
                print("Erreur de format d'entrée")
        else:
            print("Erreur de format d'entrée")
        return FormJuger

    def menulist(self):
        fn = ''
        juger = True
        menu = "1. Choisir un nom de fichier", "2. Ajouter un texte", "3. Afficher le fichier complet", \
        "4. Vider le fichier", "9. Quitter le programme"

        while juger:
            print("")
            print('-------------------------------------------------------------')
            for choice in menu:
                print(choice)

            print("")
            choix = input("Veuillez saisir votre choix: ")
            print("")

            if choix == '1':
                print("Nom de fichier: ")
                print("Conseils: Le cas de test du TP1 est fichetu.csv, veuillez sélectionner ce fichier.")
                root = tk.Tk()
                root.withdraw()
                fn = filedialog.askopenfilename()
                print(fn)

            elif choix == '2':
                print("Le fichier actuellement traité est " + fn)
                print("Veuillez saisir le format suivant: ")
                print("Nom(majuscule);Prenom(majuscule);jj/mm/yy")
                print("Un cas: ZHONG;MENGTING;16/08/1992")
                texte = input("Veuillez saisir le texte que vous souhaitez ajouter: ")
                while self.WriteForm(texte) is False:
                    texte = input("Veuillez saisir le texte que vous souhaitez ajouter: ")

                self.WriteFile(fn,texte)


            elif choix == '3':
                print("Le fichier actuellement traité est " + fn)
                self.ReadFile(fn)

            elif choix == '4':
                print("Le fichier actuellement traité est " + fn)
                self.VideFile(fn)
                print("Le fichier " + fn + " a été vidé")

            elif choix == '9':
                juger = False
                print('-------------------------------------------------------------')


if __name__ == '__main__':

    ## 01
    print("Bonjour le monde !")

    ## 02
    fo = Menu()
    fo.menulist()
