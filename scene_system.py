import pygame

class SceneSystem:
    def __init__(self, screen):
        self.screen = screen

    def show_scene(self, image_path):
        full_path = "assets/backgrounds/" + image_path
        print("Loading background:", full_path)

        bg = pygame.image.load(full_path).convert()
        bg = pygame.transform.scale(bg, (800, 600))

        self.screen.blit(bg, (0, 0))
        