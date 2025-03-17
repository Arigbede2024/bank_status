import pandas as pd
import numpy as np
from sklearn. preprocessing import LabelEncoder,StandardScaler
import pickle

model = pickle.load(open('model.pkl','rb'))
data2 = pickle.load(open('status.pkl','rb'))

def prediction(data):
    le=LabelEncoder()
    scale=StandardScaler()
    df=pd.DataFrame(data)
    

    for i in data:
        if type(i)==str:
            df.iloc[data.index(i)]=le.fit_transform(df.iloc[data.index(i)])
    df=scale.fit_transform(df)
    pred =model.predict(df.reshape(1,-1))
    if pred[0]==1:
        return 'The customer has Bank Account' 
    else:
        return 'The customer do not have Bank Account'       
    
prediction(['Kenya',
 2018,
 'uniqueid_3',
 'Urban',
 'Yes',
 5,
 26,
 'Male',
 'Other relative',
 'Single/Never Married',
 'Vocational/Specialised training',
 'Self employed'])
# print(model.predict(np.array([-1.29944427,  1.20854126, -0.58784162,  1.24989924,  0.58972136,
#         0.53983446, -0.77512418,  1.19936578,  0.41341065,  0.60758282,
#         2.49327861,  1.15462805]).reshape(1,-1)))