from lib.program.diary_entry import *
from lib.program.diary import Diary


test_date_format = datetime.now().strftime('%d/%m/%Y')


def test_add_entry():
    diary = Diary()
    entry = DiaryEntry("Title", "Content", test_date_format)
    diary.add_entry(entry)
    assert diary.all_entries() == ["Title", "Content", test_date_format]