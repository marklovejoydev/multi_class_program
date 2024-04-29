from lib.track import Track

def test_construct_track_and_get_artist_and_title():
    track = Track("My Title", "My Artist")
    assert track.title == "My Title"
    assert track.artist == "My Artist"
    
def test_formats_title_and_artist():
    track = Track("My Title", "My Artist")
    assert track.format() == "My Title by My Artist"