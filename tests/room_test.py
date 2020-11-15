import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        # self.room1 = Room("Osaka", 5, 20)
        self.room = Room("Tokyo", 3, 20)

        self.song1 = Song("Fleetwood Mac", "The Chain")
        self.song2 = Song("Dubliners", "The Rocky Road to Dublin")
        self.song3 = Song("Kate Bush", "Wuthering Heights")

        self.guest1 = Guest("Stevie", 39, "The Chain", 10)
        self.guest2 = Guest("Luke", 45, "The Rocky Road to Dublin", 150)
        self.guest3 = Guest("Cathy", 31, "Wuthering Heights", 200)


    def test_room_name(self):
        room_name = "Tokyo"
        self.assertEqual(room_name, self.room.name)

    def test_room_capacity(self):
        self.assertEqual(3, self.room.capacity)
    
    def test_room_fee(self):
        self.assertEqual(20, self.room.fee)

    def test_song_start_at_0(self):
        self.assertEqual(0, self.room.song_count())
        
    def test_add_song(self):
        self.room.add_song(self.song1)
        self.assertEqual(1, self.room.song_count())
      
    def test_room_current_capacity(self):
        self.assertEqual(0, self.room.current_capacity())
    
    def test_add_guest(self):
        self.room.add_guest(self.guest1)
        self.assertEqual(1, self.room.current_capacity())

    def test_find_song(self):
        song = "The Chain"
        self.room.find_song(self.room.song_list)
        self.assertEqual(song, self.guest1.fav_song)
    
    def test_check_in(self):
        self.room.check_in(self.guest1)
        self.assertEqual(["Stevie"], self.room.guest_list)
        
    



