from pywinauto import Application
import pygetwindow as gw
import pywinauto
import pyautogui
import time
import os

try:
    global PATH_IMAGE_POPUP
    PATH_IMAGE_POPUP = os.path.join(os.path.dirname(__file__), "Image/Popup1.png")
except (FileNotFoundError):
        print("Wrong file or file path popup1")

try:
    global PATH_IMAGE_POPUPBIS
    PATH_IMAGE_POPUPBIS = os.path.join(os.path.dirname(__file__), "Image/Popup1Bis.png")
except (FileNotFoundError):
        print("Wrong file or file path popup1Bis")

try:
    global PATH_IMAGE_POPUP2
    PATH_IMAGE_POPUP2 = os.path.join(os.path.dirname(__file__), "Image/Popup2.png")
except (FileNotFoundError):
        print("Wrong file or file path popup2")

try:
    global PATH_IMAGE_POPUP2BIS
    PATH_IMAGE_POPUP2BIS = os.path.join(os.path.dirname(__file__), "Image/Popup2Bis.png")
except (FileNotFoundError):
        print("Wrong file or file path popup2bis")

try:
    global PATH_IMAGE_QUIT
    PATH_IMAGE_QUIT = os.path.join(os.path.dirname(__file__), "Image/Quit.png")
except (FileNotFoundError):
        print("Wrong file or file path quit")

try:
    global PATH_INI
    PATH_INI = "C:\RemoteCmd\Status.ini"
except (FileNotFoundError):
        print("Wrong file or file path Status.ini")


def main():

    while(True):

        while(True):

            time.sleep(5)
            # Récupération de la référence de la pièce #
            try:
                f = open(PATH_INI, "r+")
                val = f.readlines()

                if(val[1][17] == '2'):

                    if(val[1][18] == '0'):
                        var = '490035-2000'
                    else:
                        var = '490035-2100'

                else:

                    if(val[1][18] == '2'):
                        var = '490035-3200'
                    else:
                        var = '490035-3300'

                f.close()               

            except:
                print("Closing file not found")
        
            # Lecture de la variable var_finLot
            try:
                 if(val[2][11] == '1'):
                     print("Read")
                     break
            except:
                i=0
        # Focus de la fenêtre GEOPAK # 
        try:
            notepadWindow = gw.getWindowsWithTitle('GEOPAK Mode Répétition in MCOSMOS-1 v4.2.R2   - ' + var)[0]
            notepadWindow.activate()                                                                # Fais apparaître en premier plan GEOPAK
            print("App on screen")
            
        except:
            print("Impossible to display the app")

        while(True):
            while(True):
                # Recherche de l'image Pop-Up 1 # 
                try:
                    X, Y = pyautogui.locateCenterOnScreen(PATH_IMAGE_POPUP)                         # Trouve les coordonnées du centre de l'image fournit sur la fenêtre GEOPAK
                    Xbut = X + 124                                                                  # Décalage en x pour être sur le bouton
                    Ybut = Y + 30                                                                   # Décalage en y pour être sur le bouton
                    pywinauto.mouse.click(button='left', coords=(Xbut, Ybut))                       # Clique gauche sur le bouton
                    print("Pop-up 1 : OK")
                    break                                                                           # Saute à la prochaine boucle while si image trouvée et clique fait
                except:
                    print("Pop-up 1 not found")
                # Recherche de l'image Pop-Up 1Bis # 
                try:
                    X, Y = pyautogui.locateCenterOnScreen(PATH_IMAGE_POPUPBIS)                      # Trouve les coordonnées du centre de l'image fournit sur la fenêtre GEOPAK
                    Xbut = X + 124                                                                  # Décalage en x pour être sur le bouton
                    Ybut = Y + 30                                                                   # Décalage en y pour être sur le bouton
                    pywinauto.mouse.click(button='left', coords=(Xbut, Ybut))                       # Clique gauche sur le bouton
                    print("Pop-up 1Bis : OK")
                    break                                                                           # Saute à la prochaine boucle while si image trouvée et clique fait
                except:
                    print("Pop-up 1Bis not found")

            time.sleep(1)                                                                           # Attente d'une seconde pour éviter de freeze l'application

            while(True):
                # Recherche de l'image Pop-Up 2 # 
                try :
                    X, Y = pyautogui.locateCenterOnScreen(PATH_IMAGE_POPUP2)                        # Trouve les coordonnées du centre de l'image fournit sur la fenêtre GEOPAK
                    Xbut2 = X - 70                                                                  # Décalage en x pour être sur le bouton
                    Ybut2 = Y + 45                                                                  # Décalage en y pour être sur le bouton
                    pywinauto.mouse.click(button='left', coords=(Xbut2, Ybut2))                     # Clique gauche sur le bouton
                    print("Pop-up 2 : OK")
                    break                                                                           # Saute à la prochaine boucle while si image trouvée et clique fait
                except:
                    print("Pop-up 2 not found")
                
                # Recherche de l'image Pop-Up 2Bis # 
                try :
                    X, Y = pyautogui.locateCenterOnScreen(PATH_IMAGE_POPUP2BIS)                     # Trouve les coordonnées du centre de l'image fournit sur la fenêtre GEOPAK
                    Xbut2 = X - 70                                                                  # Décalage en x pour être sur le bouton
                    Ybut2 = Y + 45                                                                  # Décalage en y pour être sur le bouton
                    pywinauto.mouse.click(button='left', coords=(Xbut2, Ybut2))                     # Clique gauche sur le bouton
                    print("Pop-up 2Bis : OK")
                    break                                                                           # Saute à la prochaine boucle while si image trouvée et clique fait
                except:
                    print("Pop-up 2Bis not found")

            time.sleep(1)                                                                           # Attente d'une seconde pour éviter de freeze l'application

            while(True):
                # Recherche de l'image Pop-Up Quit # 
                try :
                    X, Y = pyautogui.locateCenterOnScreen(PATH_IMAGE_QUIT)                          # Trouve les coordonnées du centre de l'image fournit sur la fenêtre GEOPAK
                    Xquit = X                                                                       # Décalage en x pour être sur le bouton
                    Yquit = Y                                                                       # Décalage en y pour être sur le bouton 
                    pywinauto.mouse.click(button='left', coords=(Xquit, Yquit))                     # Clique gauche sur le bouton
                    print("Quit : OK")
                    break                                                                           # Saute à la prochaine boucle while si image trouvée et clique fait
                except:
                    print("Quit not found")

            while(True):
                try:
                    f = open(PATH_INI, "r")                                                         # Ouvre Status.ini en lecture
                    contents = f.readlines()                                                        # Copie toutes ces lignes
                    f.close()                                                                       # Ferme Status.ini

                    contents.pop(2)                                                                 # Supprime la troisième ligne (Ou il y Var_FinLot)

                    f = open(PATH_INI, "w")                                                         # Ouvre Status.ini en écriture
                    contents = "".join(contents) + "Var_FinLot=0"
                    f.write(contents)                                                               # Réécrit Var_FinLot=0 en fin de fichier                                                                       
                    f.close()                                                                       # Ferme Status.ini   pour sauvegarder                                                                     
                    print("Write")
                    break                                                                           # Retourne au début du programme
                except:
                    print("Impossible writing")
            break

if __name__ == '__main__':
    main()
