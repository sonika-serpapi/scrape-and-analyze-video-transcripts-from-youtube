from serpapi import GoogleSearch
from dotenv import load_dotenv
import os
load_dotenv() 
from ollama import chat
from ollama import ChatResponse

def summarize_text(text):
    response: ChatResponse = chat(model='llama3', messages=[
    {
        'role': 'user',
        'content': f"Summarize the following text:\n\n{text}\n\nSummary:",
    },
    ])
    return response['message']['content']

# --- 1. Fetch Transcript Data from Youtube ---
def get_transcript_from_youtube(v):
    # Implement your YouTube transcript fetching logic here
    params = {
    "api_key": os.environ["SERPAPI_API_KEY"],
    "engine": "youtube_video_transcript",
    "v": v,
    "language_code": "en"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return results.get("transcript", "")

# --- Main Execution ---
if __name__ == "__main__":
    video_id = "epMDcqKoQys"  # Replace with your YouTube video ID
    transcript = get_transcript_from_youtube(video_id)
    if not transcript:
        print("No transcript found for the video.")
    else:
        summary = summarize_text(transcript)
        print("Transcript Summary:", summary)