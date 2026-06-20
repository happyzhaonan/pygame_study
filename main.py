import math
from random import random, randint
from turtle import speed

import pygame
import sys

def main():
    pygame.init()
    size = width, height = 640, 480
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Basic")
    color = (255, 255, 255)
    screen.fill(color)
    pygame.display.flip()
    
    ball = pygame.image.load("ball.png")
    ball = pygame.transform.scale(ball, (50, 50))
    ball_rect = ball.get_rect()
    speed = [10, 10]
    clock = pygame.time.Clock()
    
    while True:
        clock.tick(24 )  # Limit to 24 frames per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Mouse button down at", event.pos)
                # 随机改变运动轨迹, 点击鼠标后, 球会随机改变运动方向
                # 使用sin函数改变运动方向
                # 方向是随机的, 但是速度不变, 只是改变运动方向
                angle = random() * 2 * math.pi
                speed_magnitude = math.sqrt(speed[0] ** 2 + speed[1] ** 2)
                speed[0] = speed_magnitude * math.cos(angle)
                speed[1] = speed_magnitude * math.sin(angle)
        print(ball_rect)
        ball_rect.move_ip(speed)
        if ball_rect.left < 0 or ball_rect.right > width:
            speed[0] = -speed[0]
        if ball_rect.top < 0 or ball_rect.bottom > height:
            speed[1] = -speed[1]
        
        
        screen.fill(color)
        screen.blit(ball, ball_rect)
        pygame.display.flip()
        
    pygame.quit()


if __name__ == "__main__":
    main()
