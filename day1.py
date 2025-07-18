import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Flappy Bird Clone")
clock = pygame.time.Clock()

bird = pygame.Rect(100, 200, 20, 20)
bird_vel = 0
pipes = []
score = 0
font = pygame.font.Font(None, 36)

def reset_game():
    global bird, bird_vel, pipes, score
    bird.topleft = (100, 200)
    bird_vel = 0
    pipes.clear()
    score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_vel = -5

    bird_vel += 0.2
    bird.y += bird_vel

    if len(pipes) == 0 or pipes[-1].x < 250:
        gap_y = random.randrange(80, 300)
        pipe_width = 50
        pipe_gap_height = 150
        pipes.append(pygame.Rect(400, 0, pipe_width, gap_y - pipe_gap_height // 2))
        pipes.append(pygame.Rect(400, gap_y + pipe_gap_height // 2, pipe_width, 400 - (gap_y + pipe_gap_height // 2)))

    for pipe in pipes[:]:
        pipe.x -= 2
        if pipe.x < -pipe.width:
            pipes.remove(pipe)
        if pipe.x == bird.x and pipe.height > 0 and pipe.y < 200:
            score += 1  # Fix variable name from `scored` to `score`

    for pipe in pipes:
        if bird.colliderect(pipe):
            reset_game()

    if bird.top < 0 or bird.bottom > 400:
        reset_game()

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 0), bird)
    for pipe in pipes:
        pygame.draw.rect(screen, (0, 255, 0), pipe)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
