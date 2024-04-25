import pygame  # Importing pygame library
import math
import colors as clr
pygame.init()  # Initializing pygame

# Setting up some useful constants
WIDTH = 800
HEIGHT = 600
colorWHITE = (255, 255, 255)

# Creating the main display screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Creating a base layer for easy screen updates
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill(colorWHITE)
screen.fill(colorWHITE)
pygame.display.set_caption("Paint")

# Creating a clock object to control frame rate
clock = pygame.time.Clock()

# Boolean to track left mouse button press
LMBpressed = False
THICKNESS = 5  # Thickness of drawing lines

# Variables to track current and previous mouse positions
currX = 0
currY = 0

prevX = 0
prevY = 0

# Drawing mode (rectangle, circle, right triangle, equilateral triangle, eraser)
mode = "rectangle"
color_mode = "red"  # Initial drawing color

# Function to calculate a rectangle based on mouse positions
def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

# Function to calculate the vertices of an equilateral triangle
def calculate_equilateral_triangle(x1, y1, x2, y2):
    side_length = abs(x2 - x1)  # Calculate side length based on mouse positions
    height = int(side_length * (3 ** 0.5) / 2)  # Calculate height of equilateral triangle
    if y1<y2:
        return ((x1, y1), ((x1 + x2) // 2, y1 + height), (x2, y1))  # Return vertices of triangle
    else:
        return ((x1, y1), ((x1 + x2) // 2, y1 - height), (x2, y1))  # Return vertices of triangle

def draw_rhombus(screen, color, rect):
    points = [rect.midtop, rect.midright, rect.midbottom, rect.midleft]
    pygame.draw.polygon(screen, color, points,THICKNESS)  # Draw the rhombus

# Game loop status
done = False

# Main game loop
while not done:

    # Check for keyboard events
    pressed = pygame.key.get_pressed()
    shift_held = pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]

    for event in pygame.event.get():
        if LMBpressed:
            screen.blit(base_layer, (0, 0))  # Refresh the screen if left mouse button is pressed
        if event.type == pygame.QUIT:
            done = True  # Exit the game loop if the window is closed

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Record previous mouse position when left mouse button is pressed
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]

        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                # Update current mouse position during mouse motion
                currX = event.pos[0]
                currY = event.pos[1]

                # Draw based on the selected mode (rectangle, circle, right triangle, equilateral triangle, eraser)
                if mode == "rectangle":
                    pygame.draw.rect(screen, color_mode, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                elif mode == "circle":
                    pygame.draw.ellipse(screen, color_mode, pygame.Rect(min(currX,prevX),min(currY,prevY),abs(currX-prevX),abs(currY-prevY)),THICKNESS)#(prevX+currX)/2, (prevY+currY)/2), currX - prevX, THICKNESS)
                elif mode == "righttriangle":
                    pygame.draw.polygon(screen, color_mode, ((prevX, prevY), (prevX, currY), (currX, currY)), THICKNESS)
                elif mode == "triangle":
                    pygame.draw.polygon(screen, color_mode, calculate_equilateral_triangle(prevX, prevY, currX, currY), THICKNESS)
                elif mode == "rhombus":
                    rect1 = calculate_rect(prevX, prevY, currX, currY)
                    draw_rhombus(screen, color_mode, rect1)
                elif mode == "square":
                    # Calculate the coordinates for the square based on mouse positions
                    top_left = (min(prevX, currX), min(prevY, currY))
                    side_length = min(abs(currX - prevX), abs(currY - prevY))
                    # Draw the square using the calculated coordinates
                    pygame.draw.rect(screen, color_mode, (top_left[0], top_left[1], side_length, side_length), THICKNESS)
                elif mode == "eraser":
                    pygame.draw.circle(screen, color_mode, (currX, currY), THICKNESS)
                    base_layer.blit(screen, (0, 0))  # Update base layer for eraser mode

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            # Record current mouse position when left mouse button is released
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]

            # Draw based on the selected mode when mouse button is released
            if mode == "rectangle":
                pygame.draw.rect(screen, color_mode, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                base_layer.blit(screen, (0, 0))  # Update base layer after drawing rectangle
            elif mode == "circle":
                # pygame.draw.circle(screen, color_mode, (prevX, prevY), abs(currX - prevX), THICKNESS)
                pygame.draw.ellipse(screen, color_mode, pygame.Rect(min(currX,prevX),min(currY,prevY),abs(currX-prevX),abs(currY-prevY)),THICKNESS)#(prevX+currX)/2, (prevY+currY)/2), currX - prevX, THICKNESS)
                base_layer.blit(screen, (0, 0))  # Update base layer after drawing circle
            elif mode == "righttriangle":
                pygame.draw.polygon(screen, color_mode, ((prevX, prevY), (prevX, currY), (currX, currY)), THICKNESS)
                base_layer.blit(screen, (0, 0))  # Update base layer after drawing right triangle
            elif mode == "triangle":
                pygame.draw.polygon(screen, color_mode, calculate_equilateral_triangle(prevX, prevY, currX, currY), THICKNESS)
                base_layer.blit(screen, (0, 0))  # Update base layer after drawing equilateral triangle
            elif mode == "rhombus":
                rect1 = calculate_rect(prevX, prevY, currX, currY)
                draw_rhombus(screen, color_mode, rect1)
                base_layer.blit(screen, (0, 0))
            elif mode == "square":
                # Calculate the coordinates for the square based on mouse positions
                top_left = (min(prevX, currX), min(prevY, currY))
                side_length = min(abs(currX - prevX), abs(currY - prevY))
                # Draw the square using the calculated coordinates
                pygame.draw.rect(screen, color_mode, (top_left[0], top_left[1], side_length, side_length), THICKNESS)
                base_layer.blit(screen, (0, 0)) 


        if event.type == pygame.KEYDOWN:
            # Handle key press events
            if event.key == pygame.K_UP:
                THICKNESS += 1  # Increase line thickness
            if event.key == pygame.K_DOWN:
                THICKNESS -= 1  # Decrease line thickness
            if event.key == pygame.K_ESCAPE:
                done = True  # Exit the game loop on ESC key press

            # Change drawing mode based on key press (rectangle, circle, right triangle, equilateral triangle, eraser)
            if event.key == pygame.K_c:
                mode = "circle"
            if event.key == pygame.K_r and not shift_held:
                mode = "rectangle"
            if event.key == pygame.K_t:
                mode = "righttriangle"
            if event.key == pygame.K_v:
                mode = "triangle"
            if event.key == pygame.K_h:
                mode = "rhombus"
            if event.key == pygame.K_e:
                mode = "eraser"
                color_mode = colorWHITE
            if event.key == pygame.K_s:
                mode = "square"

            # Change drawing color based on key press (red, blue, green, black)
            if event.key == pygame.K_r and shift_held:
                color_mode = clr.colorRED
            if event.key == pygame.K_b and shift_held:
                color_mode = clr.colorBLUE
            if event.key == pygame.K_g and shift_held:
                color_mode = clr.colorGREEN
            if event.key == pygame.K_k and shift_held:
                color_mode = clr.colorBLACK
            

    pygame.display.flip()  # Update the display
    clock.tick(10000000)  # Cap the frame rate to avoid excessive CPU usage