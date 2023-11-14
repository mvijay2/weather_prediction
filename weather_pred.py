
import streamlit as st
import joblib as jb
import numpy as np

# Load the saved model
loaded_model = jb.load("D:\git projects\weather_prediction\weatherpred.joblib")

# Streamlit app
st.title('Asifabad Weather Prediction')

def weather_prediction(input_data):
   
    np_array=np.asarray(input_data)
    data=np_array.reshape(1,-1)
    #data=scaler.fit_transform(reshaped)
    prediction = loaded_model.predict(data)
    #prediction   ``
    if prediction==0:
        return 'NO RAIN :cloud:'
    else:
        return 'Raining'
                       
def main():
    
    day=st.text_input('Enter Date')
    month=st.text_input('Enter Month')
    year=st.text_input('Enter Year')
    TMAX=st.text_input('Enter T_max')
    TMIN=st.text_input('Enter T_min')
    
    result=''

    if st.button('Predict Weather'):

      result=weather_prediction([day,month,year,TMAX,TMIN])

    st.success(result)

if __name__=='__main__':
    main()
 

   
