import pandas as pd
import numpy as np
# Load Training data
numbers = []
from firebase import firebase
    # firebase = firebase.FirebaseApplication('https://tempdeepblue.firebaseio.com/', None)
firebase = firebase.FirebaseApplication('https://svsfirebaseproject-6cc9f.firebaseio.com/', None)
one = firebase.get('/message', 'Symptom1')
two=firebase.get('/message', 'Symptom2')
three=firebase.get('/message', 'Symptom3')
four=firebase.get('/message', 'Symptom4')
five=firebase.get('/message', 'Symptom5')
n=2
for i in range(n):

    df = pd.read_csv('data/clean/Training.csv')

    df.head()

    X = df.iloc[:, :-1]
    y = df['prognosis']

    # Train, Test split
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=20)

    # Random Forest Classifier
    from sklearn.ensemble import RandomForestClassifier

    rf_clf = RandomForestClassifier()

    rf_clf.fit(X_train, y_train)

#     print("Accuracy on split test: ", rf_clf.score(X_test,y_test))

    # Load real test data
    df_test = pd.read_csv('data/clean/Testing.csv')

    X_acutal_test = df_test.iloc[:, :-1]
    y_actual_test = df_test['prognosis']


#     print("Accuracy on acutal test: ", rf_clf.score(X_acutal_test, y_actual_test))

    symptoms_dict = {}

    for index, symptom in enumerate(X):
        symptoms_dict[symptom] = index

    symptoms_dict

    input_vector = np.zeros(len(symptoms_dict))
#     print("running1st file")
   
#     five=firebase.get('/message', 'Symptom1')
    # six='none'


    #     input = int(input("Enter number: "))
    input_vector[[symptoms_dict[one], symptoms_dict[two],symptoms_dict[three],symptoms_dict[four],symptoms_dict[five]]] = 1

    score=rf_clf.predict_proba([input_vector])

    k=rf_clf.predict([input_vector])[0]
#     score= rf_clf.score(X_test,y_test)
    numbers.append(k)
    
    print(k)
#     print(score)
    
print(numbers)


maximum=max(numbers,key=lambda x: numbers.count(x))
print("maximum is",maximum)
# print(bincount(max(numbers,key=lambda x: numbers.count(x))))
print(max(set(numbers), key = numbers.count))

itemList = numbers

counter = {}
maxItemCount = 0
for item in itemList:
    try:
        # Referencing this will cause a KeyError exception
        # if it doesn't already exist
        counter[item]
        # ... meaning if we get this far it didn't happen so
        # we'll increment
        counter[item] += 1
    except KeyError:
        # If we got a KeyError we need to create the
        # dictionary key
        counter[item] = 1

    # Keep overwriting maxItemCount with the latest number,
    # if it's higher than the existing itemCount
    if counter[item] > maxItemCount:
        maxItemCount = counter[item]
        mostPopularItem = item

print (mostPopularItem,maxItemCount)
probablity=maxItemCount/n
prob=(probablity*100)

result4=firebase.put('/message',"disease",maximum)
result5=firebase.put("/message","prob",prob)

# diseasese


if maximum == 'Fungal infection':
    tablet = 'Fungal 150 MG Tablet'
if maximum == 'Allergy':
    tablet = 'Cetrizine'
if maximum == 'GERD':
    tablet = 'H-2-receptors blockers'
if maximum == 'Chronic cholestasis':
    tablet = 'corticosteroids'
if maximum == 'Drug Reaction':
    tablet = 'antihistamines'
if maximum == 'Peptic ulcer diseae':
    tablet = 'ranitidine'
if maximum == 'AIDS':
    tablet = 'antiretroviral therapy'
if maximum == 'Diabetes':
    tablet = 'metformin'
if maximum == 'Gastroenteritis':
    tablet = 'ranitidine'
if maximum == 'Bronchial Asthma':
    tablet = ' Flovent'
if maximum == 'Hypertension':
    tablet = 'Diuretics'
if maximum == 'Migraine':
    tablet = 'sumatriptan'
if maximum == 'Paralysis(brain hemorrhage)':
    tablet = 'Pongamia pinnata'
if maximum == 'Jaundice':
    tablet = 'N-acetylcysteine'
if maximum == 'Malaria':
    tablet = 'Mefloquine'
if maximum == 'Chicken pox':
    tablet = 'acyclovir'
if maximum == 'Dengue':
    tablet = 'Acetaminophen'
if maximum == '(vertigo) Paroymsal  Positional Vertigo':
    tablet = 'benign paraoxymal'
if maximum == 'Acne':
    tablet = 'azidothymidine'
if maximum == 'Alcoholic Hepatitis':
    tablet = 'Liv Compound'
if maximum == 'Arthritis':
    tablet = 'Arnicare'
if maximum == 'Cervical spondylosis':
    tablet = 'Spondylon'
if maximum == 'Common  cold':
    tablet = 'Benadryl'
if maximum == 'Dimorphic hemmorhoids(piles)':
    tablet = 'Kultab'
if maximum == 'Heart Attack':
    tablet = 'amitriptyline'
if maximum == 'Hepatitis A':
    tablet = 'entavir'
if maximum == 'Hepatitis B':
    tablet = 'Liv.52'
if maximum == 'Hepatitis C':
    tablet = 'Sovaldi'
if maximum == 'Hepatitis D':
    tablet = 'Ribavirin'
if maximum == 'Hepatitis E':
    tablet = 'Sofasbuvir'
if maximum == 'Hyperthyroidism':
    tablet = 'Methimazole'
if maximum == 'Hypoglycemia':
    tablet = 'BD Glucose'
if maximum == 'Hypertension':
    tablet = 'losar-H'
if maximum == 'impetigo':
    tablet = 'cloxacillin'
if maximum == 'Jaundice':
    tablet = 'Livful-DS'
else:
    tablet='Penicillin'
#     print("heelo")
        
# cure(maximum)
result6=firebase.put("/message","cure",tablet)
#location
if maximum == 'Fungal infection':
#     tablet = 'Fungal 150 MG Tablet'
    lat=19.045927
    lon=73.020651
if maximum == 'Allergy':
#     tablet = 'Cetrizine'
    lat=19.159023
    lon=72.997271
if maximum == 'GERD':
#     tablet = 'H-2-receptors blockers'
    lat=19.159023
    lon=72.997271
if maximum == 'Chronic cholestasis':
#     tablet = 'corticosteroids'
    lat=19.159023
    lon=72.997271
if maximum == 'Drug Reaction':
#     tablet = 'antihistamines'
    lat=19.159023
    lon=72.997271
if maximum == 'Peptic ulcer diseae':
#     tablet = 'ranitidine'
    lat=19.159023
    lon=72.997271
if maximum == 'AIDS':
    tablet = 'antiretroviral therapy'
if maximum == 'Diabetes':
    tablet = 'metformin'
if maximum == 'Gastroenteritis':
    tablet = 'ranitidine'
if maximum == 'Bronchial Asthma':
    tablet = ' Flovent'
if maximum == 'Hypertension':
    tablet = 'Diuretics'
if maximum == 'Migraine':
    tablet = 'sumatriptan'
if maximum == 'Paralysis(brain hemorrhage)':
    tablet = 'Pongamia pinnata'
if maximum == 'Jaundice':
    tablet = 'N-acetylcysteine'
if maximum == 'Malaria':
    tablet = 'Mefloquine'
if maximum == 'Chicken pox':
    tablet = 'acyclovir'
if maximum == 'Dengue':
    tablet = 'Acetaminophen'
if maximum == '(vertigo) Paroymsal  Positional Vertigo':
    tablet = 'benign paraoxymal'
if maximum == 'Acne':
    tablet = 'azidothymidine'
if maximum == 'Alcoholic Hepatitis':
    tablet = 'Liv Compound'
if maximum == 'Arthritis':
    tablet = 'Arnicare'
if maximum == 'Cervical spondylosis':
    tablet = 'Spondylon'
if maximum == 'Common  cold':
    tablet = 'Benadryl'
if maximum == 'Dimorphic hemmorhoids(piles)':
    tablet = 'Kultab'
if maximum == 'Heart Attack':
    tablet = 'amitriptyline'
if maximum == 'Hepatitis A':
    tablet = 'entavir'
if maximum == 'Hepatitis B':
    tablet = 'Liv.52'
if maximum == 'Hepatitis C':
    tablet = 'Sovaldi'
if maximum == 'Hepatitis D':
    tablet = 'Ribavirin'
if maximum == 'Hepatitis E':
    tablet = 'Sofasbuvir'
if maximum == 'Hyperthyroidism':
    tablet = 'Methimazole'
if maximum == 'Hypoglycemia':
    tablet = 'BD Glucose'
if maximum == 'Hypertension':
    tablet = 'losar-H'
if maximum == 'impetigo':
    tablet = 'cloxacillin'
if maximum == 'Jaundice':
    tablet = 'Livful-DS'
else:
#     tablet='Penicillin'
#     print("heelo")
    lat=19.047094 
    lon=73.025452
result8=firebase.put("/message","latitude",lat)
result9=firebase.put("/message","longitude",lon)
