from lib.exercise.diary import Diary
from lib.exercise.diary_entry import DiaryEntry

"""
adds two diary entries 
see them in list
"""

def tests_adds_and_list_diary_entrys():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1","Contents 1")
    entry_2 = DiaryEntry("Title 2","Contents 2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]
    
"""
add 2 diary entries
count words will get sum of all words in the entry
"""

def tests_adds_two_entries_gets_sum_of_all_words_in_contents():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1","Contents 1")
    entry_2 = DiaryEntry("Title 2","counts two more")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 5
    
"""
given int of wpm 
returns int of est to read all 
"""

def tests_reading_time_to_read_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1","Contents 1 again")
    entry_2 = DiaryEntry("Title 2","counts two more")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(2) == 3
    
def tests_reading_time_to_read_all_entries_rounds_up():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1","Contents 1")
    entry_2 = DiaryEntry("Title 2","counts two more")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(2) == 3
    
"""
add two entries one long one short
call find entry for reading time 
with a wpm and min that mean i can only read a short one
"""

def test_shows_content_that_can_be_read_in_given_time():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1","Contents 1")
    entry_2 = DiaryEntry("Title 2","counts two more and then another one")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_1
    
def test_shows_empty_list_if_can_not_be_read_in_given_time():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1","counts two more and then another one and another")
    entry_2 = DiaryEntry("Title 2","counts two more and then another one")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 3) == None
    
def test_if_both_contents_can_be_read_in_time_return_longest():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1","Contents 1")
    entry_2 = DiaryEntry("Title 2","counts two more and then another")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_2