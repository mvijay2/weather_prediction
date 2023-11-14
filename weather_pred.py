
import streamlit as st
import joblib as jb
import numpy as np

# Load the saved model
loaded_model = jb.load("D:\git projects\weather_prediction\weatherpred.joblib")

# Streamlit app
st.title('weather prediction')

def weather_prediction(input_data):
   
    np_array=np.asarray(input_data)
    data=np_array.reshape(1,-1)
    #data=scaler.fit_transform(reshaped)
    prediction = loaded_model.predict(data)
    #prediction   ``
    if prediction==0:
        return 'NO RAIN, lets dry whatever you want'
    else:
        return 'Raining'
                       
def main():
    
    day=st.text_input('enter day')
    month=st.text_input('enter month')
    year=st.text_input('enter year')
    TMAX=st.text_input('enter t_max')
    TMIN=st.text_input('enter t_min')
    
    result=''

    if st.button('predict weather'):

      result=weather_prediction([day,month,year,TMAX,TMIN])

    st.success(result)

if __name__=='__main__':
    main()
 

   
