# import transformers
# import torch
from transformers import pipeline
import streamlit as st

@st.cache_resource
def summarize(text,max_length):
    
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", tokenizer="facebook/bart-large-cnn",framework="pt")
    summary = summarizer(text, min_length=5, max_length=max_length)

    return summary
# print(summary)