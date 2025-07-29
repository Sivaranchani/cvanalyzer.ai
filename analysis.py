import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
# refer pdf file
from pdf import extractpdf

# CONFIGURATION OF THE API KEY
key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)    

# CALL THE MODEL
model = genai.GenerativeModel('gemini-1.5-flash')   

# createa a def function to analyze the pdf file and job description
def analyze_resume(pdf_doc,job_des):
   if pdf_doc is not None:
      pdf_text = extractpdf(pdf_doc)
      st.write('Extracted successfully')
  
   else:
      st.warning('drop file in PDF format')
  
   ats_score =  model.generate_content(f''' compare the resume {pdf_text} with the job description {job_des} and get ATS score in scale of 0 - 100
                                       first give the ats score and then give the reason for the score and 
                                       how to improve the score in detail and in bullet points''')
   good_fit = model.generate_content(f''' compare the resume {pdf_text} with the job description {job_des} and tell if i am a good fit or not also in bullet points''')
   
   swot_analysis = model.generate_content(f''' compare the resume {pdf_text} with the job description {job_des} and give SWOT analysis in bullet points''')
   
   prob = model.generate_content(f''' compare the resume {pdf_text} with the job description {job_des} and tell me the probability of getting selected for this job in percentage''')
   
   return st.write('ATS Score:', ats_score.text), st.write('Good Fit:', good_fit.text),st.write('SWOT Analysis:', swot_analysis.text), st.write('Probability of getting selected:', prob.text)