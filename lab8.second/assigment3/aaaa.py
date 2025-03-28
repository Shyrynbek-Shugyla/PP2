import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60
clock = pygame.time.Clock()
points = []
last_pos = (0, 0)
w = 3

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
color_mode = BLUE
screen.fill(WHITE)

# Font, Icons and Buttons
welcome_font = pygame.font.SysFont('Arial', 50)
font = pygame.font.SysFont('Arial', 30)
rect_img = pygame.image.load("C:\\Users\\Admin\\Desktop\\pp2\\lab8\\assigment3\\rec.png")
rect_img = pygame.transform.scale(rect_img, (50, 50))
but1_rect = rect_img.get_rect(center=(50, 50))
circle_img = pygame.image.load("C:\\Users\\Admin\\Desktop\\pp2\\lab8\\assigment3\\circle.jpeg")
circle_img = pygame.transform.scale(circle_img, (50, 50))
but2_rect = circle_img.get_rect(center=(150, 50))
eraser_img = pygame.image.load("C:\\Users\\Admin\\Desktop\\pp2\\lab8\\assigment3\\eraser.png")
eraser_img = pygame.transform.scale(eraser_img, (50, 50))
but3_rect = eraser_img.get_rect(center=(350, 50))
red_img = pygame.image.load("C:\\Users\\Admin\\Desktop\\pp2\\lab8\\assigment3\\red.png")
red_img = pygame.transform.scale(red_img, (50, 50))
but_r_rect = red_img.get_rect(center=(450, 50))
green_img = pygame.image.load("C:\\Users\\Admin\\Desktop\\pp2\\lab8\\assigment3\\green.png")
green_img = pygame.transform.scale(green_img, (50, 50))
but_g_rect = green_img.get_rect(center=(550, 50))
blue_img = pygame.image.load("C:\\Users\\Admin\\Desktop\\pp2\\lab8\\assigment3\\blue.png")
blue_img = pygame.transform.scale(blue_img, (50, 50))
but_b_rect = blue_img.get_rect(center=(650, 50))
pencil_img = pygame.image.load("C:\\Users\\Admin\\Desktop\\pp2\\lab8\\assigment3\\pencil.png")
pencil_img = pygame.transform.scale(pencil_img, (50, 50))
but_line_rect = pencil_img.get_rect(center=(250, 50))
saver_img = pygame.image.load("C:\\Users\\Admin\\Desktop\\pp2\\lab8\\assigment3\\saver.png")
saver_img = pygame.transform.scale(saver_img, (90, 60))
but_saver_rect = pencil_img.get_rect(center=(730, 50))

# Triangle button
triangle_img = pygame.image.load("C:\\Users\\Admin\\Desktop\\pp2\\lab8\\assigment1\\triangle.png.jpg")
triangle_img = pygame.transform.scale(triangle_img, (50, 50))
but_triangle_rect = triangle_img.get_rect(center=(450, 150))  # Choose appropriate place

# Boolean variables
line = False
circle = False
rectangle = False
eraser = False
draw = False
erasing = False
triangle = False  # New variable for triangle mode

def drawTriangle(screen, start, end, color):
    x1, y1 = start
    x2, y2 = end

    # Calculate third point for triangle
    x3 = (x1 + x2) // 2
    y3 = y1 - abs(y1 - y2)  # Make the triangle higher

    # Draw the triangle
    pygame.draw.polygon(screen, color, [(x1, y1), (x2, y2), (x3, y3)])

while True:
    clock.tick(FPS)
        
    # Drawing buttons
    pygame.draw.rect(screen, (128, 128, 128), but1_rect)
    screen.blit(rect_img, but1_rect.topleft)
    pygame.draw.rect(screen, (128, 128, 128), but2_rect)
    screen.blit(circle_img, but2_rect.topleft)
    pygame.draw.rect(screen, (128, 128, 128), but3_rect)
    screen.blit(eraser_img, but3_rect.topleft)
    pygame.draw.rect(screen, (128, 128, 128), but_r_rect)
    screen.blit(red_img, but_r_rect.topleft)
    pygame.draw.rect(screen, (128, 128, 128), but_g_rect)
    screen.blit(green_img, but_g_rect.topleft)
    pygame.draw.rect(screen, (128, 128, 128), but_b_rect)
    screen.blit(blue_img, but_b_rect.topleft)
    pygame.draw.rect(screen, (128, 128, 128), but_line_rect)
    screen.blit(pencil_img, but_line_rect.topleft)
    pygame.draw.rect(screen, (128, 128, 128), but_saver_rect)
    screen.blit(saver_img, but_saver_rect.topleft)
    pygame.draw.rect(screen, (128, 128, 128), but_triangle_rect)
    screen.blit(triangle_img, but_triangle_rect.topleft)  # Draw triangle button
    pygame.display.flip()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_r]:
        color_mode = RED
    elif pressed_keys[pygame.K_g]:
        color_mode = GREEN
    elif pressed_keys[pygame.K_b]:
        color_mode = BLUE
        
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            exit()
                
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if but1_rect.collidepoint(event.pos):
                line = False
                rectangle = True
                circle = False
                eraser = False
                triangle = False
            if but2_rect.collidepoint(event.pos):
                line = False
                rectangle = False
                circle = True
                eraser = False
                triangle = False
            if but3_rect.collidepoint(event.pos):
                line = False
                rectangle = False
                circle = False
                eraser = True
                triangle = False
            if but_line_rect.collidepoint(event.pos):
                line = True
                rectangle = False
                circle = False
                eraser = False
                triangle = False
            if but_b_rect.collidepoint(event.pos):
                color_mode = BLUE
            if but_g_rect.collidepoint(event.pos):
                color_mode = GREEN
            if but_r_rect.collidepoint(event.pos):
                color_mode = RED
            if but_saver_rect.collidepoint(event.pos):
                pygame.image.save(screen, 'paint.png')
            if but_triangle_rect.collidepoint(event.pos):  # Select triangle mode
                line = False
                rectangle = False
                circle = False
                eraser = False
                triangle = True

        # Drawing tools logic
        if triangle:
            if event.type == pygame.MOUSEBUTTONDOWN:
                last_pos = pos  # Starting point of triangle
            if event.type == pygame.MOUSEBUTTONUP:
                drawTriangle(screen, last_pos, pos, color_mode)  # Draw triangle

        pygame.display.update()
