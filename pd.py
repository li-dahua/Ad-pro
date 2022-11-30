import pandas as pd

import matplotlib.pyplot as plt

titanic = pd,read.csv("https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv")
pd.set_option('precision',2)

plt.hist(titanic.age)
plt.axvline(titanic.age.mean(), color= 'k', linestyle= 'dashed', linewidth=1)
plt.title('age of passenger on titianic')
plt.ylabel('count')
plt.xlabel("age (in years)")
plt.show()