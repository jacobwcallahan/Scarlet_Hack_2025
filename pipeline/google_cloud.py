import os
from google.cloud import speech, translate_v2 as translate, texttospeech
from constants import emergency_words, all_language_codes
import queue


def google_pipeline():

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "pipeline/credentials.json"

    language = "ar"

    client = speech.SpeechClient()

    with open("pipeline/input_audio.wav", "rb") as f:
        audio = speech.RecognitionAudio(content=f.read())
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="es-ES",
        # alternative_language_codes=all_language_codes,
        enable_automatic_punctuation=True,
        enable_word_time_offsets=True,
        # use_enhanced=True,
        # model="phone_call",
        model="latest_long",
        enable_word_confidence=True,
        speech_contexts=[{"phrases": emergency_words}],
    )

    response = client.streaming_recognize(config=config, audio=audio)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)
    text = ""
    for result in response.results:
        text += result.alternatives[0].transcript
        print(result.alternatives[0].transcript)

    translate_client = translate.Client()

    target = language

    result = translate_client.translate(text, target_language=target)
    translated_text = result["translatedText"]
    print("Translated:", translated_text)

    # Path to your service account

    client = texttospeech.TextToSpeechClient()

    # Input text to synthesize
    synthesis_input = texttospeech.SynthesisInput(text=translated_text)

    # Voice configuration
    voice = texttospeech.VoiceSelectionParams(
        language_code=language, ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Audio output format (MP3 is compact + clean)
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Make the request
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Save to file
    with open("pipeline/output.mp3", "wb") as out:
        print("Writing to file")
        out.write(response.audio_content)

    print("✅ Audio saved as output.mp3")


if __name__ == "__main__":
    google_pipeline()
