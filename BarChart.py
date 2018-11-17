import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,5))

names=["Peter","Matt","Frank","Jessica"]
scores =[89,78,93,57]
scores2 = [95,95,87,78]
positions=[0,1,2,3]
positions2= [0.3,1.3,2.3,3.3]
positions3=[0.15,1.15,2.15,3.15]

plt.bar(positions, scores, width=0.3, color="g")
plt.bar(positions2, scores2, width=0.3, color="b")
plt.xticks(positions3, names)

plt.title("Latest Test Scores")
plt.show()