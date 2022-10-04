# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess:'))
#     guess_count = guess_count + 1
#     if guess == secret_number:
#         print("matches")
# i=1
# j=3
# while i <= 3:
#     inp = input("Enter your facourite color")
#     print(inp)
#     i=i+1
command =""
strarted= False
stopped= False
while True:
    command = input("Enter your command")
    if command.lower() == "start":
        if strarted:
            print("already started")
        else:
            strarted = True
            print("car is ready to go")
    elif command.lower() == "stop":
        if stopped:
            print("already stopped")
        else:
            stopped = True
            print("stop car")
    elif command.lower() == "help":
        print("""
start:raedy to car
stop:stop the car
quit:quit the car""")
    elif command.lower() == "quit":
        quit()
    else:
        print("sorry i canot understand")
