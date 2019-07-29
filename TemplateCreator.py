#!/usr/bin/env python3

try:
    import sys
    import os

    ProjectConfirmed = False

    while ProjectConfirmed == False:
        NewProject = input("Please type 'create ' to create a default template for HTML/CSS/JS project, type delete to delete it...   ")

        if NewProject == "create":
            if not os.path.exists("Project1"):
                os.system("mkdir Project1 && cd Project1 && touch index.html && mkdir css img js ")
                ProjectConfirmed = True
                print("Template created. Exiting...")
                sys.exit()
            else:
                deleteconf= input("You have another folder with this name. If you type yes, you are going to detroy the actual folder. To abort press ctrl+c Continue? ")
                if deleteconf == "yes":
                    os.system("rm -rf Project1")
                    sys.exit(0)


        if NewProject == "delete":
            ProjectConfirmed == True
            os.system("rm -rf Project1")
            print("Project deleted!")
            sys.exit(0)



        else:
            NewProject = input("Please, retype your answer. Press enter then retype ")

except KeyboardInterrupt:
    print("Have a good day... See you soon :) ")

#test branch