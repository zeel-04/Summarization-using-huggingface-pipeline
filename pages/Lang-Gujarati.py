import streamlit as st
import requests
import model

st.title("Summarization Made Easy")
text = st.text_area("Enter the text in gujarati you want to summarize")
max_length_of_output = st.number_input("Enter the maximum length(includes words and punctuation marks) for the summarized text",min_value=50, max_value=1024, value=200, step=1)

if len(text)!=0:
    #converting gujarati to english
    res_1 = requests.get(f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=gu&tl=en&dt=t&q={text}")
    input_text=""
    res_1 = res_1.json()
    length = len(res_1[0])
    # st.write(length)
    for i in range(length):
        input_text=input_text+res_1[0][i][0]
        # st.write(res_1[0][i][0])

    # st.write(input_text)
    with st.spinner():
        summarized_text = model.summarize(input_text,max_length_of_output)
        # st.write(summarized_text[0]['summary_text'])
        output_gujarati_text = summarized_text[0]['summary_text']
        res_2 = requests.get(f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=gu&dt=t&q={output_gujarati_text}")
        res_2 = res_2.json()
        output_text=""
        length_2 = len(res_2[0])
        # st.write(length)
        for i in range(length_2):
            output_text=output_text+res_2[0][i][0]
        st.write(output_text)