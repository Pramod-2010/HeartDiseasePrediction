


import numpy as np
import pickle
import streamlit as st

# Set the background image for the app
st.set_page_config(page_title="My Streamlit App", page_icon=":heart:", layout="wide")


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://hips.hearstapps.com/hmg-prod/images/health-care-concept-royalty-free-image-185000832-1549647918.jpg");
             background-attachment: fixed;
             background-size: 100%
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 


# loading the saved models
loaded_model = pickle.load(open("C:/Users/Paatashaala/Downloads/heart_disease_model.sav", 'rb'))



#creating a function for prediction
def heartdisease_prediction(input_data):
    

    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
      return 'Do not Worry.The Person does not have a Heart Disease'
    else:
      return 'The Person has Heart Disease. Consult doctor as soon as possible'
  
    

    
    #giving a title
st.title('Heart Disease Prediction')
    
    
    # getting the input data from the user
    
col1, col2 = st.columns(2)
    
with col1:
    age = st.number_input('Age (29 - 77)')
        
with col2:
    sex = st.number_input('Gender (Male : 1, Female : 0)')
        
with col1:
    cp = st.number_input('Chest Pain types (0 : typical type 1 angina, 1 : typical type angina, 2 : non-angina pain, 3 : asymptomatic)')
        
with col2:
    trestbps = st.number_input('Resting Blood Pressure (94 - 200)')
        
with col1:
    chol = st.number_input('Serum Cholestoral in mg/dl (126 - 564)')
        
with col2:
    fbs = st.number_input('Fasting Blood Sugar (value 1 : > 120 mg/dl, value 0 : < 120 mg/dl)')
        
with col1:
    restecg = st.number_input('Resting Electrocardiographic results (0 - 2)')
        
with col2:
    thalach = st.number_input('Maximum Heart Rate achieved (71 - 202)')
        
with col1:
    exang = st.number_input('Exercise Induced Angina (Yes : 1, No : 0)')
        
with col2:
    oldpeak = st.number_input('ST depression induced by exercise (0 - 6.2)')
        
with col1:
    slope = st.number_input('Slope of the peak exercise ST segment (0 - 1)')
        
with col2:
    ca = st.number_input('Major vessels colored by flourosopy (0 - 3)')
        
with col1:
    thal = st.number_input('thal (0 : normal, 1 : fixed defect, 2 : reversable defect)')
        
    
    #codes for Prdiction
diagnosis = ''
    
    #creating a button for prediction
if st.button('Heart Disease Test Result'):
    diagnosis = heartdisease_prediction([age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal])
    
        
st.success(diagnosis)
    
    
    
    
    
    
