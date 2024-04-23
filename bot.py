import pyautogui as pg
import time

confirm = pg.confirm(text='Deseja limpar arquivos temporários do seu disco C?', title='Limpeza de Disco', buttons=['OK', 'Cancel'])
if confirm == 'Cancel':
    exit()
else:
    confirm2 = pg.confirm(text=' Por Favor, não mova o mouse, ou use o teclado durante a execução do progama, caso contrário, mudará completará completamente o funcionamento do mesmo!', title= 'Limpeza de Disco', buttons= ['OK', 'Cancel'])
    if confirm2 == 'Cancel':
        exit()
    else:
        actions = ["%temp%", "PREFETCH"]
        for action in actions:

            pg.hotkey('win', 'r')
            pg.write(action)
            pg.press('enter')

            time.sleep(1)
            pg.hotkey('ctrl', 'a')
            pg.hotkey('ctrl', 'd')

            time.sleep(1)
            mark = pg.locateCenterOnScreen('mark.PNG')
            pg.click(mark)

            press = pg.locateCenterOnScreen('Capturar.PNG')
            pg.click(press)

            time.sleep(5)
            exit = pg.locateCenterOnScreen('1.PNG')
            pg.click(exit)

        pg.alert(text='Susesso!, tudo certo, pode voltar a usar seu computador!', title='Limpeza de Disco', button='OK')
