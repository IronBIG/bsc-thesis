import os
import glob
import pygame

def convert_midi_to_mp3(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Initialize pygame
    pygame.init()
    pygame.mixer.init()

    # Get a list of all MIDI files in the input folder
    midi_files = glob.glob(os.path.join(input_folder, '*.mid'))

    for file_path in midi_files:
        # Get the base file name without extension
        file_name = os.path.splitext(os.path.basename(file_path))[0]

        # Set the output MP3 file path
        output_path = os.path.join(output_folder, f"{file_name}.mp3")

        # Load the MIDI file
        pygame.mixer.music.load(file_path)

        # Export the MIDI file as an MP3
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
        pygame.mixer.music.queue(pygame.event.Event(pygame.USEREVENT))
        pygame.mixer.music.export(output_path, format='mp3')

        print(f"Converted {file_path} to {output_path}")

    # Quit pygame
    pygame.mixer.quit()
    pygame.quit()

# Example usage
input_folder = 'C:\\Users\\01040\Documents\\AI\BSc Thesis\\research2\\4. 8randomfiles cut primer'
output_folder = 'C:\\Users\\01040\Documents\\AI\BSc Thesis\\research2\\7. orig mp3'

convert_midi_to_mp3(input_folder, output_folder)