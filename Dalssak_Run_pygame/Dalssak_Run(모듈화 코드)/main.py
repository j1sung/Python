import pygame
from settings import *
from game_objects import Barrier, Snowball, Ice
from utils import dispMessage

# 게임을 초기화하고 시작하는 함수
def initGame():
    global gamepad, Dalssak, clock, background1, background2, menu_background, life, health, start_ticks
    global explosion_sound

    pygame.init() # PyGame 라이브러리 초기화
    gamepad = pygame.display.set_mode((pad_width, pad_height)) # 게임판 크기 설정
    pygame.display.set_caption("PyFlying")                     # 게임판 타이틀 설정
    clock = pygame.time.Clock() # 게임의 초당 프레임 설정을 위한 클락 생성
    
    Dalssak = pygame.image.load("assets/Dalssak.png")                 # 게임 캐릭터 설정
    background1 = pygame.image.load("assets/background.png")          # 게임 배경 설정
    background2 = background1.copy()                           # 게임 배경 복사
    life = pygame.image.load("assets/heart.png")                      # 게임 생명 설정
    explosion_sound = pygame.mixer.Sound("assets/explosion.wav")      # 부딪힐 때 나는 소리
    pygame.mixer.music.load("assets/intro.mp3")                       # 게임 메뉴 노래 설정
    pygame.mixer.music.set_volume(0.07)                        # 볼륨 0.07 지정
    pygame.mixer.music.play(-1)                                # 메뉴 노래 플레이
    menu_background = pygame.image.load("assets/menu.png")            # 메뉴 배경 설정

    gamepad.blit(menu_background,(0,0))     # 배경 이미지의 좌상단 모서리의 x좌표, 최초값은 0
    crashed = False
    while not crashed:
      for event in pygame.event.get():                # 이벤트가 발생 했을 시
            if event.type == pygame.MOUSEBUTTONDOWN:  # 마우스 버튼 이벤트가 발생 했을 때
                x,y = pygame.mouse.get_pos()          # 마우스가 눌린 위치를 받아옴
                if x >= 400 and x <= 677:             # 마우스를 누른 위치가 버튼이 그려진 x축 범위안에 들어 왔는지 판단
                        if y >= 335 and y <= 444:     # y축 범위 판단 후, 버튼 1이 눌렸을 경우(game start 버튼)
                            
                            start_ticks = pygame.time.get_ticks()  # 시작 시간 >> tick을 받아옴
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load("assets/bgm.mp3")     # intro -> bgm으로 노래 변경
                            pygame.mixer.music.set_volume(0.1)    # 볼륨 0.1 설정
                            pygame.mixer.music.play(-1)
                            runGame()                 # 게임 구동 함수 호출, game start버튼이 눌렸음을 표시
                        if y >= 490 and y <= 600:     # y축 범위 판단 후, 버튼 2이 눌렸을 경우(game quit 버튼)
                            crashed = True            # 반복문 탈출을 위해 충돌여부를 참으로 만듬
                            pygame.quit()             # pygame을 종료시킴
                            quit()                    # 스크립트 종료
      pygame.display.update()
      clock.tick(60)  # 60 프레임 설정
      

# 실제 게임이 구동되는 함수
def runGame(): 
    global gamepad, Dalssak, clock, background1, background2, total_time, start_ticks, RED
    global barrier, snowball, ice,life, health, snowball_height, pad_height, life_height, time

    pygame.mixer.music.unpause()  # 중단했던 게임bgm 다시 플레이


    x=pad_height*0.1  # 캐릭터의 최초 위치
    y=pad_height*0.4  # 캐릭터의 최초 위치
    x_change = 0      # x의 좌표 변화
    y_change = 0      # y의 좌표 변화

    background1_x = 0 # 배경 이미지의 좌상단 모서리의 x좌표, 최초값은 0
    background2_x = background_width # 배경 이미지 복사본을 배경 이미지 원본 바로 다음에 위치시키도록 좌표 지정

    barrier = Barrier()
    snowball = Snowball()
    ice = Ice()

    crashed = False
    while not crashed:
        for event in pygame.event.get():  # 키보드의 위 화살표와 아래 화살표 키를 누르면 비행기가 위 아래로 12픽셀씩 움직인다.
            if event.type == pygame.QUIT: # pygame의 X버튼을 누르면 while문 밖으로 빠져나가 게임 종료
                crashed = True

            if event.type == pygame.KEYDOWN: # 키가 눌렸을 때
                if event.key==pygame.K_UP:   # 위쪽 화살표 키 눌렀을 때
                    y_change=-12
                elif event.key==pygame.K_DOWN: # 아래쪽 화살표 키 눌렀을 때
                    y_change = 12
                elif event.key==pygame.K_LEFT: # 왼쪽 화살표 키 눌렀을 때
                    x_change = -15
                elif event.key==pygame.K_RIGHT: # 오른쪽 화살표 키 눌렀을 때
                    x_change = 15
                    
            if event.type == pygame.KEYUP:   # 키가 떼어졌을 때
                if event.key in (pygame.K_UP, pygame.K_DOWN): # 위쪽 화살표 키, 아래 화살표 키 안누를 때
                    y_change = 0             # 움직이지 않는다
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT): # 왼쪽 화살표 키, 오른쪽 화살표 키 안누를 때
                    x_change = 0             # 움직이지 않는다


        y += y_change # 키보드 입력에 따라 캐릭터의 y좌표를 변경
        x += x_change # 키보드 입력에 따라 캐릭터의 y좌표를 변경

        # 게임판 범위 안에서만 움직이게 가두기
        # 캐릭터 높이 설정
        if y<0:
            y=0
        elif y>pad_height-Dalssak_height:
            y=pad_height-Dalssak_height

        # 캐릭터 너비 설정
        if x<0:
            x=0
        elif x>pad_width-Dalssak_width:
            x=pad_width-Dalssak_width

            
        gamepad.fill(WHITE)
        
        background1_x -= 3 # 배경 이미지를 왼쪽으로 3픽셀 만큼 이동
        background2_x -= 3  # 배경 이미지 복사본을 왼쪽으로 3픽셀 만큼 이동

        if background1_x == -background_width: # 배경 이미지가 게임판에서 사라지면 그 위치를 배경 이미지 복사본 오른쪽으로 다시 위치시킴
            background1_x = background_width   # 배경 이미지 복사본이 게임판에서 완전히 사라지면 배경 이미지 오른쪽으로 다시 위치시킴
            
        if background2_x == -background_width:
            background2_x = background_width
            
        gamepad.blit(background1, (background1_x, 0))
        gamepad.blit(background2, (background2_x, 0))

        # 폰트 정의  Font(None으로 하면 알아서 기본값으로 출력, 글씨 크기)
        game_font = pygame.font.Font(None, 40) 

        # 경과 시간 계산(milisecond라 1000으로 나눠 1초로 표시)
        # start_ticks 은 고정, pygame.time.get_ticks()는 점점 커지는 듯
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

        #현재 남은 시간
        result_time = int(total_time - elapsed_time)

        # render(시간 표현글자, True, (색상 rgb 코드))
        timer = game_font.render("Time : {}".format(result_time), True, RED)

        # blit(화면에 타이머 출력, ( x, y 좌표))
        gamepad.blit(timer, (10, 10))

        # 장애물을 날아오게 함
        barrier.update()
        snowball.update()
        ice.update()

        # 캐릭터와 장애물이 부딪혔는지 확인
        if barrier.rect.colliderect((x, y, Dalssak_width, Dalssak_height)) or \
           snowball.rect.colliderect((x, y, Dalssak_width, Dalssak_height)) or \
           ice.rect.colliderect((x, y, Dalssak_width, Dalssak_height)):
            health -= 1 # 부딪히면 생명 1개 사라짐

            if health == 0: # 장애물과 부딪혔을 때 생명이 0이면 게임오버, 아니면 충돌 함수 호출
                    gameOver()

            pygame.mixer.music.pause()
            pygame.mixer.Sound.play(explosion_sound).set_volume(0.03)
            dispMessage(gamepad, "Crashed!")
            runGame()
            
        # 시간 초과했을때 승리
        if health > 0 and result_time <= 0:
            victory()

        # 게임판에 이미지 파일들 출력
        gamepad.blit(Dalssak, (x, y))
        barrier.draw(gamepad)
        snowball.draw(gamepad)
        ice.draw(gamepad)
            

        for i in range(0,health):  # 남은 생명 게임판에 출력
            gamepad.blit(life, (i * 60, pad_height - life_height))
            
        pygame.display.update() 
        clock.tick(60) # 60 프레임 설정
        
    pygame.quit() # pygame 종료
    quit()        # 스크립트 창 닫기

# 승리했을 때 
def victory():
    global gamepad, health
    health = 4  # 다시 생명 4개로 설정
    pygame.mixer.music.stop()               # 게임 bgm -> 승리 bgm으로 전환
    pygame.mixer.music.load("assets/victory.mp3")  
    pygame.mixer.music.set_volume(0.03)
    pygame.mixer.music.play(-1)
    dispMessage(gamepad, "Victory!")                 # Victory! 출력
    pygame.time.wait(8700)                              # 승리 bgm 8.7초 동안 틀기
    pygame.mixer.music.stop()
    initGame()                              # 다시 메뉴로 돌아가기

# 게임에서 졌을 때
def gameOver():
    global gamepad, health, total_time
    health = 4  # 다시 생명 4개로 설정
    pygame.mixer.music.stop()               # 게임 bgm -> 게임오버 bgm으로 전환
    pygame.mixer.music.load("assets/gameover.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    dispMessage(gamepad, "GAME OVER")                # GAME OVER 출력
    pygame.time.wait(6200)                  # 승리 bgm 6.2초 동안 틀기
    pygame.mixer.music.stop()
    initGame()                              # 다시 메뉴로 돌아가기

if __name__ == "__main__":
    initGame()
