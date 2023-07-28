# Program to simulate a Car in text form.

started = False

while True:
    command = input(">").lower()
    if command == "help":
        print(f"start - to start the car \nstop - to stop the car \nquit - to exit")
    elif command == "start":
        if not started:
            print("Car Started.")
            started = True
        else:
            print("Car is already running.")
    elif command == "stop":
        if started:
            print("Car Stopped.")
            started = False
        else:
            print("Car already stopped.")
    elif command == "quit":
        print("Exiting")
        break
    else:
        print("Unknown Command.")
