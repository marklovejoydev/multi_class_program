from datetime import datetime

class DiaryEntry:
    def __init__(self, title, content, date_time=None):
        self.title = title
        self.content = content
        self.date_time = date_time if date_time is not None else datetime.now().strftime('%d/%m/%Y')
        
    
    def count_words(self):
        pass
    
    def reading_time(self, wpm):
        pass
    
    # maybe
    
    def format_entry(self):
        pass
    