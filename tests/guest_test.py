import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Stevie", 39, "The Chain", 10)
        self.guest2 = Guest("Luke", 45, "The Rocky Road to Dublin", 150)
        self.guest3 = Guest("Marianne", 31, "Wuthering Heights", 20)
        
    def test_guest_name(self):
        guest = "Stevie"
        self.assertEqual(guest, self.guest1.name)

    def test_guest_fav_song(self):
        song = "The Rocky Road to Dublin"
        self.assertEqual(song, self.guest2.fav_song)
