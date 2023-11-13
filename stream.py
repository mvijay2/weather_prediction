import streamlit as st
#to display image on app whatver your uploading those should be in same folder where this .py file existed
#st.image('weather.png')



#page name and characters
st.set_page_config(page_title="weather pred")


# application title
st.title('weather data prediction')

#app header
st.header('komuram bheem rainfall prediction')

#sub header
st.subheader('get to know the rainfall')

#to give information in blue color
st.info('this prediction is based on the prior 50 years data')

#warning message yellow
st.warning('dont fully depend on this in your life ')
#error message basically it will show in red color
st.error('wrong input data entered')

#if you want to tell success in green color
st.success('entered correct data')



#markdown to give any data bigger biggest using # with name
st.markdown('# data columns')

st.markdown('## date')
st.markdown('#### 1951 to 2020')

st.markdown('## t min')
st.markdown('## t max')

st.markdown('## rain')
#give image using mardown
st.markdown(':dog:')
st.markdown('#### true or  false')
#to write something let the farmers know about this model 
st.write('true and false encoded into int format')

#to give caption
st.caption('it wont give you in decimal point')

#to display a math equations
#st.latex(r'''a+b x^2+c''')



##radio widget
st.radio('pick your state',['Telangana','AandhraPradesh','WB','bhr','krl'])

#select box
st.selectbox('pick your educatation qualification',['10th','12th','degree'])

#checkbox
st.button('click')