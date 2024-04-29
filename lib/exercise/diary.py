import math

class Diary:
    def __init__(self):
        self._diary_list = []

    def add(self, entry):
        self._diary_list.append(entry)

    def all(self):
        return self._diary_list

    def count_words(self):
        word_counts = [entry.count_words() for entry in self._diary_list]
        return sum(word_counts)

    def reading_time(self, wpm):
        if self._diary_list == []:
            raise Exception("No contents entered to read")
        word_count = self.count_words()
        return math.ceil(word_count / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        chunk_user_can_read = wpm * minutes
        most_readable_entry = None
        longest_found_so_far = 0
        for entry in self._diary_list:
            if entry.count_words() <= chunk_user_can_read:
                if entry.count_words() > longest_found_so_far:
                    most_readable_entry =entry
                    longest_found_so_far = entry.count_words()
        return most_readable_entry
            
