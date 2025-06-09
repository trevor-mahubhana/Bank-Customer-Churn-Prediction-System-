# -*- coding: utf-8 -*-
"""
Created on Mon May 26 16:46:43 2025

@author: MALCOM_TREVOR
"""

import pickle
import streamlit as st


st.title("Bank Customer Churn Prediction system")

#st.image(image = "C:/Users/MALCOM_TREVOR/Desktop/DATA SCIENCE/MY PROJECT/ML/Classification Tasks/bank churn/Capture.PNG",
         #caption="Bank Customer Churn")
  

if st.button("Help Desk"):
    st.write("*** Welcome to the Help Desk ***")
    st.write("Here you can find information on how to use the interface for your customer churn predictions")
    st.write("When selecting the country lived note that ")
    st.write("1 : France")
    st.write("2 : Spain")
    st.write("3 : Germany")
    st.write("---------------------------"*10)
    st.write("Select customer's gender? ")
    st.write("1 : Female")
    st.write("2 : Male")
    st.write("---------------------------"*10)
    st.write("Does the customer have a credit card ?")
    st.write("1: Yes")
    st.write("0 : No")
    st.write("---------------------------"*10)
    st.write("Is the customer active member?")
    st.write("1: Yes")
    st.write("0 : No")
    st.write("---------------------------"*10)
                
    
# loading the saved model
with open(r"C:\Users\MALCOM_TREVOR\Desktop\DATA SCIENCE\MY PROJECT\ML\Classification Tasks\bank churn\model\Random Forest Classifier Model with an accuracy of 97%","rb") as f:
    model = pickle.load(f)
    
st.write("Enter the customer's data in the field provided below")


col1,col2 = st.columns(2)

with col1:
    CreditScore = st.text_input("Enter the customer's credit score",placeholder="Type the number")
    
with col2:
    Country_lived = st.selectbox("Select the country the customer lives",options = [1,2,3],index = None)
    
with col1:
    Gender = st.selectbox("Select the customer's gender",options=[1,2],index = None,placeholder = "Choose an option")
    
with col2:
    Age = st.text_input("Enter the customer's age",placeholder="Type the number")
    
with col1:
    time_worked = st.text_input("Enter the time the customer spend with us in  (yrs)",placeholder="Type the number")
    
with col2:
    Balance = st.text_input("Enter the amount of money in a bank account",placeholder="Type the number")
    
with col1:
    product_obtained = st.text_input("Enter the number of products the customer obtained through bank",placeholder="Type the number")
    
with col2:
    Has_CrCard = st.selectbox("Does the customer have a credit card ?",options = [0,1],index = None)
    
with col1:
    Is_Active_Member = st.selectbox("Is the customer an active member?",options = [0,1],placeholder = "Choose an option",index = None)
 
with col2:
    Estimated_Salary = st.text_input("Enter the estimated salary the customer get ?",placeholder="Type the number")
  

checkpoint = ""
if st.button("Predict Churn"):
    churn_prediction = model.predict([[CreditScore,Country_lived,Gender,Age,time_worked,Balance,product_obtained,Has_CrCard,Is_Active_Member,Estimated_Salary]])
                
    if churn_prediction[0]==1:
        checkpoint = "The person is likely to leave the bank"
                    
    else:
        checkpoint = "The person is not likely to leave the bank"
                    
st.success(checkpoint,icon="✅")