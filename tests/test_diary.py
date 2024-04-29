from lib.exercise.diary import Diary
import pytest

def test_instance_of_diary_initially_is_empty():
    diary = Diary()
    assert diary.all() == []
    
def test_word_count_initally_zero():
    diary = Diary()
    assert diary.count_words() == 0
    
def test_throws_err_when_attempt_to_read_with_no_contents():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.reading_time(2)
    assert str(err.value) == "No contents entered to read"