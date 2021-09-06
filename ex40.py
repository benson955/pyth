class Song(object):
    
    def __init__(self,lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = (["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = (["They rally around the family",
                        "With pockets full of shells"])

marine_parade = (["Queen Victoria",
                        "I've missed you so bad "])

let_it_go = (["From walking home and talking loads",
                        "To seeing shows in evening clothes with you"])

songplayer = Song(marine_parade)
songplayer.sing_me_a_song()