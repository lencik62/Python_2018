import pyautogui as pag


pag.moveRel(0,100)
pag.click()
pag.typewrite("\npag.moveRel(0,25)\npag.click()\npag.typewrite('pag.click()',.05)")
pag.typewrite(['left','up'])
pag.hotkey('ctrl','s')
pag.press("enter")
