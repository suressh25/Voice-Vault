# Voice Vault 🎧

Voice Vault is a simple application that converts your notes into a podcast and uploads it to an S3 bucket. It uses AWS Polly for text-to-speech conversion and Streamlit for the user interface.

## Features

- Convert text notes into audio (MP3 format) using AWS Polly.
- Upload the generated audio file to an S3 bucket.
- Shareable link to listen to the uploaded podcast.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/voice-vault.git
   cd voice-vault
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up AWS credentials:
   - Ensure you have AWS credentials configured in your environment. You can use the AWS CLI to set them up:
     ```bash
     aws configure
     ```

## Usage

1. Run the application:

   ```bash
   streamlit run app.py
   ```

2. Open the Streamlit app in your browser (usually at `http://localhost:8501`).

3. Enter your notes in the text area, click "Convert and Upload," and get the link to your podcast.

## Project Structure

- `app.py`: Main application file for the Streamlit interface.
- `converter.py`: Contains the function to convert text to speech using AWS Polly.
- `upload.py`: Contains the function to upload files to an S3 bucket.
- `requirements.txt`: Lists the Python dependencies.
- `.gitignore`: Specifies files and directories to ignore in version control.

## Requirements

- Python 3.7 or higher
- AWS account with access to Polly and S3 services

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [AWS Polly](https://aws.amazon.com/polly/) for text-to-speech conversion.
- [Streamlit](https://streamlit.io/) for the user interface.
