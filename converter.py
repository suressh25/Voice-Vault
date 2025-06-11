import boto3

def text_to_speech(text, output_file):
    polly = boto3.client('polly')
    
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Joanna'  # Other options: 'Matthew', 'Amy', etc.
    )

    with open(output_file, 'wb') as file:
        file.write(response['AudioStream'].read())

# Example
text_to_speech("Welcome to my podcast! Today we discuss AWS projects.", "podcast.mp3")
