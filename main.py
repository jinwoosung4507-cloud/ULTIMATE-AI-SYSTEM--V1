while True:
    menu = print("1. ADD TASK\n2. SHOW TASK\n3. SHOW LEVEL\n4. ADD LEVEL\n5. DELETE LEVEL\n6. EXIT")

    command = int(input("COMMAND: ").strip())
          
    if command == 1:
        def add_task():
            f = open("task.txt","+a")
            task = input("WRITE TODAYS TASKS: ")
            task = task.upper().strip()
            f.write("\n"+task).upper()
            f.close()
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
            f = open("task.txt","w+")
            f.write(input('DELETE TASK: '))
            f.close()
        delete_task()
    
    else:
        break
    
    
    
    
    














