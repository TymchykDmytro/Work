


import os


libs = {"sqlite3", "requests", "selenium"};

try:
    for lib in libs:
        print("start install {0}".format(lib));
        os.system("pip install " + lib);
        print("{} install successful".format(lib));
    print("All Successful");
except:
    print("Failed SomeHow");
