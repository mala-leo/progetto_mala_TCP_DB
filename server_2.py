import threading 
import socket
import sqlite3
import mysql.connector

comunicazioni = ["",""]
PASSWORD = "CIAO"
MAX_ATTEMPTS = 3

def gestisci_comunicazione(conn):
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        conn.send("Benvenuto, inserisci password: ".encode())
        data = conn.recv(1024).decode()
        
        if data == PASSWORD:
            conn.send("Password corretta.\n".encode())
            break
        else:
            conn.send("Password errata, reinserisci la password.\n".encode())
            attempts += 1

    if attempts == MAX_ATTEMPTS:
        conn.send("Troppi tentativi errati. La connessione verra chiusa.\n".encode())
        conn.close()
        return

    conn.send(" Inserisci 'R' per fare una query SELECT * sul DB: , 'C' creare nuovi dipendenti , U per modificare/aggiornare , D per cancellare ".encode())   # faccio la richiesta di query 
    
    while True:
        data = conn.recv(1024).decode()
        
        if data.upper() == 'R':
            dati = db_get()
            conn.send(str(dati).encode())
        
        
        elif data.upper() == 'D':
            #valore_da_eliminare = input("inserisci il valore da eliminare ") 
            conn.send("inserisci valore da eliminare".encode())
            data2 = (conn.recv(1024)).decode() 
            print(data2)
            #query = "DELETE FROM clienti_leonardo_malaguti WHERE nome = \valore_da_eliminare\"
            #cursor.execute(query, (valore_da_eliminare,))
            db_delete(data2)

        
        elif data.upper() == 'U':
             conn.send("Inserisci l'ID del record da aggiornare: ".encode())
             record_id = (conn.recv(1024)).decode()
             conn.send("Inserisci il nuovo nome: ".encode())
             nome = (conn.recv(1024)).decode()
             conn.send("Inserisci il nuovo cognome: ".encode())
             congome = (conn.recv(1024)).decode()
             conn.send("inserisci inserisci pos_lav".encode())
             pos=(conn.recv(1024)).decode()
             conn.send("inserisci inserisci data di assunzione".encode())
             data_assunzione=(conn.recv(1024)).decode()
             conn.send("inserisci inserisci data_corr".encode())
             data_corr=(conn.recv(1024)).decode()
             conn.send("inserisci inserisci lugo di n ".encode())
             luogo_di_nascita=(conn.recv(1024)).decode()
    

             db_update(record_id,nome,congome,pos,data_assunzione,data_corr,luogo_di_nascita)
            
        elif data.upper() == 'C':
            conn.send("inserisci inserisci nome".encode())
            nome=(conn.recv(1024)).decode()
            conn.send("inserisci inserisci cognome".encode())
            congome=(conn.recv(1024)).decode()
            conn.send("inserisci inserisci pos_lav".encode())
            pos=(conn.recv(1024)).decode()
            conn.send("inserisci inserisci data di assunzione".encode())
            data_assunzione=(conn.recv(1024)).decode()
            conn.send("inserisci inserisci data_corr".encode())
            data_corr=(conn.recv(1024)).decode()
            conn.send("inserisci inserisci lugo di n ".encode())
            luogo_di_nascita=(conn.recv(1024)).decode()
            create(nome,congome,pos,data_assunzione,data_corr,luogo_di_nascita)
            
            
        else:
            conn.send("Comando non riconosciuto.\n".encode())
        
    conn.close()

def db_get():
    conn = mysql.connector.connect(
        host="localhost",
        user="leonardo_malaguti",
        password="malaguti1234",
        database="5atepsit",
        port=3306,
    )



    cur = conn.cursor()  # conn serve per la connesione al database, cursor e un puntatotre 
    query = "SELECT * FROM clienti_leonardo_malaguti"
    cur.execute(query)
    dati = cur.fetchall()
    return dati

def db_update(id, nome, cognome, posizione_lavorativa, data_di_assunzione, data_corrente, luogo_di_nascita):
    conn = mysql.connector.connect(
        host="localhost",
        user="leonardo_malaguti",
        password="malaguti1234",
        database="5atepsit",
        port=3306,
    )
    cur = conn.cursor()
    query = "UPDATE `clienti_leonardo_malaguti` SET `nome`=%s, `cognome`=%s, `posizione_lavorativa`=%s, `data_di_assunzione`=%s, `data_corrente`=%s, `luogo_di_nascita`=%s WHERE `id`=%s"
    values = (nome, cognome, posizione_lavorativa, data_di_assunzione, data_corrente, luogo_di_nascita, id)
    cur.execute(query, values)
    conn.commit()
    conn.close()


def db_delete(id):
    print("peffo")
    conn = mysql.connector.connect(
    host="localhost",
    user="leonardo_malaguti",
    password="malaguti1234",
    database="5atepsit",
    port=3306,
    )
    cur = conn.cursor()  # conn serve per la connesione al database, cursor e un puntatotre 
    query = f"DELETE FROM `clienti_leonardo_malaguti` WHERE nome= %s "
    cur.execute(query, (id,))
    conn.commit()
    #cur.execute(query)
    print("rrrrrrrrreffo")
def create(nome,congome,pos,data_assunzione,data_corr,luogo_di_nascita):
    print("peffo")
    conn = mysql.connector.connect(
    host="localhost",
    user="leonardo_malaguti",
    password="malaguti1234",
    database="5atepsit",
    port=3306,
    )
    cur = conn.cursor()  # conn serve per la connesione al database, cursor e un puntatotre #
    query= f"INSERT INTO `clienti_leonardo_malaguti`(`nome`, `cognome`, `posizione_lavorativa`, `data_di_assunzione`, `data_corrente`, `luogo_di_nascita`) VALUES (%s,%s,%s,%s,%s,%s)"
    values = (nome,congome,pos,data_assunzione,data_corr,luogo_di_nascita,)
    cur.execute(query,values)
    conn.commit()
    
print("Server in ascolto: ")
lock = threading.Lock()
HOST = ''
PORT = 50010
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)
thread = []
lista_connessioni = []
i = 0

while True:
    lista_connessioni.append(s.accept())
    print('Connected by', lista_connessioni[i][1])
    thread.append(threading.Thread(target=gestisci_comunicazione, args=(lista_connessioni[i][0],)))
    thread[i].start()
    i += 1