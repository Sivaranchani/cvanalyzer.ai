import streamlit as st
from analysis import analyze_resume
st.title('CV Analyzer')
st.header('this page helps you to compare your resume with the job description ')
st.sidebar.subheader('Drop your resume here 📋')
pdf_doc = st.sidebar.file_uploader('Upload your resume in PDF format ', type=['pdf'])

job_des = st.text_area('Paste the job description here', max_chars=10000)
submit = st.button('get result')
if submit:
    with st.spinner('getting results ...'):
      analyze_resume(pdf_doc, job_des)