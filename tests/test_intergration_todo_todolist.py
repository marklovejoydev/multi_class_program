from lib.exercise.challenge.todo import Todo
from lib.exercise.challenge.todo_list import TodoList

"""
when added todos are initiated as False
returns bool
"""

def test_adds_todo_that_initiates_as_false():
    todo_list = TodoList()
    todo_list.add(Todo("wash car"))
    result =  todo_list.incomplete()
    assert result == ["wash car"]
    
def test_marks_todo_as_complete():
    todo_list = TodoList()
    todo = Todo("wash car")
    todo_list.add(todo)
    todo.mark_complete()
    result = todo_list.incomplete()
    assert result == []

def test_marks_todo_as_complete_and_incomplete():
    todo_list = TodoList()
    todo1 = Todo("wash car")
    todo2 = Todo("clean kitchen")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo1.mark_complete()
    result = todo_list.incomplete()
    assert result == ["clean kitchen"]

def test_give_up_marks_all_todos_as_complete():
    todo_list = TodoList()
    todo1 = Todo("wash car")
    todo2 = Todo("clean kitchen")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.give_up()
    assert todo1.complete == True
    assert todo2.complete == True