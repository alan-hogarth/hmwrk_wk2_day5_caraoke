import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Osaka", 5, 20)

        self.song1 = Song("Fleetwood Mac", "The Chain")
        self.song2 = Song("Dubliners", "The Rocky Road to Dublin")
        self.song3 = Song("Kate Bush", "Wuthering Heights")

        self.guest1 = Guest("Stevie", 39, "The Chain", 100)
        self.guest2 = Guest("Luke", 45, "The Rocky Road to Dublin", 150)
        self.guest3 = Guest("Marianne", 31, "Wuthering Heights", 200)


    def test_room_name(self):
        room_name = "Osaka"
        self.assertEqual(room_name, self.room.name)

    def test_room_capacity(self):
        self.assertEqual(5, self.room.capacity)
    
    def test_room_fee(self):
        self.assertEqual(20, self.room.fee)

    def test_add_guest_to_room(self):
        