import sounddevice as sd
import wavio

def record_audio(duration, samplerate=44100):
    print("Recording...")
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2)
    sd.wait()
    print("Recording finished.")
    return audio_data

def save_audio(filename, audio_data, samplerate=44100):
    wavio.write(filename, audio_data, samplerate, sampwidth=2)
    print(f"Audio saved as {filename}")
    
def play_audio(audio_data, samplerate=44100):
    print("Playing audio...")
    sd.play(audio_data, samplerate)
    sd.wait()
    print("Playback finished.")

def main():
    duration = int(input("Enter the duration of the recording in seconds: "))
    filename = input("Enter the filename to save the recording : ")
    filename=filename+".wav"
    audio_data = record_audio(duration)
    save_audio(filename, audio_data)
    play_audio(audio_data)

if __name__ == "__main__":
    main()
