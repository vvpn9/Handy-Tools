import joblib

# notice that we do not need sklearn.externals anymore, just import the joblib

# easy, isnt it?

another_thing = ['learning', 'joblib', 'is', 'interesting']

joblib.dump(another_thing, 'another_thing.m')

new_another_thing = joblib.load('another_thing.m')

print(new_another_thing)
