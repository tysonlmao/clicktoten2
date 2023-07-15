import pygame
import sys
import webbrowser
import random

# Initialize Pygame
pygame.init()

# Set up the window
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("click gam")

# Set up variables
click_count = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Load the anime girl image
anime_girl_image = pygame.image.load("./assets/anime_girl.png")
anime_girl_rect = anime_girl_image.get_rect()

# Set up the camera
camera_offset = pygame.math.Vector2(window_size) / 2
camera_speed = 0.1

# Load the spinning fish GIF
fish_gif = pygame.image.load("./assets/fish.gif")
fish_rect = fish_gif.get_rect()
fish_rect.bottomright = (window_size[0] - 10, window_size[1] - 10)
fish_angle = 0

# Load the background music
pygame.mixer.music.load("./assets/background_music.mp3")
pygame.mixer.music.play(-1)  # Play the music on a loop

# Load the error sounds
error_sounds = [
    pygame.mixer.Sound("./assets/error1.wav"),
    pygame.mixer.Sound("./assets/error2.wav"),
    pygame.mixer.Sound("./assets/error3.wav")
]

# Function to change the background color
def change_background_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Function to display the title screen
def show_title_screen():
    title_font = pygame.font.Font(None, 72)
    instruction_font = pygame.font.Font(None, 36)
    title_text = title_font.render("Click Game", True, (0, 0, 0))
    instruction_text = instruction_font.render("Press any key to start", True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(window_size[0] // 2, window_size[1] // 2))
    instruction_rect = instruction_text.get_rect(center=(window_size[0] // 2, window_size[1] // 2 + 100))
    screen.fill((255, 255, 255))
    screen.blit(title_text, title_rect)
    screen.blit(instruction_text, instruction_rect)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

# Show the title screen
show_title_screen()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_count += 1
                # add someting that happens on click here
            if click_count == 69:
                webbrowser.open("https://www.pornhub.com")
                print("opening pornuhb.com")
            else:
                screen.fill(change_background_color())
                anime_girl_rect.center = event.pos - camera_offset  # Set the image position to the click position
                error_sound = random.choice(error_sounds)
                error_sound.play()

    # Clear the screen
    screen.fill(change_background_color())

    # Display the click count
    text = font.render(f"Clicks: {click_count}", True, (0, 0, 0))
    text_rect = text.get_rect(center=(window_size[0] // 2, 50))
    screen.blit(text, text_rect)

    # Draw the anime girl image relative to the camera
    anime_girl_position = anime_girl_rect.move(camera_offset)
    screen.blit(anime_girl_image, anime_girl_position)

    # Rotate and draw the spinning fish GIF
    fish_rotated = pygame.transform.rotate(fish_gif, fish_angle)
    fish_rect = fish_rotated.get_rect(center=fish_rect.center)
    screen.blit(fish_rotated, fish_rect)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

    # Move the camera towards the anime girl
    camera_offset += (anime_girl_rect.center - camera_offset) * camera_speed

    # Update the rotation angle of the fish
    fish_angle += 1
    if fish_angle >= 360:
        fish_angle = 0
