import matplotlib.pyplot as plt
from database import get_rows  # whatever function returns your rows

def show_charts():
    rows = get_rows()
    dates = list()
    temps = list()

    for row in rows:
        dates.append(row[0])
        temps.append(row[2])

    plt.plot(dates,temps)
    plt.show()