import boto3


def text_to_speech(text, output_file):
    polly = boto3.client("polly")

    response = polly.synthesize_speech(
        Text=text,
        OutputFormat="mp3",
        VoiceId="Joanna",
    )

    with open(output_file, "wb") as file:
        file.write(response["AudioStream"].read())
