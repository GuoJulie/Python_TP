import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from PIL import Image
import sys

class Numpy_Part():

    # 1.Créer un tableau de dimension 3
    def tableau_dim3(self):
        rand = np.random.rand(4, 3, 2)
        print(rand)
        print('ndim:', rand.ndim, "\n",
              'shape:', rand.shape, "\n",
              'size:', rand.size, "\n",
              'dtype:', rand.dtype, "\n",
              'itemsize:', rand.itemsize, "\n",
              'data:', rand.data)

    # 2 + 3.Créer 2 matrices 3x3 et les calculer
    def matrice_calcule(self):
        matrice_1 = np.arange(9).reshape(3,3)
        matrice_2 = np.arange(2,11).reshape(3,3)

        # 2.
        print("Matrice_1:")
        print(matrice_1)
        print("****************************************")

        print("Matrice_2:")
        print(matrice_2)
        print("****************************************")

        print("Le produit des 2 matrices(*):")
        print(matrice_1 * matrice_2)
        print("****************************************")

        print("Le produit des 2 matrices(dot):")
        print(matrice_1.dot(matrice_2))
        print("****************************************")

        print("Transposer Matrice_1:")
        print(np.transpose(matrice_1))
        print("----------------------------------------------------")

        # 3.
        print("Déterminant du Matrice_1:")
        print(np.linalg.det(matrice_1))
        print("****************************************")

        print("Résoudre un système d’équations linéaires:")
        # print(np.linalg.inv(matrice_1))
        print("****************************************")

        print("Les valeurs du Matrice_1:")
        print(np.linalg.eigvals(matrice_1))
        print("****************************************")

        print("Les vecteurs propres du Matrice_1:")
        print(np.linalg.eigh(matrice_1))


class Scipy_Part():

    # 4. Approcher un ensemble de points par une courbe
    def point_courbe(self):
        def func(x, a, b, c):
            return a * np.exp(-b * x) + c

        xdata = np.linspace(0, 4, 20)
        y = func(xdata, 2.5, 1.3, 0.5)

        y_bruit = 0.2 * np.random.normal(size=xdata.size)
        ydata = y + y_bruit
        plt.plot(xdata, ydata, 'b-', label='données')
        popt, pcov = curve_fit(func, xdata, ydata)

        plt.plot(xdata, func(xdata, *popt), 'r-', label='approche: a=%.3f, b=%.3f, c=%.3f' % tuple(popt))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()

    # 5. Lire une image jpeg et afficher l’image originale et réduite en taille.
    def Image_Traite(self):
        imgfile = 'images.jpg'
        try:
            img = Image.open(imgfile)
        except IOError:
            print('Erreur sur ouverture du ' + imgfile)
            sys.exit(1)

        print("# Affichage l’image originale <formule + taille + mode>: ")
        print(img.format, img.size, img.mode)
        img.show()
        imgorien = np.array(img)
        plt.imshow(imgorien)

        img = img.resize((125, 100), Image.ANTIALIAS)
        print("# Affichage l’image réduit <formule + taille + mode>: ")
        print(img.format, img.size, img.mode)
        img.show()
        imgorien = np.array(img)
        plt.imshow(imgorien)



if __name__ == "__main__":

    numpt_test = Numpy_Part()
    scipy_test = Scipy_Part()

    # 1. Créer un tableau de dimension 3 avec un shape de (4, 3, 2) remplit avec des nombres aléatoires.
    numpt_test.tableau_dim3()
    print("----------------------------------------------------")

    # 2. Créer 2 matrices 3x3 initialisées avec les entiers de 0 à 8 pour la 1e et de 2 à 10 pour la 2e
    # puis calculer le produit des 2 (différence entre * et dot).
    # Transposer une matrice.
    # 3. Calculer le déterminant et l’inverse  d’une matrice.
    # Résoudre un système d’équations linéaires.
    # Calculer les valeurs et vecteurs propres d’une matrice.
    numpt_test.matrice_calcule()
    print("----------------------------------------------------")

    # 4. Approcher un ensemble de points par une courbe
    scipy_test.point_courbe()

    # 5.Lire une image jpeg et afficher l’image originale et réduite en taille.
    scipy_test.Image_Traite()
