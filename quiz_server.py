import socket
from threading import Thread
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '123.45.67.7'
port = 4000

server.bind((ip_address, port))
server.listen()

list_of_clients = []

print("Servee has started...")

questions = [
    "What is the Italian word for PTE? \n a.Mozarella\n b.Pasty\n c.Patty\n d.Pizza",
    "Water boils at 212 Units at which scale? \n a.Farenhite\n b.Celsius\n c.Ramkin\n d.Kelvin",
    "Which sea creature has three hearts? \n a.Dolphin\n b.Octopus\n c.Malrus\n d.seal",
    "Who was the character famous in our childhood rhymes associated with a lamb? \n a.Mary\n b.Javk\n c.Johnny\n d.Mukesh",
    "How many bones does have adults human have?\n a.206\n b.208\n c.201\n d.196",
    "What element does not exist?\n a.XF \n b.Re \n c.Si \n d.Pa",
    "How many states are there in India?\n a.24 \n b.29 \n c.30 \n d.34 ",
    "Who invented the telephone?\n a.A.G Bell \n b.John Wick \n c.Thomas Edison \n d.G Marconi",
    "Who is Loki? \n a.God of Thunder \n b.God of Dwarves \n c.God of Mischief \n d.God of Gods",
    "who was the first Indian female astroaut?\n a.Sunita Williams \n b.Kalpana Chawla \n c.None of them  \n d.Both of them ",
    "What is the smallest continent?\n a.Asia \n b.Antarctic \n c.Africa\n d.Australia ",
    "The beaver is the national embeleam of which country? \n a.Zimbabwe \n b.Iceland \n c.Argentina \n d.Canada ",
    "How many players are on the field in baseball?\n a.6 \n b.7 \n c.9 \n d.8 ",
    "Hg stands for? \n a.Mercury \n b.Hulgerium \n c.Argenine \n d.Halfnium ",
    "Who gifted the Statue of Liberty to the US?\n a.Brazil\n b.France\n c.Wales\n d.Germany",
    "Which planet is closest to the sun?\n a.Mercury\n b.Pluto\n c.Earth\n d.Venus",

]
answers = ['d', 'a', 'b', 'a', 'a', 'a', 'a','b', 'a', 'c','b','d','d','c','a','b','a']


def clientthread(conn,nickname):
    score = 0
    conn.send("Welcome to this quiz game!".encode('utf-8'))
    conn.send("You will receive a question. The answer to that question should be one of a, b, c or d\n".encode('utf-8'))
    conn.send("Good Luck!\n\n".encode('utf-8'))
    index, question, answer = get_random_question_answer(conn)
    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
                if message.lower() == answer:
                    score += 1
                    conn.send(f"Bravo! your score is {score}\n\n".encode('utf-8'))
                else:
                    conn.send("Incorrect answer! Better luck next time!\n\n".encode('utf-8'))
                remove_question(index)
                index, question, answer = get_random_question_answer(conn)
            else:
                remove(conn)
                remove_nickname(nickname)
        except:
                      continue
                  
def get_random_question_answer(conn):
    random_index = random.randint(0,len(questions) - 1)
    random_question = questions[random_index]
    random_answer = answers[random_index]
    conn.send(random_question.encode('utf-8'))
    return random_index, random_question, random_answer

                  
                  
                  
def remove_question(index):
    questions.pop(index)
    answers.pop(index)
    
    
    
def remove(index):
    if index in list_of_clients:
        list_of_clients.remove(index)
        
        
        
def remove_nickname(nickname):
    if nickname in nicknames:
        nicknames.remove(nickname)
    
while True:
    conn, addr = server.accept()
    conn.send('NICKNAME'.encode('utf-8'))
    nickname = conn.recv(2048).decode('utf-8')
    list_of_clients.append(conn)
    nicknames.append(nickname)
    message = "{} joined!".format(nickname)
    
    print (nickname + "connected")
    new_thread = Thread(target= clientthread,args=(conn,nickname))
    new_thread.start()
    