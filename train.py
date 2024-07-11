from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pickle
import os,sys

# Read the file index
index = sys.argv[1]
#print(index)

trainingData_path = "/Users/harris/MLGame/Maze_Car/log/data_" + index


# x:data, y:action
data = list()
action = list()

for file in os.listdir(trainingData_path):
    with open(os.path.join(trainingData_path, file), "rb") as f:
        loaded_data = pickle.load(f)
        for Data in loaded_data:
            data.append(Data[:4])
            action.append(Data[4:]) ##3 is for frame consideration
  
            
# split data
x_train = data
y_train = action

#x_train, x_test, y_train, y_test = train_test_split(
#    data, action, test_size = 0.5
#)

# model train
model = KNeighborsClassifier(n_neighbors = 1)
model.fit(x_train, y_train)

# store model

save_path = "/Users/harris/MLGame/Maze_Car/model/K" + index + "model.pickle"
with open(save_path, "wb") as file:
    pickle.dump(model, file)
    
#modle = pickle.load(file)
#y = model.predict(x)


