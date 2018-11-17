import matplotlib.pyplot as plt

# Create figure, 5 inches by 5 inches
plt.figure(figsize=(5,5))

labels = ["USA","China","India","Canada","Turkey"]
values = [25,10,15,40,23]

# Pop up section of the pie chart
explode = [0,0,0,0.05,0]

# Change colors in the pie chart
# You can use RGB and HEX values
colors = ["c","b","g","r","y"]

# Create pie chart
plt.pie(values, labels=labels, autopct="%.1f%%", explode=explode, colors=colors)

plt.show()
