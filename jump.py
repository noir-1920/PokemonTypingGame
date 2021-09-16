import pygame
import random
import time
pygame.init()
Wid = 800
Hei = 600
Black=(0,0,0)
Disp = pygame.display.set_mode((Wid, Hei))#setting game display Size
pygame.display.set_caption('POKEMON- Keyboard Jump Game')
Bg = pygame.image.load('keyback.jpg')
Bg = pygame.transform.scale(Bg, (Wid, Hei))  #scaling image 
font = pygame.font.Font('MotionPersonalUseBold-2O0od.ttf', 40)

## function to get words randomly
Speed_Word = 0.5
Score = 0
def new_word():
    global DisplayWord, Word, X_Coodinate, Y_Coordinate, Text, Speed_Word
    X_Coodinate = random.randint(300,700)     #choosing x-cor between 300-700
    Y_Coordinate = 200  #y-cor
    Speed_Word += 0.10
    Word = ''
    words = open("words.txt").read().split(', ') # a text file named WORDS.TXT which contains random words which are used in game
    DisplayWord = random.choice(words)
new_word()


#function to draw Text
font_name = pygame.font.match_font('MotionPersonalUseBold-2O0od.ttf')
def draw_Text(display, Text, Size, X, Y):
    font = pygame.font.Font(font_name, Size)
    Text_surface = font.render(Text, True, Black)
    Text_rect = Text_surface.get_rect()
    Text_rect.midtop = (X, Y)
    Disp.blit(Text_surface, Text_rect)

 
#function to show front screen and gameover screen
def game_front_screen():
    Disp.blit(Bg, (0,0))
    if not game_over :
        draw_Text(Disp, "TRY AGAIN!", 90, Wid / 2, Hei / 4)
        draw_Text(Disp,"Well Done.. !! Your Score : " + str(Score), 70, Wid / 2, Hei /2)
    else:
        draw_Text(Disp, "Welcome, Press ANY KEY TO START..!", 54, Wid / 2, 550)
    pygame.display.flip()
    waiting = True
    while waiting:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


#main Game loop
game_over = True
game_start = True
while True:
    if game_over:
        if game_start:
            game_front_screen()
        game_start = False
    game_over = False

    
    Bg = pygame.image.load('teacher-Bg.jpg')
    Bg = pygame.transform.scale(Bg, (Wid, Hei))
    character = pygame.image.load('char.jpg')
    character = pygame.transform.scale(character, (50,50))
    wood = pygame.image.load('wood-.png')
    wood = pygame.transform.scale(wood, (90,50))


    Disp.blit(Bg, (0,0))

    Y_Coordinate += Speed_Word
    Disp.blit(wood,(X_Coodinate-50,Y_Coordinate+15))
    Disp.blit(character,(X_Coodinate-100,Y_Coordinate))
    draw_Text(Disp, str(DisplayWord), 40, X_Coodinate, Y_Coordinate)
    draw_Text(Disp, 'Score:'+str(Score), 40, Wid/2 , 5)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            Word += pygame.key.name(event.key)

            if DisplayWord.startswith(Word):
                if DisplayWord == Word:
                    Score += len(DisplayWord)
                    new_word()
            else:
                game_front_screen()
                time.sleep(2)
                pygame.quit()
                
    if Y_Coordinate < Hei-5:
        pygame.display.update()
    else:
        game_front_screen()

