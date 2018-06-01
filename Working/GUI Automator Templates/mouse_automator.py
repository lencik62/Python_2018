import pyautogui as pag

def sprial():
    print("drag motion")
    i = 0
    while i < 300:
        pag.dragRel(i,0,duration=.01)
        i+=10
        pag.dragRel(0,-i,duration=.01)
        i+=10
        pag.dragRel(-i,0,duration=.01)
        i+=10
        pag.dragRel(0,i,duration=.01)
        i+=10

def faker():
    print(pag.size())
    print(pag.position())
    x,y = pag.position()
    pag.moveTo(100,500,duration=1.6)
    pag.rightClick()
    pag.moveRel(200,500,duration=2)
    pag.rightClick(x,y)
    # pag.displayMousePosition()

def reverse_minimize():
    print("drag motion")
    i = 0
    while i < 100:
        pag.dragRel(i,0,duration=.01)
        pag.dragRel(0,-i,duration=.01)
        pag.dragRel(-i,0,duration=.01)
        pag.dragRel(0,i,duration=.01)
        i+=10


def main():
    sprial()
    faker()

if __name__ =="__main__":
    print("running main")
    print("please drag the cursor to the left top most corner to stop the auto mouse controls")
    main()
