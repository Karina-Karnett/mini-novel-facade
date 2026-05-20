from audio_system import AudioSystem
from scene_system import SceneSystem
from dialogue_system import DialogueSystem
from save_system import SaveSystem

import pygame


class GameFacade:
    def __init__(self, screen):
        self.screen = screen

        self.audio = AudioSystem()
        self.scene = SceneSystem(screen)
        self.dialogue = DialogueSystem(screen)
        self.save = SaveSystem()

        self.stage = 0

        self.current_background = "street.jpeg"
        self.current_character = None

        
        self.choice_active = False
        self.choices = []

        
        self.domofon_sound = pygame.mixer.Sound(
            "assets/music/domofon.mp3"
        )

   
    def start_game(self):

        self.audio.play_music("gen_265_main.mp3")

        self.dialogue.set_dialogues([
            "И вот я снова на улицах города...",
            "Совсем не помню, что было вчера после работы.",
            "Сегодня первый выходной спустя неделю.",
            "Может поехать к Годжо? Он говорил, что будет дома."
        ])

   
    def next(self):

        
        if self.stage == 0:

            self.current_background = "blackfade.jpeg"

            self.dialogue.set_dialogues([
                "..."
            ])

        
        elif self.stage == 1:

            self.current_background = "entrance.jpeg"

            self.dialogue.set_dialogues([
                "Надеюсь, он не спит...",
                "Хотя зная Годжо — он наверняка опять смотрит аниме."
            ])

        
        elif self.stage == 2:

            self.domofon_sound.play()

            self.dialogue.set_dialogues([
                "..."
            ])

        
        elif self.stage == 3:

            self.current_background = "blackfade.jpeg"

            self.dialogue.set_dialogues([
                "Секунду спустя дверь открылась."
            ])

        
        elif self.stage == 4:

            self.current_background = "entrance.jpeg"
            self.current_character = "gojo1.png"

            self.dialogue.set_dialogues([

                "Годжо: Дэни! Какими судьбами? Ты же работаешь как проклятый!",

                " Решил повидаться, вдруг ты меня оставил.",

                "Годжо: Двинем куда-нибудь, или ты ко мне?",

                "Игрок: А куда пойдем? Не хочу в тот торговый центр..",

                "Годжо: Слухай, я недавно нашел крышу многоэтажки куда можно спокойно пройти.",

                "Годжо: Крайне красивое место вечером.. Можем туда двинуть.",

                "Годжо: Либо в парк как раньше. Я давно тебя не видел, поэтому выбор за тобой."
            ])

        elif self.stage == 5:

            self.choice_active = True

            self.choices = [
                "Крыша",
                "Парк"
            ]

        self.stage += 1

    
    def make_choice(self, choice):

        self.choice_active = False

        
        if choice == 1:

            self.dialogue.set_dialogues([

                "Игрок: Заинтриговал ты меня этой крышей.. пошли.",

                "Годжо: Ехать до нее далековато, зато посплетничаем вдоволь :)"
            ])

        
        elif choice == 2:

            self.dialogue.set_dialogues([

                "Игрок: Как в старые добрые у парка возле вуза.. Не хватает мне ностальгии, давай туда.",

                "Годжо: Знал что ты захочешь туда. Меланхолик."
            ])

    # 🎨 отрисовка
    def draw(self):

        self.scene.show_scene(self.current_background)

        # 🧍 персонаж
        if self.current_character:

            char = pygame.image.load(
                "assets/characters/" + self.current_character
            ).convert_alpha()

            char = pygame.transform.scale(char, (350, 500))

            self.screen.blit(char, (420, 100))

        # 💬 диалог
        self.dialogue.draw()

        # 🎮 выбор
        if self.choice_active:

            font = pygame.font.SysFont("Arial", 30)

            overlay = pygame.Surface((500, 170))
            overlay.set_alpha(220)
            overlay.fill((40, 40, 40))

            self.screen.blit(overlay, (150, 180))

            for i, choice in enumerate(self.choices):

                text = font.render(
                    f"{i + 1}. {choice}",
                    True,
                    (255, 255, 255)
                )

                self.screen.blit(
                    text,
                    (190, 230 + i * 60)
                )

    def load_game(self):

        print("Loading game...")
        self.save.load()

    def open_settings(self):

        print("Opening settings...")

    def exit_game(self):

        print("Saving and exiting...")
        self.save.save()