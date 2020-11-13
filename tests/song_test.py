import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Fleetwood Mac", "The Chain")
        self.song2 = Song("Dubliners", "The Rocky Road to Dublin")
        self.song3 = Song("Kate Bush", "Wuthering Heights")

    def test_find_artist(self):
        artist = "Kate Bush"
        self.assertEqual(artist, self.song3.artist)    
    
    def test_find_song(self):
        song = "The Chain"
        self.assertEqual(song, self.song1.title)
