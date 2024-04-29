from lib.exercise.challenge.todo_list import TodoList

"""
Will add a todo to the list
return the list
"""

def test_adds_a_todo_and_returns_it():
    todo_list = TodoList()
    todo_list.add("clean car")
    assert todo_list.all() == ["clean car"]
    
def test_adds_two_todo_and_returns_it():
    todo_list = TodoList()
    todo_list.add("clean car")
    todo_list.add("clean kitchen")
    assert todo_list.all() == ["clean car", "clean kitchen"]
    
