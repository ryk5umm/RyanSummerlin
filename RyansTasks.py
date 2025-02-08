import pandas as pd
import colorama
from colorama import Fore, Back, Style

df = pd.read_csv("TaskList.csv")

print("\n")
print("Welcome to Ryan's Tasks...")
print("\n")

print('''
           _ -  /  -  _
         -      /       -
       -        /         -
     -          /           -
    _           /            _
    _           /             _
  ( / / / / / / 0/ / / / / / / )
  0 _           /            _ 0
  #  _          /           _  #
  #   _         /          _   #
  #     _       /        _     #
  0        -  _ / _   -        0
 /I             0             /I
//I             #            //I
//I             #            //I
//I             0            //I
 /I            /I             /I
  v           //I              v
              //I
              //I
               /I
                V

    .                  .-.    .  _   *     _   .
           *          /   \     ((       _/ \       *    .
         _    .   .--'\/\_ \     `      /    \  *    ___
     *  / \_    _/ ^      \/\'__        /\/\  /\  __/   \ *
       /    \  /    .'   _/  /  \  *' /    \/  \/ .`'\_/\   .
  .   /\/\  /\/ :' __  ^/  ^/    `--./.'  ^  `-.\ _    _:\ _
     /    \/  \  _/  \-' __/.' ^ _   \_   .'\   _/ \ .  __/ \\
   /\  .-   `. \/     \ / -.   _/ \ -. `_/   \ /    `._/  ^  \\
  /  `-.__ ^   / .-'.--'    . /    `--./ .-'  `-.  `-. `.  -  `.
@/        `.  / /      `-.   /  .-'   / .   .'   \    \  \  .-  \%
@&8jgs@@\%\% @)&@&(88&@.-_=_-=_-=_-=_-=_.8@% &@&&8(8%@%8)(8@%8 8%@)%
@88:::&(&8&&8:::::%&`.~-_~~-~~_~-~_~-~~=.'@(&%::::%@8&8)::&#@8::::
`::::::8%@@%:::::@%&8:`.=~~-.~~-.~~=..~'8::::::::&@8:::::&8:::::'
 `::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.'
      
      ''')

print(df)
print("\n")

# df['priority'] = df['priority'].apply(pd.to_numeric)

# for i in df["priority"]:
#      df["priority"][i] = int(df['priority'][i])

us_ip = input("Add, Remove, or Exit? ")
print(us_ip)

status = True

def task_function(ipt):
    global df
    global status
    while status == True:
        if ipt == "Add":
            print("\n")
            print("Add new task")
            print("\n")
            add_input = input("New task: ")
            add_priority = int(input("Priority (1, 2, or 3): "))
            add_df = pd.DataFrame([[add_input, add_priority]], columns=['task', 'priority'])
            df = pd.concat([df, add_df], axis=0, ignore_index=False)
            # Appears that priority is going from int to object here
            # Solution was to make certain the input is turned into an "int"
            df = df.sort_values('priority', ascending=True)
            print(df)
            print("\n")
            return_input = input("Add, Remove, or Exit? ")
            task_function(return_input)
        elif ipt == "Remove":
            print("\n")
            remove_input = input("Name of task to remove: ")
            
            # From here, I need to use the input to create a new DF without the identified row
            df = df.loc[df['task'] != remove_input, :]

            print(df)
            print("\n")
            return_input = input("Add, Remove, or Exit? ")
            task_function(return_input)
        elif ipt == "Exit":
            add_input_2 = input("Are you sure?: ")
            if add_input_2 == "Y":
                    status = False
                    print("\n")
                    print("//////////////////////////////////////////")
                    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
                    print("\n")
                    print("\n")
                    print("Farewell, Young Warrior...")
                    print("\n")
                    print('''

                 ___                          (_)
               _/XXX\\
_             /XXXXXX\\_                                    __
X\\__    __   /X XXXX XX\\                          _       /XX\\__      ___
    \\__/  \\_/__       \\ \\                       _/X\\__   /XX XXX\\____/XXX\\
  \\  ___   \\/  \\_      \\ \\               __   _/      \\_/  _/  -   __  -  \\__/
 ___/   \\__/   \\ \\__     \\\\__           /  \\_//  _ _ \\  \\     __  /  \\____//
/  __    \\  /     \\ \\_   _//_\\___     _/    //           \\___/  \\/     __/
__/_______\\________\\__\\_/________\\_ _/_____/_____________/_______\\____/_______
                                  /|\\
                                 / | \\
                                /  |  \\
                               /   |   \\
                              /    |    \\
                             /     |     \\
                            /      |      \\
                           /       |       \\
                          /        |        \\
                         /         |         \\

''')
                    print("\n")
                    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
                    print("//////////////////////////////////////////")
                    print("\n")
                    print("\n")
            else:
                    print(df)
                    #I want to be able to return to the top of the function
        else:
            print("Invalid input.")
    else:
        print("Press Enter to exit...")

print(task_function(us_ip))

df.to_csv('TaskList.csv', sep=',', index=False)