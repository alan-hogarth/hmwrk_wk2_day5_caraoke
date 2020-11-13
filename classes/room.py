class Room:
    def __init__(self, name, capacity, fee):
        self.name = name
        self.capacity = capacity
        self.fee = fee
        self.guest_list = []
        self.song_list = []
        

# fucntion to check song_count in room
    def song_count(self):
        return len(self.song_list)
    
# function to add songs to list 
    def add_song(self, song_1):
        self.song_list.append(song_1)

# check room capacity
    def current_capacity(self):
        return len(self.guest_list)

# add guest
    def add_guest(self, guest1):
        self.guest_list.append(guest1) 

# remove guest
    def remove_guest(self, guest2):
        self.guest_list.pop(guest2)

# function to check if fav_song is on list

# check in guest
#  if they have sufficient funds
    
#  and if their fav_song is in room
# if room capacity is not reached