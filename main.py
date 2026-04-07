print("1. ADD TASK\n2. SHOW TASK\n3. EXIT")

command = int(input("COMMAND: ").strip())

if command == 1:
    def add_task():
        f = open("task.txt","+a")
        task = input("WRITE TODAYS TASKS: ")
        f.write("\n"+task)
        f.close()
    add_task()

elif command == 2: 
    def show_task():
        f = open("task.txt","r")
        data = f.read()
        print(data)
    show_task()










