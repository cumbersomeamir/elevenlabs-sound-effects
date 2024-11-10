import os
from elevenlabs import ElevenLabs


elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

def generate_sound_effect(text: str):
    output_path = "output.mp3"
    folder_path = "testing_sound_effects"
    os.makedirs(folder_path, exist_ok=True)
    output_path = os.path.join(folder_path, output_path)
    
    print("Generating sound effects...")
    result = elevenlabs.text_to_sound_effects.convert(
        text=text,
        duration_seconds=1,
        prompt_influence=0.3,
    )

    with open(output_path, "wb") as f:
        for chunk in result:
            f.write(chunk)
    print(f"Audio saved to {output_path}")
    

sound= input("Enter the prompt for sound effect ")
generate_sound_effect(sound)
