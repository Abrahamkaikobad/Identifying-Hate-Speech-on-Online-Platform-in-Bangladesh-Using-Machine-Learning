import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack
from .cleaning_text import clean_bangla_text, clean_banglish_text  # Add a dot before 'cleaning_text'


class Prediction:
    def __init__(self):
        #self.model_path = "src/model/random_forest_model.sav"
        self.model_path = "src/model/rf.sav"
        self.bangla_vector = 'src/model/tfidf_vectorizer_bangla.sav'
        self.banglish_vector = 'src/model/tfidf_vectorizer_banglish.sav'
        self.loaded_model = pickle.load(open(self.model_path, 'rb'))
        self.vectoriser1 = pickle.load(open(self.bangla_vector, 'rb'))
        self.vectoriser2 = pickle.load(open(self.banglish_vector, 'rb'))

    def get_prediction(self, user_input_bangla, user_input_banglish):
        # Clean the input data
        cleaned_bangla = clean_bangla_text(user_input_bangla)
        cleaned_banglish =clean_banglish_text(user_input_banglish)

        # Transform the cleaned input data using the trained vectorizers
        vectorized_input_bangla = self.vectoriser1.transform([cleaned_bangla])
        vectorized_input_banglish = self.vectoriser2.transform([cleaned_banglish])
        #print(vectorized_input_bangla)
        # Concatenate the features
        X_input = hstack([vectorized_input_bangla, vectorized_input_banglish])

        # Now you can predict using your model (e.g., random_forest_classifier)
        result = self.loaded_model.predict(X_input)
        print(result)

        if result == 0:
            return "Neutral"
        elif result == 1:
            return "Personal"
        elif result == 2:
            return "Geo Political"
        elif result == 3:
            return "Religious"
        else:
            return "Political"
        

# input_bn = "রাহীম কুত্তার বাচ্চা"
# input_banglish = "rahim kuttar baccha"
# obj = Prediction()
# output = obj.get_prediction(input_bn, input_banglish)
# print(output)


