# YouTube Video Summarizer

This **YouTube Video Summarizer** is a Streamlit-based web application that transcribes and summarizes YouTube videos using **LangChain** and **OpenAI's GPT** models. Users can input a YouTube video URL and customize how the video summary is generated, providing a concise interpretation of the video's content.

---

## Features

- **Transcribe Videos**: Extracts text from videos in supported languages (Hindi, Indonesian, English, and Urdu).
- **Summarize Content**: Uses OpenAI's GPT-4o-mini model to create summaries based on a customizable system role.
- **Streamlit Interface**: Simple and interactive user interface for ease of use.

---

## How It Works

1. **Input YouTube URL**: Paste the URL of the YouTube video you want to summarize.
2. **Customize Interpretation**: Enter a specific system role to guide the summary generation.
3. **Summarization**: The app transcribes the video and generates a summary based on the input.
4. **View Results**: The transcription and summary are displayed in the interface.

---

## Installation

Follow these steps to run the tool locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/shakeel-ai/youtube-video-summarizerer.git
   cd youtube-video-summarizer
   
2.Install Dependencies: Make sure you have Python installed. Then, run:
pip install -r requirements.txt

3. Set OpenAI API Key: Add your OpenAI API key to the environment variable:
   export OPENAI_API_KEY="your_openai_api_key"
4. Run the App:
   streamlit run app.py

Usage
Open the application in your browser (default URL: http://localhost:8501).
Enter the YouTube video URL in the sidebar.
Specify how you want the summary interpreted using the "System Role" field.
Click the "Summarize" button to process the video.
View the transcription and summary on the main page.
