import streamlit as st
from langchain_community.document_loaders import YoutubeLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
import os
from langchain_openai import ChatOpenAI


openai_api_key = st.secrets["OPENAI_API_KEY"]
st.set_page_config(page_title="shakeel")
st.title("YouTube Video Summarizer")

# Define function for video transcription
def video_to_text(url):
    loader = YoutubeLoader.from_youtube_url(
        url,
        add_video_info=False,
        language=["hi", "id", "en", "ur"],
        #translation="ur",
    )
    result =loader.load()
    return result

# Define function for summarization using LLM
def summarize_text(llm,system_role,text):
    prompt = ChatPromptTemplate.from_messages(
        [("system","{system_role}: \\n\\n{context}")])
    chain = create_stuff_documents_chain(llm, prompt)    
    summary = chain.invoke({"system_role":system_role,"context":text})
    return summary

# Streamlit UI
def main():
    with st.sidebar:
        st.subheader("Enter the YouTube Video URL")
        video_url = st.text_input("Enter", key="video_url")
        st.subheader("Choose how to interpret your video summary")
        system_role = st.text_input("Enter", key="system_role")
        
    if st.button("Summarize"):
        with st.spinner("Processing the video..."):
            try:
                # Step 1: Transcribe video
                transcription = video_to_text(video_url)
                if not transcription:
                    st.error("Failed to transcribe video. Please check the URL or video content.")
                    return
                # Step 2: Summarize text
                llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)
                summary = summarize_text(llm=llm,system_role=system_role,text=transcription)

                # Step 3: Display and edit summary
                st.success("Video transcription and summarization completed!")
                st.write("### Original Summary:")
                st.text(summary)

            except Exception as e:
                st.error(f"An error occurred: {e}")
    
if __name__ == "__main__":
    main()
