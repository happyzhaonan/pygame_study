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
    # 碰撞的帧索引
    colliding_frame = []
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
            # 为碰撞的帧添加红色边框
            if i in colliding_frame:
                pygame.draw.rect(screen, (255, 0, 0), frames[i]["rect"], 1)
        # 如果正在拖动且有碰撞，用绿色边框标记被拖动的帧
        if is_selected :
            pygame.draw.rect(screen, (0, 255, 0), frames[-1]["rect"], 1)
        
        # 绘制一个矩形画框,大小等于整个图像
        pygame.draw.rect(screen, (0, 0, 0), puzzle_sheet.get_rect(), 1)
        
        
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

                    # 碰撞检测：检查当前拖动的帧是否与其他帧碰撞
                    colliding_frame = []
                    current_framerect = frames[-1]["rect"]
                    for i in range(num_frames-1):
                        if current_framerect.colliderect(frames[i]["rect"]):
                            colliding_frame.append(i)
                    
            # 鼠标松开事件
            if event.type == pygame.MOUSEBUTTONUP:
                if is_selected:
                    is_selected = False
                    colliding_frame = []
                    
                    # 让移动到画框内的帧吸附到整数位置
                    # 先判断时候在画框内
                    _rect = puzzle_sheet.get_rect()
                    if _rect.collidepoint(event.pos):
                        _rect = frames[-1]["rect"]
                        _rect.left = round(_rect.left / frame_width) * frame_width
                        _rect.top = round(_rect.top / frame_height) * frame_height
                    
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
