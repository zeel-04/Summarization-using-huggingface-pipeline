import streamlit as st
import model

st.title("Summarization Made Easy")
text = st.text_area("Enter the text you want to summarize")
max_length_of_output = st.number_input("Enter the maximum length(includes words and punctuation marks) for the summarized text",min_value=50, max_value=1024, value=200, step=1)

if len(text)!= 0:
    with st.spinner():
        summarized_text = model.summarize(text,max_length_of_output)
        st.write(summarized_text[0]['summary_text'])