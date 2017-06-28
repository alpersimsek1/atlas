import cv2
import numpy as np
import time
import argparse
import random
import time
from tkinter import *

from pythonosc import osc_message
from pythonosc import osc_message_builder
from pythonosc import udp_client

window = Tk()
def setIp():

    pass

def main():
    global ip
    ip = "192.168.1.4"



    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default=ip,
                                        help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=5005,
                                        help="The port the OSC server is listening on")
    args = parser.parse_args()
    client = udp_client.SimpleUDPClient(args.ip, args.port)
    client = udp_client.SimpleUDPClient(args.ip, args.port)
    msg = osc_message_builder.OscMessageBuilder(address="/filter")
        #client.send_message("/hj", message)

    def sendMsg():
        msg = e2_value.get()
        client.send_message("/hj", msg)

    e1 = Label(window, text="Your Message ")
    e1.grid(row=1, column=0)

    e2_value = StringVar()
    e2 = Entry(window, textvariable=e2_value)
    e2.grid(row=1, column=1)

    b1 = Button(window, text="Send", command=sendMsg)
    b1.grid(row=1, column=2)



main()



window.mainloop()
#while True:
#    message = input("Give me your message: ('e' for exit) ")
#    client.send_message("/hj", message)
#    if(message=="e"):
#        break

