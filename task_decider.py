def get_preffered_option(task1, task2):
    if (task1.description == "Cooking Dinner" or task2.description == "Cooking Dinner") and (task1.description == "Washing Dishes" or task2.description == "Washing Dishes"):
        return "Washing Dishes"
    if (task1.description == "Cooking Dinner" or task2.description == "Cooking Dinner") and (task1.description == "Cleaning Windows" or task2.description == "Cleaning Windows"):
        return "Cooking Dinner"
    if (task1.description == "Washing Dishes" or task2.description == "Washing Dishes") and (task1.description == "Cleaning Windows" or task2.description == "Cleaning Windows"):
        return "Cleaning Windows"

def does_task_exist(task):
    if task.description:
        return True
    return False

