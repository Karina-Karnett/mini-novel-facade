import pygame


class DialogueSystem:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 28)

        self.dialogues = []
        self.index = 0
        self.current_text = ""

    # 📌 установка диалогов
    def set_dialogues(self, dialogues):
        self.dialogues = dialogues
        self.index = 0

        if self.dialogues:
            self.current_text = self.dialogues[0]
        else:
            self.current_text = ""

    # 📌 следующий текст
    def next(self):
        if self.index < len(self.dialogues) - 1:
            self.index += 1
            self.current_text = self.dialogues[self.index]

    # 📌 перенос текста по ширине
    def wrap_text(self, text, max_width=740):
        words = text.split(" ")
        lines = []
        current = ""

        for word in words:
            test_line = current + word + " "

            if self.font.size(test_line)[0] < max_width:
                current = test_line
            else:
                lines.append(current)
                current = word + " "

        lines.append(current)
        return lines

    # 📌 отрисовка
    def draw(self):
        overlay = pygame.Surface((800, 150))
        overlay.set_alpha(180)
        overlay.fill((60, 60, 60))
        self.screen.blit(overlay, (0, 450))

        lines = self.wrap_text(self.current_text)

        y = 470
        for line in lines:
            text_surface = self.font.render(line, True, (255, 255, 255))
            self.screen.blit(text_surface, (30, y))
            y += 28