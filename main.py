import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# --- Constants ---
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CENTER_LINE_WIDTH = 5

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Paddle dimensions
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 80
PADDLE_SPEED = 6

# Ball dimensions
BALL_RADIUS = 10
INITIAL_BALL_SPEED = 5
BALL_SPEED_INCREMENT = 0.2

# Score font
FONT = pygame.font.Font(None, 64)


# --- Classes ---

class Paddle:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.color = color
        self.speed = PADDLE_SPEED

    def move(self, up, down):
        if up:
            self.rect.y -= self.speed
        if down:
            self.rect.y += self.speed
        # Keep the paddle within the screen bounds
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - PADDLE_HEIGHT))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def ai_move(self, ball_y, difficulty_factor):
        # Introduce a delay based on difficulty
        delay = (3 - difficulty_factor) * 0.1  # Difficulty can be 1, 2, or 3

        # Simulate a delay, making the AI imperfect
        if random.random() < delay:
            return

        if self.rect.centery < ball_y:
            self.rect.y += self.speed
        elif self.rect.centery > ball_y:
            self.rect.y -= self.speed
        # Keep the paddle within the screen bounds
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - PADDLE_HEIGHT))


class Ball:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.color = color
        self.speed_x = INITIAL_BALL_SPEED
        self.speed_y = INITIAL_BALL_SPEED
        self.initial_speed_x = INITIAL_BALL_SPEED
        self.initial_speed_y = INITIAL_BALL_SPEED
        self.speed_multiplier = 1

        self.reset()  # Set initial direction randomly

    def move(self):
        self.rect.x += self.speed_x * self.speed_multiplier
        self.rect.y += self.speed_y * self.speed_multiplier

        # Bounce off top and bottom walls
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, BALL_RADIUS)

    def reset(self):
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed_multiplier = 1

        angle = random.uniform(-45, 45)

        if random.choice([True, False]):
            angle += 180

        self.speed_x = self.initial_speed_x * (1 if angle < 90 and angle > -90 else -1)
        self.speed_y = self.initial_speed_y * (1 if angle < 0 else -1)

    def handle_paddle_collision(self, paddle):

        collision_point = (self.rect.centery - paddle.rect.top) / PADDLE_HEIGHT

        angle_factor = (collision_point - 0.5) * 2

        max_angle = 60

        new_angle = angle_factor * max_angle

        self.speed_x = abs(self.initial_speed_x) * (1 if self.speed_x < 0 else -1)
        self.speed_y = self.initial_speed_y * (new_angle / max_angle)

        self.speed_multiplier += BALL_SPEED_INCREMENT / INITIAL_BALL_SPEED


class Score:
    def __init__(self, x, y, color):
        self.score = 0
        self.x = x
        self.y = y
        self.color = color

    def increase(self):
        self.score += 1

    def draw(self, screen):
        score_surface = FONT.render(str(self.score), True, self.color)
        score_rect = score_surface.get_rect(center=(self.x, self.y))
        screen.blit(score_surface, score_rect)


# --- Game Functions ---

def draw_center_line(screen):
    pygame.draw.line(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT), CENTER_LINE_WIDTH)


def handle_ball_paddle_collision(ball, paddle1, paddle2):
    if ball.rect.colliderect(paddle1.rect):
        ball.handle_paddle_collision(paddle1)
    elif ball.rect.colliderect(paddle2.rect):
        ball.handle_paddle_collision(paddle2)


def display_paused_message(screen):
    paused_text = FONT.render("Paused", True, WHITE)
    text_rect = paused_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(paused_text, text_rect)
    pygame.display.flip()


def game_loop(screen, mode, difficulty):
    # --- Game Objects ---
    paddle1 = Paddle(50, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, RED)
    paddle2 = Paddle(SCREEN_WIDTH - 50 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, BLUE)
    ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, WHITE)
    score1 = Score(SCREEN_WIDTH // 4, 50, RED)
    score2 = Score(SCREEN_WIDTH * 3 // 4, 50, BLUE)

    clock = pygame.time.Clock()
    running = True
    paused = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                if event.key == pygame.K_q:
                    running = False

        if not paused:
            # --- Input Handling ---
            keys = pygame.key.get_pressed()
            paddle1.move(keys[pygame.K_w], keys[pygame.K_s])
            if mode == "2P":
                paddle2.move(keys[pygame.K_UP], keys[pygame.K_DOWN])

            # --- AI Logic ---
            if mode == "1P":
                paddle2.ai_move(ball.rect.centery, difficulty)

            # --- Game Logic ---
            ball.move()
            handle_ball_paddle_collision(ball, paddle1, paddle2)

            # --- Scoring ---
            if ball.rect.left <= 0:
                score2.increase()
                ball.reset()
            elif ball.rect.right >= SCREEN_WIDTH:
                score1.increase()
                ball.reset()

            # --- Drawing ---
            screen.fill(BLACK)
            draw_center_line(screen)
            paddle1.draw(screen)
            paddle2.draw(screen)
            ball.draw(screen)
            score1.draw(screen)
            score2.draw(screen)

            pygame.display.flip()
            clock.tick(60)  # Limit to 60 frames per second
        else:
            display_paused_message(screen)


def main_menu(screen):
    title_font = pygame.font.Font(None, 80)
    menu_font = pygame.font.Font(None, 50)

    title_text = title_font.render("Ping Pong", True, WHITE)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))

    mode_1p_text = menu_font.render("1 Player (1P)", True, WHITE)
    mode_1p_rect = mode_1p_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    mode_2p_text = menu_font.render("2 Players (2P)", True, WHITE)
    mode_2p_rect = mode_2p_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))

    difficulty_easy_text = menu_font.render("Easy (1)", True, WHITE)
    difficulty_easy_rect = difficulty_easy_text.get_rect(center=(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 120))

    difficulty_medium_text = menu_font.render("Medium (2)", True, WHITE)
    difficulty_medium_rect = difficulty_medium_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120))

    difficulty_hard_text = menu_font.render("Hard (3)", True, WHITE)
    difficulty_hard_rect = difficulty_hard_text.get_rect(center=(SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT // 2 + 120))

    selected_mode = None
    selected_difficulty = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode_1p_rect.collidepoint(event.pos):
                    selected_mode = "1P"
                elif mode_2p_rect.collidepoint(event.pos):
                    selected_mode = "2P"
                elif difficulty_easy_rect.collidepoint(event.pos):
                    selected_difficulty = 1
                elif difficulty_medium_rect.collidepoint(event.pos):
                    selected_difficulty = 2
                elif difficulty_hard_rect.collidepoint(event.pos):
                    selected_difficulty = 3

        if selected_mode == "2P":
            selected_difficulty = 0
            game_loop(screen, selected_mode, selected_difficulty)
            selected_mode = None
        elif selected_mode == "1P" and selected_difficulty is not None:
            game_loop(screen, selected_mode, selected_difficulty)
            selected_mode = None
            selected_difficulty = None

        screen.fill(BLACK)
        screen.blit(title_text, title_rect)
        screen.blit(mode_1p_text, mode_1p_rect)
        screen.blit(mode_2p_text, mode_2p_rect)

        if selected_mode == "1P":
            screen.blit(difficulty_easy_text, difficulty_easy_rect)
            screen.blit(difficulty_medium_text, difficulty_medium_rect)
            screen.blit(difficulty_hard_text, difficulty_hard_rect)

        pygame.display.flip()


# --- Main Execution ---

if __name__ == "__main__":
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Ping Pong")
    main_menu(screen)
    pygame.quit()
    sys.exit()