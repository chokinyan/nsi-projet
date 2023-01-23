import socket
import time

#192.168.1.13
ip = "localhost"
port = 80
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((ip,port))
print("Connecté")
test = (input("On fait quoi -->"))
client.send(test.encode())

if test == "fichier_find":
    test = (input("nom du fichier -->"))
    client.send(test.encode())
    retour = client.recv(10**8)
    retour = retour.decode("utf-8")
    print(retour)

elif test == "recup_fichier":
    retour = client.recv(10**8)
    retour = retour.decode("utf-8")
    print(retour)
    test = (input("regarder où ? -->"))
    client.send(test.encode())
    retour = client.recv(10**8)
    retour = retour.decode("utf-8")
    print(retour)
    client.close()

elif test == "send_fichier":
    fichier_serv = input("le chemain du fichier sur le serv + le nom de celui-ci -->") 
    fichier_cli = open(input("le chemain du fichier sur le client -->"), "rb")
    text_send = fichier_cli.read()
    client.send(fichier_serv.encode())
    time.sleep(5)
    client.sendall(text_send)
    client.close()

elif test == "lancer":
    fichier_lancer = input("Fichier a lancer sur le serv (True pour envoyer un fichier a lancer la bas puis supprimer) -->")
    client.send(fichier_lancer.encode())
    if fichier_lancer  == "True":
        fichier_serv = input("le chemain du fichier sur le serv + nom de ceui-ci -->")
        client.send(fichier_serv.encode())
        time.sleep(5)
        fichier_cli = open(input("le chemain du fichier sur le client -->"),"rb")
        text_send = fichier_cli.read()
        client.send(text_send)
        time.sleep(5)
        temp = input("Temps avant le delete du fichier -->")
        client.send(temp.encode())
        client.close
    else:
        client.close()

elif test == "supp_fichier":
    fermer = input("delet qui -->")
    client.send(fermer.encode())
    client.close()

elif test == "cmd":
    commande_cmd = input("la commande cmd a faire -->")
    client.send(commande_cmd.encode())

elif test == "beep":
    HZ = input("Le nombre en HZ -->")
    client.send(HZ.encode())
    temps = input("La durée du beep -->")
    client.send(temps.encode())

else:
    client.close()
client.close()