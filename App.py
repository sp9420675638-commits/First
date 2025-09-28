import streamlit as st
import pickle
st.title('Health Insurance Premium Prediction')

age=st.number_input('AGE:',min_value=0,step=1)
bmi=st.number_input('BMI:')
children=st.number_input('Number of Children:',min_value=0,step=1)
Gender=st.radio("Gender:",["Male","Female"])
smoker=st.radio("Do you smoke ?",["Yes","No"])
model=pickle.load(open('m.pkl','rb'))

if(st.button("Predict")):
    Gender=0 if Gender.upper()=='MALE' else 1
    smoker=0 if smoker.upper()=='NO' else 1
    x_test=[[age,bmi,children,Gender,smoker]]
    yp=str(round(model.predict(x_test)[0],2))
    st.write('Your Premium is \u20B9 '+yp)