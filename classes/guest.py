class Guest:
    def __init__(self, name, age, fav_song, wallet):
        self.name = name 
        self.age = age
        self.fav_song = fav_song
        self.wallet = wallet


    # # check for sufficient funds
    def sufficient_funds(self, cost):
        return self.wallet >= cost.fee

    # # check fav_song

    def favourite_song(self, song_name):
        return self.fav_song(song_name)

