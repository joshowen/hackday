import soco

sonos = soco.discover().pop()



sonos.play_uri("https://dl.dropboxusercontent.com/u/21513800/05%20An%20Eluardian%20Instance.mp3?dl=1")



def get_currently_playing():
    pass


SONOS = None

def _get_sonos():
    