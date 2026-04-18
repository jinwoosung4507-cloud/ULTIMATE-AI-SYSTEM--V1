while True:
    menu = print("1. ADD TASK\n2. SHOW TASK\n3. SHOW LEVEL\n4. ADD LEVEL\n5. DELETE TASK\n6. EXIT")

    command = int(input("COMMAND: ").strip())
          
    if command == 1:
        def add_task():
            f = open("task.txt","+a")
            task = input("WRITE TODAYS TASKS: ")
            task = task.upper().strip()
            f.write("\n"+task)
            f.close()  
        task = list  
        add_task()

    elif command == 2: 
        def show_task():
            f = open("task.txt","r")
            data = f.read()
            print(data)
        show_task()

    elif command == 3:
        def show_level():
            f = open("level.txt","r")
            data = f.read()
            print(data)
            f.close()
        show_level()

    elif command == 4:
        def add_level():
            f = open("level.txt","w")
            f.write(input("UPGRADE LEVEL: "))
            f.close()
        add_level()

    elif command == 5:
        def delete_task():
            with open("task.txt","r") as file: 
                tasks = file.readlines()
            if len(tasks) == 0: 
                print("NO task available!")
            else: 
                print("\nYour tasks:")
                for i in range(len(tasks)):
                    print(f"{i+1}.{tasks[i].strip()}")
                
                try:
                    choice =int(input("\nEnter task number to delete: "))

                    if choice < 1 or choice > len(tasks):
                        print("invalid choice")
                    else:
                        index = choice - 1 

                        removed_task = tasks.pop(index)

                        with open("tasks.txt","w") as file:
                            for task in tasks:
                                file.write(task)
                        
                        print(f"task'{removed_task.strip()}' deleted successfully ")
                
                except ValueError:
                    print("please enter a valid number")
                
        delete_task()


    else:
        break


    
    
    
    
    














