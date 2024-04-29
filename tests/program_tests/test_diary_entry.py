from lib.program.diary_entry import DiaryEntry, datetime

def test_initialize_with_title_and_contents():
    diary_entry = DiaryEntry("My Title", "My Content")
    assert diary_entry.title == "My Title"
    assert diary_entry.content == "My Content"
    
def test_initialize_with_default_datetimenow_when_no_time_passed():
    diary_entry = DiaryEntry("My Title", "My Content")
    assert diary_entry.date_time == datetime.now().strftime('%d/%m/%Y')

def test_initalize_with_given_date_when_passed_date():
    diary_entry = DiaryEntry("My Title", "My Content","02/10/1989")
    assert diary_entry.date_time == "02/10/1989"