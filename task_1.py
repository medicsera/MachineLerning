import matplotlib.pyplot as plt
import datetime as dt
from matplotlib.dates import date2num

def num_1():
    x = range(1,50)
    y = [value * 3 for value in x]

    plt.title("Draw a line")
    plt.xlabel("x - axis")
    plt.ylabel("y - axis")

    plt.plot(x,y)
    plt.show()


#num_1()

def num_2():

    x = [0,20,30]
    
    y1 = [20,40,10]
    y2 = [40,10,30]

    plt.title("Two or more lines with different widths and colors with suitable legends")
    plt.xlabel("x - axis")
    plt.ylabel("y - axis")

    plt.plot(x,y1, color="blue", linewidth="3", label='line1-width-3')
    plt.plot(x,y2, color="red", linewidth="5", label='line2-width-5')

    plt.legend()
    plt.show()


#num_2()

def num_3():

    x = [0,20,30]
    
    y1 = [20,40,10]
    y2 = [40,10,30]

    plt.title("Plot with two or more lines with different styles")
    plt.xlabel("x - axis")
    plt.ylabel("y - axis")

    plt.plot(x,y1, color="blue",linestyle="dotted", linewidth="3", label='line1-dotted')
    plt.plot(x,y2, color="red", linestyle="dashed", linewidth="5", label='line2-dashed')

    plt.legend()
    plt.show()


#num_3()

def num_4():

    x = [1,4,5,6,7]
    
    y = [2,6,3,6,3]

    plt.title("Display marker")
    plt.xlabel("x - axis")
    plt.ylabel("y - axis")

    plt.plot(x,y, color="red",linestyle="dashdot", linewidth="2", marker="o", markerfacecolor="blue", markersize=12)

    plt.ylim(1,8)
    plt.xlim(1,8)

    plt.show()


#num_4()

def num_5():

    x1 = [2,3,5,6,8]
    x2 = [3,4,6,7,9]
    
    y1 = [1,5,10,18,20]
    y2 = [2,6,11,20,22]

    plt.axis([0,10,0,30])

    plt.plot(x1,y1, "b*",x2,y2,"ro")

    plt.show()


#num_5()

def num_6():

    date = [(dt.datetime.strptime('2016-10-03','%Y-%m-%d'),772.55),
            (dt.datetime.strptime('2016-10-04','%Y-%m-%d'),776.42),
            (dt.datetime.strptime('2016-10-05','%Y-%m-%d'),776.46),
            (dt.datetime.strptime('2016-10-06','%Y-%m-%d'),776.85),
            (dt.datetime.strptime('2016-10-07','%Y-%m-%d'),775.10)]
    
    x = [date2num(date) for (date,value) in date]
    y = [value for (date,value) in date]

    fig = plt.figure()

    grath = fig.add_subplot(111)

    grath.plot(x,y,'r-o')

    grath.set_xticks(x)
    grath.set_xticklabels([date.strftime('%Y-%m-%d') for (date, value) in date])

    plt.title("Closing stock value of Alphabet Inc.")
    plt.xlabel("Date")
    plt.ylabel("Closing Value")

    plt.minorticks_on()

    plt.grid(which="major", linestyle="-", linewidth="0.5", color="red")
    plt.grid(which="minor", linestyle=":", linewidth="0.5", color="black")

    plt.show()


num_6()