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
    is_clicked = False
    clicked_pos_to_ball = [0, 0]
    
    while True:
        clock.tick(60 )  # Limit to 60 frames per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Mouse button down at", event.pos)
                # 如果鼠标点击在球的范围内，改变is_clicked的值
                if ball_rect.collidepoint(event.pos):
                    is_clicked = True
                    clicked_pos_to_ball[0] = event.pos[0] - ball_rect.center[0]
                    clicked_pos_to_ball[1] = event.pos[1] - ball_rect.center[1]
                
            # 鼠标移动时候，打印坐标
            if event.type == pygame.MOUSEMOTION:
                print("Mouse moved to", event.pos)
                if is_clicked:
                    # 如果is_clicked为True，更新球的位置，使其中心跟随鼠标
                    new_center_x = event.pos[0] - clicked_pos_to_ball[0]
                    new_center_y = event.pos[1] - clicked_pos_to_ball[1]
                    ball_rect.center = (new_center_x, new_center_y)
            # 鼠标松开时候，打印坐标
            if event.type == pygame.MOUSEBUTTONUP:
                print("Mouse button up at", event.pos)
                is_clicked = False
        # print(ball_rect)
        # ball_rect.move_ip(speed)
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
