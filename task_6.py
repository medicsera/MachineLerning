import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def num_1():
    data = np.random.normal(loc=1.5, scale=0.5, size=100)

    plt.figure(figsize=(7, 5))

    plt.hist(data, bins=7, density=True, alpha=0.7, color='pink')

    # Сглаживание линии не нашел нормального в matplotlib,
    # поэтому просто для красоты использовал с библиотеки seaborn
    sns.kdeplot(data, color='red', linewidth=2)

    plt.xlabel('petal_length')
    plt.show()


#num_1()

def num_2():
    x = np.linspace(0, 100, 100)
    y = 2 * x

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(x, y)
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax_inset = fig.add_axes([0.6, 0.5, 0.1, 0.15])  

    ax_inset.plot(x, y)
    ax_inset.set_xlabel("x")
    ax_inset.set_ylabel("y")

    plt.show()


#num_2()

def num_3():
    x1 = np.linspace(0,100,100)
    y1 = 2 * x1
    
    y2 = np.linspace(0,10000,100)
    x2 = np.sqrt(y2)

    fig, axs = plt.subplots(1,2, figsize=(12,4))

    axs[0].plot(x1,y1,color="blue",linewidth=3)
    axs[0].set_xlabel("x")
    axs[0].set_ylabel("y")

    axs[1].plot(x2,y2,color="red", linestyle="dashdot", linewidth=3)
    axs[1].set_xlabel("x")
    axs[1].set_ylabel("y")

    plt.tight_layout()
    plt.show()


num_3()