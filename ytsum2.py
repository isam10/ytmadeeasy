import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # Load all environment variables
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Prompt for the video summarizer
prompt = """You are a YouTube video summarizer. You will be taking the transcript text
and summarizing the entire video, providing important points in bullet points,
and also trying to provide timestamps. Please provide the summary of the text given here: """

# Function to extract transcript details from YouTube videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript, transcript_text

    except Exception as e:
        raise e

# Function to generate summary based on the prompt using Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Function to extract timestamps for different topics
def extract_topic_timestamps(transcript_text, transcript_data):
    timestamps = []
    for item in transcript_data:
        if "topic" in item["text"].lower():
            timestamps.append((item["start"], item["text"]))

    return timestamps

# Streamlit app layout
st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get Detailed Notes"):
    transcript_text, transcript_data = extract_transcript_details(youtube_link)

    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)

        # Extract and display topic timestamps
        topic_timestamps = extract_topic_timestamps(transcript_text, transcript_data)
        if topic_timestamps:
            st.markdown("## Topic Timestamps:")
            for timestamp, topic in topic_timestamps:
                st.write(f"- **{topic}**: {timestamp:.2f} seconds")
