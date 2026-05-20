import pygame
from facade import GameFacade

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mini Novel")

game = GameFacade(screen)
game.start_game()

running = True
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            x, y = event.pos

            if x > 400 and y > 450:

                if game.choice_active:
                    continue

                if game.dialogue.index >= len(game.dialogue.dialogues) - 1:
                    game.next()
                else:
                    game.dialogue.next()

        
        if event.type == pygame.KEYDOWN:

            if game.choice_active:

                if event.key == pygame.K_1:
                    game.make_choice(1)

                if event.key == pygame.K_2:
                    game.make_choice(2)

    screen.fill((0, 0, 0))

    game.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()