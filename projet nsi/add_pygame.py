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
    def __init__(self,screen : pygame.Surface,x :int = 0, y :int = 0,w : int = 100, h : int = 100, color : tuple[int,int,int,int] = (255,255,255,0), bg : tuple[int,int,int,int] = (0,0,0,0),nb_car_max : int = None) -> None:
        self.info = {"x" : x,"y" : y,"w" : w,"h" : h,"ini_h" : h,"ini_w" : w}
        self.position()
        self.color = color
        self.text = ""
        self.focus = False
        self.taille = int(h)
        self.surface = screen
        self.bg = bg
        self.surftext = self.surface.blit(pygame.font.SysFont(None, self.taille).render(self.text,False,self.color,self.bg),self.pos)
        self.sub = screen.subsurface(self.pos)
        self.nb_max = nb_car_max
        self.update()
        self.cursor = pygame.mouse.get_cursor().copy()

    def draw(self,event : pygame.event.Event) -> None:

        pos_mouse = pygame.mouse.get_pos()
        click = True if pygame.mouse.get_pressed()[0] else False
        pygame.mouse.set_cursor(self.cursor)

        if self.pos.collidepoint(pos_mouse):

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)

            if click and not(self.focus):
                self.focus = True
                
        if click and not(self.pos.collidepoint(pos_mouse)) and self.focus:
            self.focus = False
        
        if self.focus:
            if event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key) == "backspace":
                    self.text = self.text[:-1]
                elif event.unicode == "" or pygame.key.name(event.key) == "tab":
                    pass
                else:
                    self.text += event.unicode
                self.update()

    def update(self) -> None:
        
        pygame.draw.rect(self.surface,self.bg,self.pos)
        self.texte_edit()
        self.update_size()

    def update_size(self,changement : dict[str,int] = {}) -> None:
        
        """
        update the size of the text input\n
        possbile value : x,y,w,h\n
        change inition value of w,h : ini_w,ini_h
        """

        
        for i,j in changement.items():
            if i in self.info:
                self.info[i] = j
        
        self.position()
        try:
            self.sub = self.surface.subsurface(self.pos)
        except:
            self.info["w"] = pygame.display.get_window_size()[0]
            self.pos = pygame.Rect(self.info["x"],self.info["y"],self.info["w"],self.info["h"])
        
        self.texte_edit()
        self.update_surf()

    def update_surf(self) -> None:

        if type(self.surftext) == pygame.surface.Surface:
            self.sub.fill(self.bg)
            self.sub.blit(self.surftext,self.pos)
            self.surface.blit(self.sub.copy(),self.pos)

    def texte_edit(self) -> None:
        self.surftext = pygame.font.SysFont(None, self.taille).render(self.text,False,self.color,self.bg)
        txt_size = self.surftext.get_width() if type(self.surftext) == pygame.surface.Surface else self.surftext.x
        while self.info["w"] < txt_size:
            self.text = self.text[:-1]
            self.surftext = pygame.font.SysFont(None, self.taille).render(self.text,False,self.color,self.bg)
            txt_size = self.surftext.get_width() if type(self.surftext) == pygame.surface.Surface else self.surftext.x

    def position(self) -> None:
        
        self.info["w"] = pygame.display.get_window_size()[0] if self.info["w"] > pygame.display.get_window_size()[0] else self.info["ini_w"]
        self.info["h"] = pygame.display.get_window_size()[1] if self.info["h"] > pygame.display.get_window_size()[1] else self.info["ini_h"]
        self.pos = pygame.Rect(self.info["x"],self.info["y"],self.info["w"],self.info["h"])