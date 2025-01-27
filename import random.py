import random
import curses

# Game settings
HEIGHT = 24
WIDTH = 24
SNAKE_START_LENGTH = 1
SNAKE_SPEED = 100  # Milliseconds between each game tick

# Initialize the game
stdscr = curses.initscr()
curses.curs_set(0)
stdscr.nodelay(1)
stdscr.timeout(SNAKE_SPEED)

# Create the game window
window = curses.newwin(HEIGHT, WIDTH, 0, 0)
window.keypad(1)
window.border(0)
window.nodelay(1)

# Initial snake position and direction
snake_x = WIDTH // 2
snake_y = HEIGHT // 2
snake_direction = curses.KEY_RIGHT

# Initialize the snake and food positions
snake = [(snake_y, snake_x)]
food = []
score = 0

# Function to generate new food
def generate_food():
    while True:
        food_x = random.randint(1, WIDTH - 2)
        food_y = random.randint(1, HEIGHT - 2)
        if (food_y, food_x) not in snake and (food_y, food_x) not in food:
            return (food_y, food_x)

# Game loop
while True:
    # Display the snake
    for y, x in snake:
        window.addch(y, x, curses.ACS_BLOCK)

    # Display the food
    for y, x in food:
        window.addch(y, x, curses.ACS_DIAMOND)

    # Get user input
    key = window.getch()

    # Change the snake's direction based on user input
    if key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
        snake_direction = key

    # Calculate new snake position
    if snake_direction == curses.KEY_UP:
        new_head = (snake[0][0] - 1, snake[0][1])
    elif snake_direction == curses.KEY_DOWN:
        new_head = (snake[0][0] + 1, snake[0][1])
    elif snake_direction == curses.KEY_LEFT:
        new_head = (snake[0][0], snake[0][1] - 1)
    elif snake_direction == curses.KEY_RIGHT:
        new_head = (snake[0][0], snake[0][1] + 1)

    # Check if the snake hits the wall or itself
    if (
        new_head[0] in [0, HEIGHT - 1]
        or new_head[1] in [0, WIDTH - 1]
        or new_head in snake[1:]
    ):
        break

    # Check if the snake eats the food
    if new_head in food:
        food.remove(new_head)
        score += 1
        snake.append((snake[-1][0], snake[-1][1]))  # Grow the snake
    else:
        snake.pop()

    snake.insert(0, new_head)

    # Generate new food if there is none
    if not food:
        food.append(generate_food())

    # Clear the window
    window.erase()
    window.border(0)

# Game over
stdscr.addstr(HEIGHT // 2, WIDTH // 2 - 4, "Game Over")
stdscr.addstr(HEIGHT // 2 + 1, WIDTH // 2 - 8, f"Score: {score}.refresh()
curses.napms(3000)  # Display the game over screen for 3 seconds

# Cleanup and exit
curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()
