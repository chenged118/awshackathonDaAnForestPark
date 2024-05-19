import pygame
import sys
import json
import requests
import asyncio
from machine import Machine
from settings import *

class WelcomePage:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Slot Machine - Welcome')
        self.clock = pygame.time.Clock()
        self.title_font = pygame.font.Font(UI_FONT, WIN_FONT_SIZE)
        self.button_font = pygame.font.Font(UI_FONT, 80)
        self.start_button = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 100)

    def draw(self):
        self.screen.fill((0, 0, 0))
        title_surface = self.title_font.render("Welcome to Slot Machine", True, pygame.Color('yellow'))
        self.screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, HEIGHT // 2 - title_surface.get_height() // 2 - 100))
        
        pygame.draw.rect(self.screen, pygame.Color('green'), self.start_button)
        button_text = self.button_font.render("Start", True, pygame.Color('white'))
        self.screen.blit(button_text, (self.start_button.x + (self.start_button.width - button_text.get_width()) // 2, self.start_button.y + (self.start_button.height - button_text.get_height()) // 2))
        
        pygame.display.flip()

    async def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.collidepoint(event.pos):
                        return  # Exit the loop to start the game

            self.draw()
            self.clock.tick(FPS)
            await asyncio.sleep(0.01)

class StartPage:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Slot Machine - Chat Room')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        
        self.chat_log = [{'role': 'assistant', 'message': "Welcome! I'm your Slot Machine NPC. Type 'play' to start the game, or tell me anything you want!"}]
        self.input_box = pygame.Rect(10, HEIGHT - 60, WIDTH - 20, 50)
        self.input_text = ''
        self.active = False
        self.start_game = False

    def draw(self):
        self.screen.fill((0, 0, 0))
        
        # Draw chat log
        max_line_length = WIDTH // 2 - 20  # Maximum line length for wrapping
        y_offset = 50
        for chat in self.chat_log:
            message, is_user = chat["message"], chat['role'] == "user"
            if is_user:
                txt_surface = self.font.render(message, True, pygame.Color('white'))
                x = WIDTH - txt_surface.get_width() - 70
                if txt_surface.get_width() > max_line_length:
                    lines = [message[i:i+70] for i in range(0, len(message), 70)]
                    for line in lines:
                        txt_surface = self.font.render(line, True, pygame.Color('white'))
                        self.screen.blit(txt_surface, (x, y_offset))
                        y_offset += 50
                else:
                    self.screen.blit(txt_surface, (x, y_offset))
                    y_offset += 50
            else:
                txt_surface = self.font.render(message, True, pygame.Color('yellow'))
                x = 70
                if txt_surface.get_width() > max_line_length:
                    lines = [message[i:i+70] for i in range(0, len(message), 70)]
                    for line in lines:
                        txt_surface = self.font.render(line, True, pygame.Color('yellow'))
                        self.screen.blit(txt_surface, (x, y_offset))
                        y_offset += 50
                else:
                    self.screen.blit(txt_surface, (x, y_offset))
                    y_offset += 50
            
        # Draw input box
        txt_surface = self.font.render(self.input_text, True, pygame.Color('white'))
        self.screen.blit(txt_surface, (self.input_box.x + 10, self.input_box.y + 10))
        pygame.draw.rect(self.screen, pygame.Color('white'), self.input_box, 2)
        
        pygame.display.flip()


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_box.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.chat_log.append({'role': 'user', 'message': self.input_text})
                    self.simulate_response(self.input_text)
                    self.input_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                else:
                    self.input_text += event.unicode

    def generate_imgs(self, style):
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiODg1MTEyNTItYzI2Ni00YzIwLTg1MmEtZTU3MzAxYzhmMjEzIiwidHlwZSI6ImFwaV90b2tlbiJ9.1CK031wFzoA5whOZ4EbiOaL8RK9jBoBYujEoINrpeEc"}

        url = "https://api.edenai.run/v2/image/generation"
        payload = {
            "providers": "openai",
            "text": style,
            "resolution": "256x256",
            "fallback_providers": "replicate",
            "num_images": 7,
        }

        response = requests.post(url, json=payload, headers=headers)
        result = json.loads(response.text)
        for i in range(7):
            print(result['replicate']['items'][i]["image_resource_url"])


    def simulate_response(self, user_message):
        if user_message.lower() == "play":
            self.start_game = True
        elif user_message.startswith("style:"):
            # self.generate_imgs(user_message.split(':')[-1])
            self.chat_log.append({'role': 'assistant', 'message': f"OK! I have set your image style to {user_message.split(':')[-1]}"})
        else:
            headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiODg1MTEyNTItYzI2Ni00YzIwLTg1MmEtZTU3MzAxYzhmMjEzIiwidHlwZSI6ImFwaV90b2tlbiJ9.1CK031wFzoA5whOZ4EbiOaL8RK9jBoBYujEoINrpeEc"}

            url = "https://api.edenai.run/v2/text/chat"
            payload = {
                "providers": "openai",
                "text": user_message,
                "chatbot_global_action": "Act as an assistant",
                "previous_history": self.chat_log,
                "temperature": 0.0,
                "max_tokens": 150,
                "fallback_providers": "replicate"
            }

            response = requests.post(url, json=payload, headers=headers)
            result = json.loads(response.text)
            print(result['openai']['generated_text'])
            response = result['openai']['generated_text']
            # response = "test"
            self.chat_log.append({'role': 'assistant', 'message': response})

    async def run(self):
        while not self.start_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.handle_event(event)

            self.draw()
            self.clock.tick(FPS)
            await asyncio.sleep(0.01)


class GameOverPage:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Game Over')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(UI_FONT, WIN_FONT_SIZE)
        self.btn_font = pygame.font.Font(UI_FONT, 80)
        self.quit_button = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 100)

    def draw(self):
        self.screen.fill((0, 0, 0))
        text_surface = self.font.render("Game Over", True, pygame.Color('red'))
        self.screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2 - text_surface.get_height() // 2 - 100))
        pygame.draw.rect(self.screen, pygame.Color('red'), self.quit_button)
        button_text = self.btn_font.render("Quit", True, pygame.Color('white'))
        self.screen.blit(button_text, (self.quit_button.x + (self.quit_button.width - button_text.get_width()) // 2, self.quit_button.y + (self.quit_button.height - button_text.get_height()) // 2))
        pygame.display.flip()

    async def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.quit_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

            self.draw()
            self.clock.tick(FPS)
            await asyncio.sleep(0.01)

class Game:
    def __init__(self):

        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Slot Machine Demo')
        self.clock = pygame.time.Clock()
        self.bg_image = pygame.image.load(BG_IMAGE_PATH).convert_alpha()
        self.grid_image = pygame.image.load(GRID_IMAGE_PATH).convert_alpha()
        self.machine = Machine()
        self.delta_time = 0.01
        self.game_over = False

    async def run(self):
        self.start_time = pygame.time.get_ticks()

        while not self.game_over:
            # Handle quit operation
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Time variables
            self.delta_time = (pygame.time.get_ticks() - self.start_time) / 1000
            self.start_time = pygame.time.get_ticks()

            # Drawing
            self.screen.blit(self.bg_image, (0, 0))
            self.machine.update(self.delta_time)
            self.screen.blit(self.grid_image, (0, 0))

            # Check for game over
            if self.machine.currPlayer.balance <= 0:
                self.game_over = True

            pygame.display.update()
            self.clock.tick(FPS)

            await asyncio.sleep(0.01)

        return "game_over"

async def main():
    while True:
        welcome_page = WelcomePage()
        await welcome_page.run()
        start_page = StartPage()
        await start_page.run()
        game = Game()
        if await game.run() == "game_over":
            game_over_page = GameOverPage()
            await game_over_page.run()

if __name__ == "__main__":
    asyncio.run(main())
