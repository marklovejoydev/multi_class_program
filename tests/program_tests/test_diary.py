from lib.program.diary import Diary
from datetime import datetime

def test_initialized_as_empty_lists():
    diary = Diary()
    assert diary.entries == []
    assert diary.todos == []
    assert diary.contacts == []
    

