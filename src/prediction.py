import pickle
import numpy as np

with open("model.pkl", 'rb') as file:
    pickle_model = pickle.load(file)
    file.close()

with open('binarizer.pkl', 'rb') as file:
    pickle_bin = pickle.load(file)
    file.close()

def predict_lines(desc):
    if not desc or type(desc) != str:
        return "Invalid request. Please provide a valid input."

    prediction = pickle_model.predict([desc.lower()])
    prediction_bin = np.round(prediction).astype(int)
    prediction_labels = pickle_bin.inverse_transform(prediction_bin)

    if (len(prediction_labels) == 0):
        return "No predictions"
    else:
        return prediction_labels[0]
