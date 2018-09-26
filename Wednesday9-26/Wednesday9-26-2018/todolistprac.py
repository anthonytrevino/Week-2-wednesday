

tasks =[]


class Task:
    def __init__(self,task_name):
        self.task_name = task_name



class Menu:
    def __init__(self):
        pass


    def add_new_task(self,new_task):

        tasks.append(task)

    def remove_task(self,task_name):
        pass

    def quit(self):
        print("Thank you for using the app! ")

menu = Menu()

while True:
    choice =input("Enter a choice: ")
    if(choice =="1"):
        new_task = input("Enter a task: ")
        task = Task(new_task)
        menu.add_new_task(task)

        for task in range(len(tasks)) :
            print(tasks[task].task_name)
            task += 1


    if(choice =="2"):
        removed_task = input("Which task do you want to remove? ")
        # task = Task(removed_task)

        #menu.remove_task(removed_task)

        for task in range(len(tasks)):
            if(removed_task ==tasks[task].task_name):
                tasks.remove(tasks[task])

        for task in range(len(tasks)) :
            print(tasks[task].task_name)
            task += 1



    if(choice =="3"):
        menu.quit()
        break
