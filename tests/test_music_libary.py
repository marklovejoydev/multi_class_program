from lib.music_libary import MusicLibrary

    
def test_initially_no_tracks():
    library = MusicLibrary()
    assert library.all() == []
    
def test_search_in_empty_list_returns_empty_list():
    library = MusicLibrary()
    assert library.search_by_title("something") == []