import pygame

def play_audio(file_path):
    """Plays an audio file using pygame."""
    pygame.mixer.init()  # Initialize the mixer module
    pygame.mixer.music.load(file_path)  # Load the audio file
    pygame.mixer.music.play()  # Start playing the audio

    # Keep the program running until the music finishes or user input
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10) # Control CPU usage

