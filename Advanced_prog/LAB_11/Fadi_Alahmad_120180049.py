# CSE314- Lab 11
#
# Topic: Object Serialization
# Author : Fadi Alahmad 120180049
# Date : 19/01/2021
# Question 1:

import pickle
import json

test_Data_Pickle = ["FAdi", "ALahmad", 'ALomar', "FAdy200"]

with open('PickleTest', 'wb') as f:
    pickle.dump(test_Data_Pickle, f)

with open('PickleTest', 'rb') as f:
    pickle_Load = pickle.load(f)
    print(pickle_Load)
    if pickle_Load == test_Data_Pickle:
        print("Serialization with Pickle done correctly")

# Question 2:


test_Data_Json = {"FAdi": "Alahmad", "Alomar": "FAdy200"}

with open('JsonTest', 'w') as f:
    json.dump(test_Data_Json, f)

with open('JsonTest', 'r') as f:
    json_Load = json.load(f)
    print(json_Load)
    if pickle_Load == test_Data_Pickle:
        print("Serialization with JSON done correctly")



import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,1000)
fig, axes = plt.subplots()
axes.plot(x,x)
axt = axes.twinx()
axt.plot(x,x**2)
plt.show()
