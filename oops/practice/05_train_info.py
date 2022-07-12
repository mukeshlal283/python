from tarfile import TarInfo


class Train:

    railway = "INDIAN RAILWAY"

    def __init__(self, name, seat, fare):
        self.name = name
        self.seat = seat
        self.fare = fare

    def getStatus(self):
        print(f"train name = {self.name} ")
        print(f"seat available = {self.seat} ")

    def fareInfo(self):
        print(f"price = Rs. {self.fare} ")

    def bookTicket(self):
        if(self.seat > 0):
            print(f"your ticket has been confirm! your ticket number is \
{self.seat} ")
            self.seat = self.seat - 1
        else:
            print("sorry! seat is full")

train21 = Train("chetak express: 10021", 90, 300)
train21.getStatus()
train21.fareInfo()
train21.bookTicket()
train21.getStatus()