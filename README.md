# ytmadeeasy
# YouTube Transcript to notes

This Python application uses Streamlit, Google's Generative AI, and the YouTube Transcript API to convert YouTube video transcripts into detailed notes. It also extracts timestamps for different topics discussed in the video.

## Features

- Extracts transcript details from YouTube videos.
- Generates a summary of the transcript using Google's Generative AI.
- Extracts timestamps for different topics discussed in the video.
- Displays the YouTube video thumbnail and the detailed notes in a Streamlit app.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a .env file in the root directory and add your Google API Key:

    ```bash
    echo "GOOGLE_API_KEY=your_google_api_key" > .env
    ```

    

## Usage

1. Run the Streamlit app:
    
    streamlit run app.py
    
2. Enter the YouTube video link in the text input field.
3. Click on the "Get Detailed Notes" button to generate the detailed notes and topic timestamps.

## Note

This application requires a Google API Key to use Google's Generative AI. Please ensure you have the necessary permissions and quota to use this service.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
