import tkinter as tk
import sys
import glob
import serial
import time

class App:
    def __init__(self, master, ser):
        # TMCC Commands based on ENG 1 address of TPC 300
        self.eng1 = [0xFE, 0x00]                    # TMCC 1 command and ENG 1 address
        self.address = 0xAB                         # Set Engine Address to 1 in prg
        self.med = 0xA9                             # Med Momentum / Conventional mode
        self.throttleUp = 0xCA                      # increment throttle by 5 steps
        self.throttleDown = 0xC0                    # decrement throttle by 5 steps
        self.halt = [0xFE, 0xFF, 0xFF]              # Halt(Removes power from track)
        self.whistle = 0x9F                         # Blow Whistle
        self.forward = 0x80                         # Direction Forward
        self.neutral = 0x81                         # neutral
        self.reverse = 0x80                         # Direction Reverse
        self.currentThrottle = 0                    # Current throttle location

        self.ser = ser
        self.w2 = tk.Scale(master, from_=0, to=40, length=300, tickinterval=10, orient=tk.HORIZONTAL, command=self.update_throttle)
        self.w2.set(0)
        self.stopTrain
        self.w2.grid(row=1, column=4, padx=0, pady=0, sticky="nw")
        self.slogan = tk.Button(master,
                             text="Reverse",
                             command=self.reverse_direction)
        self.slogan.grid(row=0, column=4, padx=0, pady=0, sticky="nw")

        self.slogan = tk.Button(master,
                                text="Neutral",
                                command=self.reverse_direction)
        self.slogan.grid(row=0, column=2, padx=0, pady=0, sticky="nw")

        self.Left = tk.Button(master,
                           text="Forward", padx=10,
                           command=self.forward_direction)
        self.Left.grid(row=0, column=1, padx=0, pady=0, sticky="nw")

        self.Right = tk.Button(master,
                            text="HALT", padx=10,
                            command=self.stopTrain)
        self.Right.grid(row=0, column=6, padx=2, pady=0, sticky="nw")
        self.sweep = tk.Button(master,
                            text="Whistle",
                            command=self.blow_whistle)
        self.sweep.grid(row=0, column=8, padx=0, pady=0, sticky="nw")

    def send_tmcc(self, command):
        message = self.eng1.copy()
        message.append(command)
        message = serial.to_bytes(message)
        self.ser.write(message)

    def stopTrain(self):
        self.ser.write(serial.to_bytes(self.halt))
        self.w2.set(0)
        self.currentThrottle = 0

    def update_throttle(self, speed):
        increase_speed = (self.currentThrottle < int(speed))
        if increase_speed:
            self.send_tmcc(self.throttleUp)
        elif not increase_speed:
            self.send_tmcc(self.throttleDown)
        self.currentThrottle = int(speed)

    def goto_neutral(self):
        self.send_tmcc(self.neutral)

    def reverse_direction(self):
        self.send_tmcc(self.reverse)

    def forward_direction(self):
        self.send_tmcc(self.forward)

    def blow_whistle(self):
        self.send_tmcc(self.whistle)


ser = serial.Serial()
ser.port = '/dev/cu.usbserial-A1081AFL'
ser.baudrate = 9600
ser.timeout = 0
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
# open port if not already open
if ser.isOpen() == False:
    ser.open()
master = tk.Tk()
master.geometry('600x100')
master.title("LIONEL CONTROLLER")
app = App(master, ser)
tk.mainloop()

