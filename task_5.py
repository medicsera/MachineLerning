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


#num_4()

def num_5():
    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

    width = [0.1,0.2,0.5,1.1,0.2,0.3]
    y_pos = [0,.8,1.5,3,5,6]

    plt.bar(y_pos, popularity, width=width, color="blue")
    plt.xlabel("Languages")
    plt.ylabel("Popularity")
    plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
    plt.xticks(y_pos, x)

    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

    plt.show()


#num_5()

def num_6():
    men = (22,30,33,30,26)
    women = (25,32,30,35,29)
    numbers = ('G1', 'G2', 'G3', 'G4', 'G5')
    bar_width = 0.3

    fig, ax = plt.subplots()
    index = np.arange(5)

    rect1 = plt.bar(index, men, bar_width, color="green", label="Men")
    rect2 = plt.bar(index + bar_width, women, bar_width, color="red", label="Women")

    plt.xlabel("Person")
    plt.ylabel("Scores")
    plt.title("Scores by person")
    plt.xticks(index + bar_width, numbers)
    plt.legend()

    plt.tight_layout()
    plt.show()


#num_6()

def num_7():
    languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
    popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    colors = ["blue", "orange", "green", "red", "purple", "brown"]
    explode = (0.1,0,0,0,0,0)

    plt.pie(popuratity,explode=explode, labels=languages,colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')

    plt.show()


num_7()