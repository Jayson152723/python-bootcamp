class Door:
    def __init__(self, closed):
        self.closed = closed

    def open_door(self):
        print("The door is open")
        self.closed = False

    def close_door(self):
        print("The door is close")
        self.closed = True

door_status = Door(False)
door_status.close_door()

