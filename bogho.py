# import sys module
import pygame
import sys
import csv  
import webbrowser


    
with open("AHS Jazz Music Library - Jazz - Instrument Storage.csv", "r") as f:
    csv_reader = csv.DictReader(f)
    name_records = list(csv_reader)



def geturl(num):
    num = int(num)
    if list(name_records[num-1].values())[6] != "":
        webbrowser.open(list(name_records[num-1].values())[6])
    else:
        webbrowser.open("https://www.jwpepper.com/sheet-music/welcome.jsp")

def show(test):
    string = []
    test = int(test)
    test -= 1
    temp = list(name_records[test].values())
    temp2 = list(name_records[test].keys())
    for i in range(0,7,1):
         string.append(f'{temp2[i]}: {temp[i]}')
    # print(string)
    for iter, thing in enumerate(string):
        screen.blit(base_font.render(thing, True, (0,0,0)), (5,25*iter))
         
# pygame.init() will initialize all
# imported module
pygame.init()
clock = pygame.time.Clock()
# it will display on screen
display_surface = pygame.display.set_mode((100, 100))
screen = pygame.display.set_mode([1280, 720])

# display icon and caption text
pygame.display.set_caption('AHS Jazz Library locator!')
Icon = pygame.image.load("ICON.jpg")
pygame.display.set_icon(Icon)

# display image
image = pygame.image.load("shelf.png")

# basic font for user typed
base_font = pygame.font.SysFont("comicsansms", 17)
user_text = ''
text = base_font.render('', True, (255,255,255))
textRect = text.get_rect()
link_color = (0, 0, 0)


# create rectangle
input_rect = pygame.Rect(200, 200, 100, 32)
  
# color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
color_active = pygame.Color('lightskyblue3')
  
# color_passive store color(chartreuse4) which is
# color of input box.
color_passive = pygame.Color('chartreuse4')
color = color_passive
  
active = False


while True:
    for event in pygame.event.get():
  
      # if user types QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if len(user_text) > 3:
            user_text = user_text[:-1] 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
            if urlbutton.collidepoint(event.pos) and len(user_text) != 0 and int(user_text) <= len(name_records):
                #print("bob")
                geturl(user_text)
            
  
        if event.type == pygame.KEYDOWN and active == True:
  
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]
  
            # Unicode standard is used for string
            # formation
            else:
                try:
                    temp = event.unicode
                    temp = int(temp)
                    user_text += event.unicode
                except:
                    print("letter")
    
    # it will set background color of screen
    screen.fill((255, 255, 255))
  
    if active:
        color = color_active
    else:
        color = color_passive
    if active == False and len(user_text) != 0 and int(user_text) <= len(name_records) :
         show(user_text)
        
    urlbutton = screen.blit(base_font.render("Go to recording", True, link_color), (5, 200))
    display_surface.blit(text, textRect)
    # draw rectangle and argument passed which should
    # be on screen
    pygame.draw.rect(screen, color, input_rect)
  
    text_surface = base_font.render(user_text, True, (255, 255, 255))
      
    # render at position stated in arguments
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    display_surface.blit(image, (400, 200))  
    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(100, text_surface.get_width()+10)
      
    # display.flip() will update only a portion of the
    # screen to updated, not full area
    pygame.display.flip()
      
    # clock.tick(60) means that for every second at most
    # 60 frames should be passed.
    clock.tick(60)
