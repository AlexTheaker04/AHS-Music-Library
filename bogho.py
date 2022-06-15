# imports
import pygame
from pygame import mixer
import sys
import csv  
import webbrowser

# declare class
class cupboard:

    def __init__(self,box_num, X, Y, W, H):
        self.box_num = box_num
        self.x = X
        self.y = Y
        self.w = W
        self.h = H
        
    def reveal(self):
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y, self.w, self.h))

# open and make list of csv file
with open("AHS Jazz Music Library - Jazz - Instrument Storage.csv", "r") as f:
    csv_reader = csv.DictReader(f)
    name_records = list(csv_reader)


# function to locate where the music folder is
def locate(index_num):
    index_num = int(index_num)
    if (0<= index_num <= 14):
        return 1
    elif (15 <=  index_num <=33):
        return 2
    elif (34 <= index_num <=50):
        return 3
    elif (51 <= index_num <=70):
        return 4
    elif (71 <= index_num <=90):
        return 5
    elif (91 <= index_num <=110):
        return 6
    elif (111 <= index_num <=130):
        return 7
    elif (131-148 <= index_num <=148):
        return 8
    elif ( 149 <= index_num <=166):
        return 9
    elif ( 167 <= index_num <= 186):
        return 10
    elif ( 187<= index_num <= 206):
        return 11
    elif (207 <= index_num <=263 ):
        return 12
    
# create search function to look through the list of music folders to find the target (title)
def search(title):
    found = False
    arr = []
    arr2 = []
    count = 0
    for i in range (len(name_records)):
        if name_records[i]["Title"].upper()  == title.upper() :
            count +=1
            found = True
            
            if count >1:
                
                arr.append(name_records[i]["Folder number"])
            else:
                show(name_records[i]["Folder number"])
            #break
    if found == False: # if not found
        screen.blit(base_font.render("NOT FOUND", True, (0,0,0)), (6,25))
    if count >1:
        arr2.append(f"Also appears at: {arr}")
        for iter, thing in enumerate(arr2):
            screen.blit(base_font.render(thing,True, (0,0,0)),(6,500))

# when "go to recording" button is pressed, go to link or if no link to generic site
def geturl(num):
    num = int(num)
    if list(name_records[num-1].values())[6] != "": # if the url value is not empty, open it in browser.
        webbrowser.open(list(name_records[num-1].values())[6])
    else: # open the generic link to the music recording site.
        webbrowser.open("https://www.jwpepper.com/sheet-music/welcome.jsp")

#get the values from the list (name_records) and display them
def show(test):
    arr = []
    test = int(test)
    test -= 1
    temp = list(name_records[test].values()) # get all the values and keys
    temp2 = list(name_records[test].keys())
    for i in range(0,7,1):
         if temp[i] != "":
             arr.append(f'{temp2[i]}: {temp[i]}') # append those values to arr to be printed out.
         else:
             arr.append(f'{temp2[i]}: None')
    # print(string)
    for iter, thing in enumerate(arr):
        screen.blit(base_font.render(thing, True, (0,0,0)), (6,25*iter))
# init pygame         
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
mixer.music.set_volume(0.2)
# screen = pygame.display.set_mode((100, 100))
screen = pygame.display.set_mode([1280, 800])

# display icon and caption text
pygame.display.set_caption('AHS Jazz Library locator!')
Icon = pygame.image.load("ICON.jpg")
pygame.display.set_icon(Icon)

# music
mixer.music.load('take5.wav')

# display image
image = pygame.image.load("shelf.png")
image = pygame.transform.scale(image, (900, 600))

# get a font and set a few variables related to text up
base_font = pygame.font.SysFont("comicsansms", 19)
user_text = ''
search_text = ""
help1_text = "Search by number:"
help2_text = "Search by name:"
found_at_text = ""
text = base_font.render('', True, (255,255,255))
text2= base_font.render('', True, (255,255,255))
textRect = text.get_rect()
textRect2 = text2.get_rect()
link_color = (0, 0, 0)


# create rectangles
input_rect = pygame.Rect(200, 200, 100, 32)
search_rect = pygame.Rect(5, 400, 300, 32)
  
# set active and passive colors
color_active = pygame.Color('gray')
color_passive = pygame.Color('gainsboro')
color = color_passive
color2 = color_passive

  
active = False
active2 = False

# declare classes
box_1 = cupboard(1,410, 210, 190, 210)
box_2 = cupboard(2,600,210,190,210)
box_3 = cupboard(2,790,210,190,210)
box_4 = cupboard(4,1024,210,190,210)
#box_5 = cupboard(5,80,80)
#box_6 = cupboard(6,100,100)



while True:
    for event in pygame.event.get():
  
        # quit game if user clicks exit
        if event.type == pygame.QUIT:
            mixer.music.play() # play funny sound
            pygame.time.wait(1020) # wait until end
            pygame.quit()
            sys.exit()
        if len(user_text) > 3: # makes sure length is less then 3
            user_text = user_text[:-1] 
        if event.type == pygame.MOUSEBUTTONDOWN: # if user clicks mouse on a button, set to active
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
            if search_rect.collidepoint(event.pos):
                active2 = True
            else:
                active2 = False
            # if the user clicks on get url button
            if urlbutton.collidepoint(event.pos) and len(user_text) != 0 and int(user_text) <= len(name_records):
                geturl(user_text)
            
  
        if event.type == pygame.KEYDOWN and active == True: # if user presses a key down when with the number search box

            if event.key == pygame.K_RETURN: # if key is the enter key set active to fase.
                active = False
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]
  
            else: # input validation ( only between 0-9)
                try:
                    temp = event.unicode
                    temp = int(temp)
                    user_text += event.unicode
                    print(locate(user_text))
                except:
                    print("letter")


        if event.type == pygame.KEYDOWN and active2 == True: # if user presses a key down when with the title search box
            
            if event.key == pygame.K_RETURN: # if key is the enter key
                active2 = False
            elif event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                search_text = search_text[:-1]
            else: # input validation only unicode characters.
                try:
                    search_text += event.unicode
                except:
                    print("non unicode character!")    
            
    # fill screen with white
    screen.fill((255, 255, 255))
  
    if active:
        color = color_active
        search_text = ""
    else:
        color = color_passive
    if active2:
        color2 = color_active
        user_text = ''
    else:
        color2 = color_passive
    if active == False and len(user_text) != 0 and int(user_text) <= len(name_records) :
         show(user_text)
    if active2 == False and len(search_text) != 0:
        search(search_text)


    # display texts    
    urlbutton = screen.blit(base_font.render("Go to recording", True, link_color), (5, 300))
    screen.blit(text, textRect)
    screen.blit(text2, textRect2)
    # draw rectangles 
    pygame.draw.rect(screen, color, input_rect)
    pygame.draw.rect(screen, color2, search_rect)

    # draw text to the screen  
    text_surface  = base_font.render(user_text, True, (255, 255, 255))
    text_surface2 = base_font.render(search_text, True, (255,255,255))
    text_surface3 = base_font.render(help1_text, True, (0,0,0))
    text_surface4 = base_font.render(help2_text, True, (0,0,0))

    
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    screen.blit(text_surface2, (search_rect.x+5, search_rect.y+5))
    screen.blit(text_surface3, (5, 200))
    screen.blit(text_surface4, (search_rect.x, search_rect.y-30))
    screen.blit(image, (400, 200))  

    # locate where the box is and display it.
    if len(user_text) >0 and active == False:

        
        if locate(user_text) == 1:
            box_1.reveal()
        elif locate(user_text) == 2:
            box_2.reveal()
        elif locate(user_text) == 3:
            box_3.reveal()
        elif locate(user_text) == 4:
            box_4.reveal()

     
    pygame.display.flip()
    clock.tick(60)
