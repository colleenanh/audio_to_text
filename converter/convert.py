from pydub import AudioSegment
import os

def mp4_to_wav(mp4_filepath, wav_filepath, first_n_seconds=None):
    _, extension = os.path.splitext(mp4_filepath)
    
    if extension == ".mp4":
        print(f"Converting {mp4_filepath} to WAV...")
        audio = AudioSegment.from_file(mp4_filepath, format="mp4")
        
        if first_n_seconds:
            # Trim the audio to the first 'first_n_seconds' seconds
            audio = audio[:first_n_seconds * 1000]  # pydub uses milliseconds
            
        audio.export(wav_filepath, format='wav')
        print(f"Conversion complete. WAV file saved at: {wav_filepath}")
    else:
        raise ValueError(f"Extension '{extension}' is not supported. Only .mp4 files are supported.")
