import pyxel as pyx

test = 0

pyx.init(500,500,fps=60,title= "jeu de l'oie ")

def update():
    global test
    if pyx.btnp(pyx.KEY_Q):
        #pyx.quit()
        test = 1
    elif pyx.btnp(pyx.MOUSE_BUTTON_LEFT):
        #pyx.pset(pyx.mouse_x,pyx.mouse_y,1)
        print(pyx.mouse_x, pyx.mouse_y)
        print(pyx.pget(pyx.mouse_x, pyx.mouse_y))

def draw(waw = False):
    global test
    if test == 0:
        pyx.cls(0)
        #pyx.rect(10, 10, 20, 20, 11)
        pyx.mouse(True)
    elif test == 1:
        pyx.cls(1)
    #pyx.Image.load(x = 0, y = 0 , Image= r"projet nsi\image\dée\1.png")

pyx.run(update, draw)

