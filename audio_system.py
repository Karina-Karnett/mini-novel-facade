import pygame

class AudioSystem:
    def __init__(self):
        pygame.mixer.init()

    def play_music(self, file):
        pygame.mixer.music.load("assets/music/" + file)
        pygame.mixer.music.play(-1)