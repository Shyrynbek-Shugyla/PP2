import pygame 
import random
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

#paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)


#Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

#Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

#Catching sound
collision_sound = pygame.mixer.Sound('/Users/damirnurmagambetov/Desktop/PP2_Labs/Lab_8/arkanoid/catch.mp3')

#Function that detect collision
def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

block_list = []
color_list = []
rows = 4
columns = 10
shrink_rate = 3
initial_paddle = paddleW
last_time = pygame.time.get_ticks()

#block settings
for i in range(rows):
    for j in range(columns):
        if j%4 == 3:
            block = pygame.Rect(10 + 120*j, 50 + 70 * i, 100, 50)
            color = (128, 128, 128)
        else:
            block = pygame.Rect(10 + 120 * j, 50 + 70 * i, 100, 50)
            color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
            if ((j > random.randrange(0, 11) and j < random.randrange(0, 11)) and i > random.randrange(0, 4)) or ((j > random.randrange(0, 4) and j < random.randrange(0, 11)) and i > random.randrange(0, 7)):
                color = (255, 255, 0)
        block_list.append(block)
        color_list.append(color)


#Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

#Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)

    #Convert milliseconds to seconds by dividing by 1000
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - last_time) / 1000
    last_time = current_time

    # Increase ball speed over time
    ballSpeed += elapsed_time * 0.1
    
    # Shrink paddle over time
    paddleW -= elapsed_time * shrink_rate
    paddleW = max(paddleW, ballRadius * 4) 
    
    #Drawing blocks
    for color, block in enumerate(block_list):
        pygame.draw.rect(screen, color_list[color], block)
        if color_list[color] == (255, 255, 0):
            pygame.draw.circle(screen, (0, 0, 0), block.center, 20)

    #drawing the paddle
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    #drawing the ball
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    #Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    #Collision left 
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    #Collision top
    if ball.centery < ballRadius + 50: 
        dy = -dy
    #Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    #Collision blocks
    hitIndex = ball.collidelist(block_list)

    if hitIndex != -1:
        hit_block = block_list[hitIndex]
        hit_color = color_list[hitIndex]
        if hit_color != (128, 128, 128):
            hit_block = block_list.pop(hitIndex)
            hit_color = color_list.pop(hitIndex)
            dx, dy = detect_collision(dx, dy, ball, hit_block)
            game_score += 1
            collision_sound.play()
            if hit_color == (255, 255, 0):
                paddleW += 40
                paddle.width = int(paddleW)
        else:
            dx, dy = detect_collision(dx, dy, ball, hit_block)
        
    #Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    
    #Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255,255, 255))
        screen.blit(wintext, wintextRect)

    #Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed


    pygame.display.flip()
    clock.tick(FPS)