from pwn import socket
import time
import random

class Netcat:

    """ Python 'netcat like' module """

    def __init__(self, ip, port):

        self.buff = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def read(self, length=1024):
        """ Read 1024 bytes off the socket """

        return self.socket.recv(length)

    def read_until(self, data):
        """ Read data into the buffer until we have data """

        while not data in self.buff:
            self.buff += self.socket.recv(1024)

        pos = self.buff.find(data)
        rval = self.buff[:pos + len(data)]
        self.buff = self.buff[pos + len(data):]

        return rval

    def write(self, data):

        self.socket.send(data)

    def close(self):

        self.socket.close()

with open('words.txt', 'r') as f:
    words = f.read().split('\n')

def two_words_n_comman_letters(w1, w2, num):
    counter = 0
    for char in w1:
        if char in w2:
            counter += 1
    return counter == num


def solve(c, out, words):
    choice = random.choice(words)
    c.write(choice.encode())
    out = c.read()
    while out:
        print(out)
        if (len(out) > 2):
            break
        words = [word for word in words if two_words_n_comman_letters(word, choice, int(out))]
        choice = random.choice(words)
        c.write(choice.encode())
        out = c.read()


nc = Netcat("tricky-guess.csa-challenge.com", 2222)
time.sleep(0.1)
output = nc.read()

while output:
    time.sleep(0.1)
    output = nc.read()
    if output == b'GO !\n':
        solve(nc, output, words)
