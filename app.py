print("Hello, here's a way to orgainse your tasks more efficiently! Begin by typing either of the following commands...")
print("===================================================")
print("Please bear in mind the syntax for entering your request.")
print("'add <task name>' adds a new task with the name <task name>.")
print("'show' displays all your current tasks to do.")
print("'edit <task id>' edits the task with the id <task id>.")
print("'complete <task id>' removes the task with the id <task id>.")
print("'exit' quits the program.")
print("===================================================")
with open("user_data.txt", "r") as file:
    todos = file.readlines()
if todos:
    print("Here are your existing todos.")
    for index, item in enumerate(todos):
        item_wo_break = item.strip('\n')
        print(f"{index+1}. {item_wo_break}")
    print("===================================================")

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.lower()
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        with open("user_data.txt", "r") as file:
            todos = file.readlines()
            todos.append(todo)
        
        with open("user_data.txt", "w") as file:
            file.writelines(todos)

        for index, item in enumerate(todos):
            item_wo_break = item.strip('\n')
            print(f"{index+1}. {item_wo_break}")

        todo_wo_break = todo.strip('\n')
        print(f"The item '{todo_wo_break}' was added to your to do list. You now have {len(todos)} thing(s) left to do.")
    
    elif user_action.startswith("show"):
        with open("user_data.txt", "r") as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
            item_wo_break = item.strip('\n')
            print(f"{index+1}. {item_wo_break}")
        print(f"You have {len(todos)} thing(s) left to do.")
    
    elif user_action.startswith("edit"):
        for index, item in enumerate(todos):
            item_wo_break = item.strip('\n')
            print(f"{index+1}. {item_wo_break}")
        try:
            edit_position = int(user_action[5:])
            edit_position = edit_position - 1
            todo_wo_break = todos[edit_position].strip('\n')
            edited_todo = input(f"What do you want to replace '{todo_wo_break}' with? ") + "\n"

            with open("user_data.txt", "r") as file:
                todos = file.readlines()
                previous_value = todos[edit_position]
                todos[edit_position] = edited_todo
            
            with open("user_data.txt", "w") as file:
                file.writelines(todos)

            todo_wo_break = edited_todo.strip('\n')
            prev_wo_break = previous_value.strip('\n')
            print(f"The item '{prev_wo_break}' was updated to '{todo_wo_break}'!")
        except:
            with open("user_data.txt", "r") as file:
                todos = file.readlines()
            data_verify = user_action[5:] + '\n'
            if data_verify in todos:
                todo_wo_break = user_action[5:].strip('\n')
                edited_todo = input(f"What do you want to replace '{todo_wo_break}' with? ") + "\n"
                edit_position = todos.index(data_verify)
                with open("user_data.txt", "r") as file:
                    todos = file.readlines()
                    previous_value = todo_wo_break
                    todos[edit_position] = edited_todo
                
                with open("user_data.txt", "w") as file:
                    file.writelines(todos)

                todo_wo_break = edited_todo.strip('\n')
                prev_wo_break = previous_value.strip('\n')
                print(f"The item '{prev_wo_break}' was updated to '{todo_wo_break}'!")
            else:
                print("Did not find that task in your list. Consider using the 'add' command.")

    
    elif user_action.startswith("complete"):
        try:
            complete = int(user_action[9:])
            complete = complete - 1
            with open("user_data.txt", "r") as file:
                todos = file.readlines()
                task_completed = todos[complete]
                todos.pop(complete)

            with open("user_data.txt", "w") as file:
                file.writelines(todos)

            for index, item in enumerate(todos):
                item_wo_break = item.strip('\n')
                print(f"{index+1}. {item_wo_break}")
            completed_wo_break = task_completed.strip('\n')
            print(f"The task '{completed_wo_break}' was removed from your list! You now have {len(todos)} thing(s) left to do.")
        except:
            with open("user_data.txt", "w") as file:
                file.truncate()
            with open("user_data.txt", "r") as file:
                todos = file.readlines()
            print(f"All the tasks were removed from your list! You now have {len(todos)} thing(s) left to do.")
        
    
    elif user_action.startswith("exit"):
        break
    
    else:
        print("Sorry, your input was invalid. Please try again!")

print("Until next time!")