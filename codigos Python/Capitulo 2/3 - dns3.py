from Queue import Queue
import threading, socket

dominio = "dominio.com"
lock = threading.Lock() #1

def forca_bruta():
    while not q.empty(): #2
        DNS = q.get() + "." + dominio #3
        try: #4
            IP = socket.gethostbyname(DNS) #5
            lock.acquire() #6
            print DNS + ":\t" + IP #7
        except socket.gaierror: #8
            pass #9
        else: #10
            lock.release() #11
        q.task_done() #12

q = Queue() #13

for i in range(20): #14
    t = threading.Thread(target=forca_bruta)
    t.daemon = True
    t.start()

with open("lista.txt") as lista: #15
    while True: #16
        nome = lista.readline().strip("\n") #17
        if not nome:
            break #18
        q.put(nome) #19

q.join() #20
print "\nMapeamento completo"