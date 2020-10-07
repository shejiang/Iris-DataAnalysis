import pandas as pd
import matplotlib.pyplot as plt

# load data from iris.data
iris = pd.read_csv('../data/iris.data', names=['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])

setosa = iris[iris['class']=='Iris-setosa']
versicolor = iris[iris['class']=='Iris-versicolor']
virginica = iris[iris['class']=='Iris-virginica']

# Figures
fig,axs = plt.subplots(2,1)

axs[0].scatter(setosa['sepal length'],setosa['sepal width'],label='setosa')
axs[0].scatter(versicolor['sepal length'],setosa['sepal width'],label='versicolor')
axs[0].scatter(virginica['sepal length'],setosa['sepal width'],label='virginica')
axs[0].set_ylabel('width')
axs[0].set_xlabel('length')
axs[0].set_title('Distribution of sepal')
axs[0].legend()

axs[1].scatter(setosa['petal length'],setosa['petal width'],label='setosa')
axs[1].scatter(versicolor['petal length'],setosa['petal width'],label='versicolor')
axs[1].scatter(virginica['petal length'],setosa['petal width'],label='virginica')
axs[1].set_ylabel('width')
axs[1].set_xlabel('length')
axs[1].set_title('Distribution of petal')
axs[1].legend()