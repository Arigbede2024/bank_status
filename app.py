import streamlit as st
from mode import *

def main():
    st.title("FINANCIAL INCLUSION PREDICTION")

    country =st.selectbox('select your country', (data2['country']))
    uniqueid =st.selectbox('Insert your Id', (data2['uniqueid']))
    location_type =st.selectbox('Insert your location_type',(data2['location_type']))
    cellphone_access= st.selectbox("If interviewee has access to a cellphone: Yes, No",(data2['cellphone_access']))
    household_size= st.number_input('Number of people living in your house',value=None)
    age_of_respondent =st.number_input("Input your age", value =None)
    gender_of_respondent =st.selectbox('what is your gender',(data2['gender_of_respondent']))
    relationship_with_head =st.selectbox('what your relationship with head of the house',(data2['relationship_with_head']))
    marital_status= st.selectbox('what is your marital status',(data2["marital_status"]))
    education_level= st.selectbox('select your education_leavel',(data2["education_level"]))
    job_type =st.selectbox('select your job_type'(data2['job_type']))

    Bank= "" 

    if st.button("predict"):

        Bank=prediction([country,uniqueid,location_type,cellphone_access,household_size,age_of_respondent,gender_of_respondent,relationship_with_head,marital_status,education_level,job_type])
    st.success(Bank) 

if __name__ =="__main__" :
     main()      