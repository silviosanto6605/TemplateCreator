#!/usr/bin/env python3


try:
    import sys
    import os
    import shutil

    ProjectConfirmed: bool = False
    TypeOfFile = None

    while ProjectConfirmed == False:

        TypeOfProject = input("Insert the type of project you want to create: 1) HTML, 2) Electron ")
        if TypeOfProject == '1':
            NewHTMLProject = input("Please type 'create ' to create a default template for HTML/CSS/JS project, type delete to delete it...   ")
            if NewHTMLProject == "create":
                if not os.path.exists("HTMLProject"):
                    os.system("mkdir HTMLProject && cd HTMLProject && touch index.html && mkdir css img js ")
                    indexhtml = open("HTMLProject/index.html", "w")
                    indexhtml.writelines('<!DOCTYPE html>\n<html>\n<meta charset="utf-8">\n<head>\n<title>Hello World</title>\n</head>\n<body>\n<link rel=stylesheet href="css/index.css">\n<marquee>\n<h1>Hello! I am an index.html page :)</h1>\n</marquee>\n<footer>\n<h6><em>Autogenerated by Template Creator</em></h6>\n</footer>\n</body>\n</html>\n')
                    indexcss = open("HTMLProject/css/index.css","w+")
                    indexcss.writelines('body{\nbackground-color:lightgoldenrodyellow;\n}\nh1{\nfont-family: Courier;\ncolor: blue\n}\n')
                    ProjectConfirmed = True
                    print("Template created. Exiting...")
                    sys.exit()

                else:
                    deleteconf=input("You have another folder with this name. If you type yes, you are going to detroy the actual folder. To abort press ctrl+c Continue? ")
                    if deleteconf == "yes":
                        shutil.rmtree("HTMLProject")
                        sys.exit(0)


            if NewHTMLProject=="delete":
                ProjectConfirmed==True
                shutil.rmtree("HTMLProject")
                print("Project deleted!")
                sys.exit(0)



            else:
                NewHTMLProject = input("Please, retype your answer. Press enter then retype ")


#================================================================================================
#Electron

        if TypeOfProject == '2':
            NewElectronProject = input("Please type 'create ' to create a default template for Electron project, type delete to delete it...   ")
            if NewElectronProject == "create":
                if not os.path.exists("MyElectronProject"):
                    os.system("mkdir MyElectronProject && cd MyElectronProject && mkdir css img js ")
                    indexhtml = open("MyElectronProject/index.html", "w")
                    indexhtml.writelines('<!DOCTYPE html>\n<html>\n<meta charset="utf-8">\n<head>\n<title>Hello World</title>\n</head>\n<body>\n<link rel=stylesheet href="css/index.css">\n<marquee>\n<h1>Hello! I am an index.html page, BUT IN AN ELECTRON APP :)</h1>\n</marquee>\n<footer>\n<h6><em>Autogenerated by Template Creator</em></h6>\n</footer>\n</body>\n</html>\n')
                    indexcss = open("MyElectronProject/css/index.css","w+")
                    indexcss.writelines('body{\nbackground-color:lightgoldenrodyellow;\n}\nh1{\nfont-family: Courier;\ncolor: blue\n}\n')
                        #Replaced ==>     os.system("cd MyElectronProject && npm init")
                    packagejson = open("MyElectronProject/package.json","w+")
                    packagejson.writelines('{\n"name": "myElectronproject",\n"version": "1.0.0",\n"description": "",\n"main": "main.js",\n"scripts": {\n\t"start" : "electron ."\n},\n"author": "Silvio Santoriello",\n"license": ""\n}')
                    indexjs = open("MyElectronProject/main.js","w+")
                    indexjs.writelines("const { app, BrowserWindow } = require('electron')\nfunction createWindow () {\nlet win = new BrowserWindow({\nwidth: 800,\nheight: 600,\nwebPreferences: {\nnodeIntegration: true\n}\n})\nwin.loadFile('index.html')\n}\napp.on('ready', createWindow)")
                    print("Template created. Exiting...")
                    ProjectConfirmed = True
                    sys.exit()

                else:
                    deleteconf= input("You have another folder with this name. If you type yes, you are going to detroy the actual folder. To abort press ctrl+c Continue? ")
                    if deleteconf == "yes":
                        shutil.rmtree("MyElectronProject")
                        sys.exit(0)

            if NewElectronProject == "delete":
                ProjectConfirmed == True
                shutil.rmtree("MyElectronProject")
                print("Project deleted!")
                sys.exit(0)


            else:
                NewElectronProject = input("Please, retype your answer. Press enter then retype ")






except KeyboardInterrupt:
    print("     Terminating.. Have a good day. See you soon :) ")

#test branch
#Silvio Santoriello (C) 2019
