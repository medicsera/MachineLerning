import matplotlib.pyplot as plt
import numpy as np


def num_1():
    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [22.2, 17.5, 8.8, 8, 7.7, 6.7]
    x_pos = [i for i, _ in enumerate(x)]

    plt.bar(x_pos, popularity, color='blue')
    plt.xlabel("Languages")
    plt.ylabel("Popularity")
    plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")

    plt.xticks(x_pos, x)
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

    plt.show()


#num_1()

def num_2():
    x = ['Java', 'Python', 'PHP', 'JS', 'C#', 'C++']
    popularity = [22.2, 17.5, 8.8, 8, 7.7, 6.7]
    x_pos = [i for i, _ in enumerate(x)]

    plt.barh(x_pos, popularity, color='green')
    plt.xlabel("Popularity")
    plt.ylabel("Languages")
    plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
    plt.yticks(x_pos, x)

    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

    plt.show()


#num_2()  

def num_3():
    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [22.2, 17.5, 8.8, 8, 7.7, 6.7]
    x_pos = [i for i, _ in enumerate(x)]

    plt.bar(x_pos, popularity, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])
    plt.xlabel("Languages")
    plt.ylabel("Popularity")
    plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
    plt.xticks(x_pos, x)

    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

    plt.show()


#num_3()

def num_4():
    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    x_pos = [i for i, _ in enumerate(x)]

    fig, ax = plt.subplots()
    rect = ax.bar(x_pos, popularity, color="blue")
    
    plt.xlabel("Languages")
    plt.ylabel("Popularity")
    plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
    plt.xticks(x_pos, x)

    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

    def label(rects):
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2.,
                    1.05*height,
                    '%f' % float(height),
                    ha="center", 
                    va="bottom")


    label(rect)

    plt.show()


num_4()