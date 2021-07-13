import pickle

# notice that avoid self referring
# one step further to store the data from ML forecasting

something = ['learning', 'pickle', 'module', 'is', 'funny']

type(something)

with open('pickle-test.pickle', 'wb') as f:
    pickle.dump(something, f)

# here we will see a pcikle file is created and stored

with open('pickle-test.pickle', 'rb') as f:
    new_something = pickle.load(f)

type(new_something)

print(new_something)