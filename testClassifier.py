#Category classification using scilearn  tfidf vecotorization
import sklearn

import numpy as np

from glob import glob

from sklearn import datasets

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.linear_model import SGDClassifier

from sklearn import metrics

from sklearn.pipeline import Pipeline

from sklearn.model_selection import GridSearchCV





def pathfinder(i):

    path_string = i.replace('\\','/').replace('C:/Users/asojasingarayar/CaseClassification/CaseClassifier/document/','')

    path_string = path_string.strip('/')

    return path_string
#print(pathfinder("C:/Users/asojasingarayar/CaseClassification/CaseClassifier/document\\Absence\\ "))

# Get paths to labelled data

rawFolderPaths = glob("C:/Users/asojasingarayar/CaseClassification/CaseClassifier/document/*/")

print ('\nGathering labelled categories...\n')

categories = []


# Extract the folder paths, reduce down to the label and append to the categories list

for i in rawFolderPaths:

    category = pathfinder(i)

    categories.append(category)
print ('\n-----------------------------------------------------------Case Category-----------------------------------------------------------\n')
print (categories)

# Load the data

print ('\nLoading the dataset...\n')

docs_to_train = sklearn.datasets.load_files("document",

                                            description=None, categories=categories, load_content=True,

                                            encoding='utf-8', shuffle=True, random_state=42)



# Split the dataset into training and testing sets

print ('\nBuilding out hold-out test sample...\n')

X_train, X_test, y_train, y_test = train_test_split(docs_to_train.data, docs_to_train.target, test_size=0.3)





# Construct the classifier pipeline using a SGDClassifier algorithm

print ('\nApplying the classifier...\n')

text_clf = Pipeline([('vect', CountVectorizer(stop_words='english')),

                     ('tfidf', TfidfTransformer(use_idf=True)),

                     ('clf', SGDClassifier(loss='hinge', penalty='l2',

                                           alpha=1e-3, random_state=42, verbose=1)),

])



# Fit the model to the training data
print("\nTraining a model it will take few minutes......\n")
text_clf.fit(X_train, y_train)



# Run the test data into the model

predicted = text_clf.predict(X_test)



# Calculate mean accuracy of predictions
print("\nCalculating Prediction...\n")
print (np.mean(predicted == y_test))



# Generate labelled performance metrics
print("\n-----------------------------------------------------------PERFORMENCE MATRIX-----------------------------------------------------------\n")
print(metrics.classification_report(y_test, predicted,

    target_names=docs_to_train.target_names))

#grid search

parameters = {'vect__ngram_range': [(1, 1), (1, 2)],
              'tfidf__use_idf': (True, False),
              'clf__alpha': (1e-2, 1e-3),
}

gs_clf = GridSearchCV(text_clf, parameters, cv=2, iid=False, n_jobs=-1)

#grid search work like a model
gs_clf = gs_clf.fit(docs_to_train.data[:10], docs_to_train.target[:10])

# #prediction with example text
# docs_to_train.target_names[gs_clf.predict(['Pour un enfant de 10 ans il n y a pas de versement en juillet et aout ?'])[0]]
# #docs_to_train.target_names[gs_clf.predict(['Où trouve t on le nom de notre juriste dans la base documentaire ?'])[0]]
#
# gs_clf.best_score_
#
# for param_name in sorted(parameters.keys()):
#     print("%s: %r" % (param_name, gs_clf.best_params_[param_name]))

docs_to_train.target_names[gs_clf.predict(['Jai créé expression de besoin AJ000049. Elle a bien le statut "diffusée"
mais je n'ai pas eu de confirmation par mail et les ETT ont pas recu expression de besoin'])[0]]
docs_to_train.target_names[gs_clf.predict(['Est ce que je peux prétendre au prêt 1% logement, et si oui comment je dois y prendre.'])[0]]
docs_to_train.target_names[gs_clf.predict(['Quels sont les congés relevant exclusivement de la SG, dans le cadre une maternité?"])[0]]
docs_to_train.target_names[gs_clf.predict(['Pour un enfant de 10 ans il n y a pas de versement en juillet et aout ?'])[0]]
#docs_to_train.target_names[gs_clf.predict(['Où trouve t on le nom de notre juriste dans la base documentaire ?'])[0]]
