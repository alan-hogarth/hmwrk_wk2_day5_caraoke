class Room:
    def __init__(self, name, capacity, fee):
        self.name = name
        self.capacity = capacity
        self.fee = fee
        self.guest_list = []
        self.song_list = []
        
# # method to check song_count in room

    def song_count(self):
        return len(self.song_list)
    
# method to check fav song
    def favourite_song(self, song_name):
        return self.fav_song(song_name)

# # method to add songs to list 

    def add_song(self, song_1):
        self.song_list.append(song_1)

# # method to check room capacity

    def current_capacity(self):
        return len(self.guest_list)

# # method to check for funds

    def sufficient_funds(self, cost):
        return self.wallet >= cost.fee

# # method to add guest

    def add_guest(self, guest1):
        self.guest_list.append(guest1) 

# # method to remove guest

    def remove_guest(self, guest2):
        self.guest_list.remove(guest2)

# method to check if fav_song is on list and to add if not
    def find_song(self, song_title):
        for song_2 in self.song_list:
            if song_2["title"] == self.favourite_song:
                return "Woohoo!!"
            else:
                self.add_song(song_title)
           

#  method to check in guest:
#  if they have sufficient funds  
#  and if room capacity is not reached

    def check_in(self, guest_name):
        max_cap = self.capacity
        entry_guaranteed = len(self.guest_list)

        if entry_guaranteed < max_cap and self.sufficient_funds:
            self.add_guest(guest_name.name)
        else:
            return "Sorry, no admittance"
        
            




