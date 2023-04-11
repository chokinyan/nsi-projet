import pygame
class Button:
    """comme son nom l'indique permet de cré de bouton clicable\n
        quoi jsp ecrire francais ?\n
        ba c'est vrai
    """
    def __init__(self,x :int = 0, y :int = 0, fild :str = "", scale :float = 1) -> None:
        width = fild.get_width()
        height = fild.get_height()
        self.fild = pygame.transform.scale(fild,((width*scale),(height*scale)))
        self.coo = self.fild.get_rect()
        self.coo.topleft = (x,y)
        self.click = False


    def draw(self,screen : pygame.Surface, precis :str = "",bruit :str = "") -> bool:

        action = False
        pos = pygame.mouse.get_pos()
        
        if self.coo.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                if bruit != "":
                    pygame.mixer.Sound(bruit).play
                self.click = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.click = False

        if precis == "center":
            center = screen.get_rect().center
            self.coo = self.fild.get_rect(center = center)
            screen.blit(self.fild, self.fild.get_rect(center = center))
        elif precis == "left":
            left = screen.get_rect().left
            self.coo = self.fild.get_rect(left = left)
            screen.blit(self.fild, self.fild.get_rect(left = left))
        elif precis == "bottom":
            bottom = screen.get_rect().bottom
            self.coo = self.fild.get_rect(bottom = bottom)
            screen.blit(self.fild, self.fild.get_rect(bottom = bottom))
        elif precis == "right":
            right = screen.get_rect().right
            self.coo = self.fild.get_rect(right = right)
            screen.blit(self.fild, self.fild.get_rect(right = right))
        elif precis == "topright":
            topright = screen.get_rect().topright
            self.coo = self.fild.get_rect(topright = topright)
            screen.blit(self.fild,self.fild.get_rect(topright=topright))
        elif precis == "bottomleft":
            topleft = screen.get_rect().topleft
            self.coo = self.fild.get_rect(topleft = topleft)
            screen.blit(self.fild,self.fild.get_rect(topleft=topleft))
        elif precis == "bottomright":
            bottomright = screen.get_rect().bottomright
            self.coo = self.fild.get_rect(bottomright = bottomright)
            screen.blit(self.fild,self.fild.get_rect(bottomright=bottomright))
        elif precis == "topleft":
            topleft = screen.get_rect().topleft
            self.coo = self.fild.get_rect(topleft = topleft)
            screen.blit(self.fild,self.fild.get_rect(topleft = topleft))
        else:
            screen.blit(self.fild, (self.coo.x,self.coo.y))
        
        return action
    
class TextInput:
    """
    Text input creator\n
    x,y is the position\n
    h = height\n
    w = width\n
    size = text size\n 
    bg != beau gosse\n
    bg = background\n
    """
    def __init__(self,screen : pygame.Surface,x :int = 0, y :int = 0,w : int = 100, h : int = 100, color : tuple[int,int,int,int] = (255,255,255,0),size : int = 30, bg : tuple[int,int,int,int] = None,nb_car_max : int = None) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.text = ""
        self.focus = False
        self.pos = pygame.Rect(self.x,self.y,self.w,self.h)
        self.taille = size
        self.surface = screen
        self.surftext = self.surface.blit(pygame.font.SysFont(None, self.taille).render(self.text,False,self.color,(255,255,255)),self.pos)
        if bg == None:
            self.bg = (0,0,0,0)
        else:
            self.bg = bg
        self.sub = screen.subsurface(self.pos)
        self.nb_max = nb_car_max

    def draw(self,event : pygame.event.Event) -> None:

        pos_mouse = pygame.mouse.get_pos()

        if self.pos.collidepoint(pos_mouse):

            #pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)

            if pygame.mouse.get_pressed()[0] == 1 and self.focus == False:
                self.focus = True
                
        if pygame.mouse.get_pressed()[0] == 1 and not(self.pos.collidepoint(pos_mouse))  and self.focus == True:
            self.focus = False
        
        if self.focus == True:
            if event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key) == "backspace":
                    self.text = self.text[:-1]
                elif event.unicode == "" or pygame.key.name(event.key) == "tab":
                    pass
                else:
                    self.text += event.unicode
                self.__update__()

    def __update__(self) -> None:

        if self.bg != None:
            pygame.draw.rect(self.surface,self.bg,self.pos)

        self.__changetxt__()

        if self.w < self.surftext.get_width():
            print('out of text surface')
            self.text = self.text[:-1]
            self.__changetxt__()
        self.sub.fill(self.bg)
        self.sub.blit(self.surftext,self.pos)
        self.surface.blit(self.sub.copy(),self.pos) 

    def __changetxt__(self)-> None:
        self.surftext = pygame.font.SysFont(None, self.taille).render(self.text,False,self.color,(255,255,255))