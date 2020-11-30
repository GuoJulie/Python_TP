import random
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


# 1. Générer des nombres aléatoires
def Random_List(start, stop, length):
    if length >= 0:
        length = int(length)

    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

# 2. Afficher la courbe de ces données dans une fenêtre matplotlib
def Courbe(list_x, list_1, list_2):
    plt.plot(list_x, list_1, label='Courbe_rouge', color='red')
    plt.plot(list_x, list_2, label='Courbe_blue', color='blue')

    # Des flèches
    plt.annotate('(2,4)', xy=(2, 4), xytext=(3, 150), arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))

    # Les noms des axes
    plt.title(u'Courbe')
    plt.xlabel(u'test_x')
    plt.ylabel(u'test_y')

    # La légende
    plt.legend(loc='best')

    plt.show()


# 3. Afficher un histogramme de ces données dans une fenêtre matplotlib
def Histogramme(list_x, list_1, list_2):
    plt.bar(list_x, list_1, facecolor='red', edgecolor='white')
    plt.bar(list_x, list_2, facecolor='blue', edgecolor='white')

    # Les noms des axes
    plt.title(u'Histogramme')
    plt.xlabel(u'test_x')
    plt.ylabel(u'test_y')

    # La légende
    plt.legend(loc='best')

    plt.show()


# 4. Afficher un camembert de ces données dans une fenêtre matplotlib
def Camembert():
    data = [1, 2, 3]
    text = ['A', 'B', 'C']
    plt.pie(data, labels=text, colors=['red', 'green', 'yellow'], explode=[0, 0.4, 0],
             autopct='%1.1f%%', startangle=90, pctdistance=0.7, labeldistance=0.4, shadow=True)

    # Les noms des axes
    plt.title(u'Camembert')

    # La légende
    plt.legend()

    plt.show()


# 5. Afficher une surface 2D dans un espace 3D (mesh)
def Espace_3D():
    fig = plt.figure("Espace_3D")
    ax = Axes3D(fig)
    ax.set_title("Espace_3D")
    X = np.arange(-12, 12, 0.5)
    Y = np.arange(-12, 12, 0.5)
    X, Y = np.meshgrid(X, Y)
    Z = np.sin(np.sqrt(X ** 2 + Y ** 2))
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.hot)
    ax.contourf(X, Y, Z, zdir="z", offset=-2, cmap=plt.cm.hot)
    ax.set_zlim(-2, 2)
    fig.colorbar(surf, shrink=0.6, aspect=8)
    plt.show()



if __name__ == '__main__':

    # Générer un tableau en indice
    list_x = []
    for i in range(20):
        list_x.append(i)

    list_1 = Random_List(1,100,20)

    list_2 = []
    for i in list_x:
        list_2.append(i**2)

    Courbe(list_x, list_1, list_2)
    # Histogramme(list_x, list_1, list_2)
    # Camembert()
    # Espace_3D()

