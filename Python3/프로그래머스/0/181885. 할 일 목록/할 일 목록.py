def solution(todo_list, finished):
    return [i for index,i in enumerate(todo_list) if not finished[index]]