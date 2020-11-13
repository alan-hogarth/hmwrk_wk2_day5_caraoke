import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Stevie", 39, "The Chain", 10)
        self.guest2 = Guest("Luke", 45, "The Rocky Road to Dublin", 150)
        self.guest3 = Guest("Marianne", 31, "Wuthering Heights", 20)
        
        # self.room1 = Room("Osaka", 5, 20)
        self.room = Room("Tokyo", 3, 20)

    def test_guest_name(self):
        guest = "Stevie"
        self.assertEqual(guest, self.guest1.name)

    def test_guest_fav_song(self):
        song = "The Rocky Road to Dublin"
        self.assertEqual(song, self.guest2.fav_song)

    def test_sufficient_funds__true_if_enough(self):
        self.assertEqual(True, self.guest2.sufficient_funds(self.room))

    def test_sufficient_funds__false_if_not(self):
        poor_guest = Guest("Stevie", 39, "The Chain", 10)
        self.assertEqual(False, poor_guest.sufficient_funds(self.room))