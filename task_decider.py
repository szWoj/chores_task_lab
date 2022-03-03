def get_preffered_option(task1, task2):
    if (task1.description == "Cooking Dinner" or task2.description == "Cooking Dinner") and (task1.description == "Washing Dishes" or task2.description == "Washing Dishes"):
        return "Washing Dishes"
    elif (task1.description == "Cooking Dinner" or task2.description == "Cooking Dinner") and (task1.description == "Cleaning Windows" or task2.description == "Cleaning Windows"):
        return "Cooking Dinner"
    elif (task1.description == "Washing Dishes" or task2.description == "Washing Dishes") and (task1.description == "Cleaning Windows" or task2.description == "Cleaning Windows"):
        return "Cleaning Windows"
    else:
        return "This task does not exist"

def does_task_exist(task):
    if task.description:
        return True
    return False


def get_longest_task(task1, task2):
    if task1.duration == task2.duration:
        return "Tasks take the same amount of time."
    elif task1.duration > task2.duration:
        return task1.description
    return task2.description 
    







