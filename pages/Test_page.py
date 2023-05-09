import streamlit as st
import requests

text = "Our translation software is FREE. It makes use of the powerful Google translation API which uses Google’s pre-trained neural machine translation to instantly translate words and phrases between English to Gujarati. You can translate up to a maximum of 500 characters per request and can make an unlimited request. Although our Gujarati translation is not 100% accurate - with a few modifications it can be pretty accurate. It is particularly helpful in framing the sentence and to get a general idea on what the sentence is conveying the message. It is therefore used by thousands of people around the globe."

res = requests.get(f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=gu&dt=t&q={text}")
res = res.json()
###################################
print(res)
st.write(res)
st.write(res[0][0][0])
st.markdown("---")
###################################
length = len(res[0])
st.write(length)
for i in range(length):
    st.write(res[0][i][0])