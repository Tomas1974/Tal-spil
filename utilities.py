import pygame
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def play_music(mp3_file):
    
    file_path = os.path.join(BASE_DIR, mp3_file)

    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()