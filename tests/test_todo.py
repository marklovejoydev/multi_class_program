from lib.exercise.challenge.todo import Todo

def test_todo_initialization():
    todo = Todo("clean car")
    assert todo.task == "clean car"
    assert todo.complete == False

def test_mark_complete():
    todo = Todo("clean car")
    todo.mark_complete()
    assert todo.complete == True