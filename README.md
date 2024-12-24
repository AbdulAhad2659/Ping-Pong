# Ping Pong Game


This is a feature-rich Ping Pong game developed in Python using the Pygame library. It offers both single-player (against an AI with adjustable difficulty) and two-player modes, making it a fun and engaging experience for everyone.

## Features

-   **1-Player and 2-Player Modes:** Play against a challenging AI or a friend on the same computer.
-   **Adjustable AI Difficulty:** Choose from Easy, Medium, or Hard difficulty levels in 1-player mode. The AI dynamically adjusts its strategy based on the selected difficulty.
-   **Power-ups:**
    -   **Speed Up:** Temporarily increases the ball's speed when hit.
    -   **Big Paddle:** Temporarily increases the paddle's height, making it easier to hit the ball.
-   **Sound Effects:** Immersive sound effects for paddle hits, wall bounces, scoring, and power-up activation.
-   **Customizable Visuals:**
    -   Option to use images for paddles and the ball.
    -   Optional background image for a more visually appealing experience.
-   **Smooth Gameplay:** Maintains a high frame rate for a fluid and responsive gaming experience.
-   **Pause Functionality:** Pause the game at any time using the 'P' key.
-   **Intuitive Controls:** Easy-to-learn controls for both players.

## Requirements

-   Python 3.x
-   Pygame library

## Installation

1. **Install Python:** If you don't have Python installed, download and install the latest version from [python.org](https://www.python.org/).
2. **Install Pygame:** Open your terminal or command prompt and run:

    ```bash
    pip install pygame
    ```

## Getting Started

1. **Clone the Repository:**

    ```bash
    git clone <https://github.com/AbdulAhad2659/Ping-Pong> 
    ```
2. **Download Assets:**
    -   Download the required sound and image assets:
        -   `paddle_hit.wav`
        -   `score.wav`
        -   `wall_hit.wav`
        -   `powerup.wav`
        -   `paddle.png`
        -   `ball.png`
        -   `speed_up.png`
        -   `big_paddle.png`
        -   `background.jpg` (optional)
    -   Place these files in the same directory as the `improved_ping_pong.py` script.
    -   You can find free assets online or create your own.
3. **Run the Game:**

    ```bash
    python improved_ping_pong.py
    ```

## Controls

| Action          | Player 1 (Left) | Player 2 (Right) |
| --------------- | --------------- | ---------------- |
| Move Up         | W               | Up Arrow         |
| Move Down       | S               | Down Arrow       |
| Pause           | P               | P                |
| Quit            | Q               | Q                |

## Gameplay

1. **Main Menu:** When you start the game, you'll see the main menu.
    -   Click on "1 Player (1P)" to play against the AI.
    -   Click on "2 Players (2P)" to play against another player.
2. **Difficulty Selection (1-Player Mode):**
    -   If you choose 1-player mode, you'll be prompted to select a difficulty:
        -   Easy (1)
        -   Medium (2)
        -   Hard (3)
3. **Game Start:** The game begins with the ball served from the center of the screen.
4. **Objective:** Use your paddle to hit the ball back to the opponent's side. If the opponent misses, you score a point.
5. **Power-ups:** Randomly appearing power-ups can be collected by hitting them with the ball or your paddle.
6. **Winning:** The first player to reach a certain score (determined by the game settings) wins.

## Customization

-   **Images:** You can replace the default `paddle.png`, `ball.png`, `background.jpg`, `speed_up.png` and `big_paddle.png` files with your own images to customize the look of the game. Make sure to keep the same file names or modify the code accordingly.
-   **Sounds:** Similarly, replace the `.wav` files with your preferred sound effects.
-   **Difficulty:** Adjust the AI's difficulty by changing the `difficulty` parameter in the `ai_move()` function in the `Paddle` class.
-   **Game Settings:** Modify constants like `PADDLE_SPEED`, `INITIAL_BALL_SPEED`, `BALL_SPEED_INCREMENT`, `POWERUP_SPAWN_CHANCE`, etc., to change the game's behavior.

## Code Structure

-   **`Paddle` Class:** Represents a player's paddle. Handles movement, drawing, and power-up effects.
-   **`Ball` Class:** Represents the ball. Manages movement, collision detection, drawing, and power-up effects.
-   **`Score` Class:** Tracks and displays the score for each player.
-   **`PowerUp` Class:** Represents a power-up. Handles its position, type, and drawing.
-   **`game_loop()` Function:** The main game loop that handles events, updates game objects, and renders the game.
-   **`main_menu()` Function:** Displays the main menu and handles mode/difficulty selection.

## Contributing

Contributions to this project are welcome! If you'd like to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear messages.
4. Push your branch to your forked repository.
5. Submit a pull request to the main repository.

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details. (You should include a LICENSE file in your repository if you want to specify a license).

## Acknowledgments

-   This game was built using the [Pygame](https://www.pygame.org/) library.
-   Special thanks to the creators of the sound effects and images used in this game (if you used assets from others, give them proper credit here).

## Future Enhancements

-   **Advanced AI:** Implement a more intelligent AI using prediction, machine learning, or other advanced techniques.
-   **More Power-ups:** Add a wider variety of power-ups with different effects.
-   **Tournament Mode:** Create a tournament mode for single-player or even multiplayer.
-   **Network Play:** Enable online multiplayer over a network.
-   **Improved Graphics:** Add more visually appealing graphics, animations, and particle effects.
-   **Mobile Port:** Port the game to mobile devices using a framework like Kivy.

Enjoy the game!
