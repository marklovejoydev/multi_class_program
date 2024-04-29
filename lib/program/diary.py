class Diary:
    def __init__(self):
        self.entries = []
        self.contacts = []
        self.todos = []
    
    def add_entry(self, entry):
        self.entries.append(entry)
    
    def all_entries(self):
        return self.entries
    
    def read_entry(self, entry):
        pass
    
    def count_words(self):
        pass
    
    def reading_time(self, wpm):
        pass
    
    def list_of_entries_for_reading_time(self, wpm):
        pass
    
    def all_todos(self, todos):
        pass
    
    def all_contacts(self, contacts):
        pass