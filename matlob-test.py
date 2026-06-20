import matplotlib.pyplot as plt

dates = ["Mon", "Tue", "Wed", "Thu", "Fri", "No", "No", "No", "No", "No", "No", "No", "No"]
temps = [65, 68, 70, 67, 72, 67, 67, 67, 67, 67, 67, 67, 67]

plt.plot(dates, temps)
plt.title("Daily Temperature")
plt.xlabel("Dates")
plt.ylabel("Temperature")
plt.xticks(rotation=45)
plt.show()
