import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("图片切片示例")
    
    # 加载拼图（假设有4个32x32的帧横向排列）
    puzzle_sheet = pygame.image.load("puzzle_sheet.jpg")
    
    # 时候选中帧
    is_selected = False
    
    # 鼠标点击位置与帧中心的偏移量
    clicked_pos_to_frame = [0, 0]
    
    # 切片参数
    frame_width = 100
    frame_height = 100
    num_frames = 12
    
    # 提取所有帧
    frames = []
    for i in range(num_frames):
        # 每个帧的位置
        top = i // 3 * frame_height  # 每3帧换行
        left = i % 3 * frame_width  # 每3帧换行
        rect = pygame.Rect(left, top, frame_width, frame_height)
        frame = puzzle_sheet.subsurface(rect)
        # 使用字典，存储每个帧位置信息和帧图像
        frame_info = {
            "rect": rect,
            "frame": frame
        }
        frames.append(frame_info)

    
    # 显示拼图
 
    
    current_frame = 0
    clock = pygame.time.Clock()
    
    while True:
        screen.fill((255, 255, 255))
                # 显示当前帧
        # screen.blit(frames[current_frame], (184, 134))
        
        # 帧动画
        # current_frame = (current_frame + 1) % num_frames
        
        for i in range(num_frames):
            # 将每个帧显示在屏幕上，形成一个3x4的网格
            screen.blit(frames[i]["frame"], frames[i]["rect"])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 鼠标按下事件
            if event.type == pygame.MOUSEBUTTONDOWN:
                length = num_frames
                while length > 0:
                    _rect = frames[length-1]["rect"]
                    print(_rect)
                    if _rect.collidepoint(event.pos):
                        print("Clicked on frame", length-1)
                        frames.append(frames.pop(length-1))
                        is_selected = True
                        # 计算鼠标点击位置与帧中心的偏移量
                        clicked_pos_to_frame[0] = event.pos[0] - _rect.centerx
                        clicked_pos_to_frame[1] = event.pos[1] - _rect.centery
                        break
                    length -= 1
            # 鼠标移动事件
            if event.type == pygame.MOUSEMOTION:
                if is_selected:
                    # 最后一帧移动到鼠标位置，保持点击位置与帧中心的偏移量不变
                    _rect = frames[-1]["rect"]
                    _rect.center = (event.pos[0] - clicked_pos_to_frame[0], event.pos[1] - clicked_pos_to_frame[1])
            
            # 鼠标松开事件
            if event.type == pygame.MOUSEBUTTONUP:
                if is_selected:
                    is_selected = False

                    
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
