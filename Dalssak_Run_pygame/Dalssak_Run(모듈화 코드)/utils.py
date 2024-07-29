import pygame
from settings import RED

# 게임 화면에 표시될 텍스트 모양과 영역 설정
def textObj(text,font): 
    textSurface = font.render(text,True, RED) 
    return textSurface, textSurface.get_rect()

# 게임 화면 정중앙에 text로 지정된 글자를 출력
def dispMessage(surface, text): 
    largeText = pygame.font.Font("freesansbold.ttf",115)  # 폰트, 크기 설정
    TextSurf, TextRect = textObj(text, largeText)         
    TextRect.center = (surface.get_width() // 2, surface.get_height() // 2)
    surface.blit(TextSurf, TextRect)    # 게임판 위에 글자 출력
    pygame.display.update()
    pygame.time.wait(1000)    # 1초동안 출력
