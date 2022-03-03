def get_preffered_option(task1, task2):
    if (task1.description == "Cooking Dinner" or task2.description == "Cooking Dinner") and (task1.description == "Washing Dishes" or task2.description == "Washing Dishes"):
        return "Washing Dishes"

