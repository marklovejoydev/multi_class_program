from lib.exercise.diary_entry import DiaryEntry
"""
initialize with title and contents 
i get access title and contents
"""

def test_initialize_with_title_and_contents():
    diary_entry = DiaryEntry("My Title", "My Content")
    assert diary_entry.title == "My Title"
    assert diary_entry.contents == "My Content"



def test_counts_words_of_contents():
    diary_entry = DiaryEntry("My Title", "My Content is now longer")
    assert diary_entry.count_words() == 5
    
def test_reading_time():
    diary_entry= DiaryEntry("My Title", "My Content is now longer")
    assert diary_entry.reading_time(2) ==3
    
def test_returns_first_chunk():
    diary_entry= DiaryEntry("My Title", "My Content is now longer")
    assert diary_entry.reading_chunk(2, 1) == "My Content"
    
def test_returns_second_chunk_when_called_again():
    diary_entry= DiaryEntry("My Title", "My Content is now longer")
    diary_entry.reading_chunk(2, 1) == "My Content"
    assert diary_entry.reading_chunk(2, 1) == "is now"
    
def test_starts_again_once_reading_complete_if_continued():
    diary_entry= DiaryEntry("My Title", "My Content is now longer")
    diary_entry.reading_chunk(2, 1) == "My Content"
    diary_entry.reading_chunk(3, 1) == "is now longer"
    assert diary_entry.reading_chunk(2, 1) == "My Content"
    