
import connexion
import numpy as np
import json
from flask import jsonify


from sklearn.externals import joblib
classifier = joblib.load('Multinomial Model/model.pkl')

def PredictCaseCategory(query):
    predictions = []
    #predictions=np.array(predictions)
    for item in query:
        text = item['text']

"""the above code can be used when your category label is in vector form
 #        categoryName=['ABSENCES',
 # 'AVANTAGES',
 # "DEPART DE L'ENTREPRISE",
 # 'DONNEES PERSONNELLES',
 # 'FORMATION',
 # 'INTERIM  STAGES  EXTERNES',
 # 'MUTUELLE  PREVOYANCE',
 # 'OUTILS RH',
 # 'PAIE, REMUNERATION ET FRAIS PROFESSIONNELS',
 # 'PARCOURS PROFESSIONNEL',
 # 'TEMPS DE TRAVAIL',
 # 'THEME AUTRE']
        #category = categoryName[classifier.predict([text])[0]]"""

        category = classifier.predict([text])[0]
# def default(o):
#      if isinstance(o, np.integer): return int(o)
#      raise TypeError
        predictions.append(json.dumps({"category":(category), "text": (text)}))

    return predictions

app = connexion.FlaskApp(__name__)
app.add_api('swagger.yaml')

if __name__ == '__main__':
    app.run(port=8080, server='gevent')

print("-----------------------------------------------------------------------------------------------")
print("Case Classifier Running on http://127.0.0.1:8080/")
print("-----------------------------------------------------------------------------------------------")
