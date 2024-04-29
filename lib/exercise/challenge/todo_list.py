class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.todos.append(todo)
    
    def all(self):
        # returns a list of all todos 
        return self.todos
    
    def incomplete(self):
        return [todo.task for todo in self.todos if not todo.complete]

    def complete(self):
        return [todo.task for todo in self.todos if todo.complete]

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for todo in self.todos:
            todo.mark_complete()
