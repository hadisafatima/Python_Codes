import re
pattern = re.compile(r"[a-z]+[!@#$%^&*()]+[0-9]+$") # this command specifies a pattern for the password

userPassword = "none"
while(userPassword == "none") :
    print("Enter a strong password for your account : ")
    userPassword = input()

    strongPassword = re.search(pattern, userPassword) # search() of "re" module searches for the first occurance of hte string, in this case userPassword, and matches it with the specified pattern, in this case "pattern"

    if(strongPassword) :
        print("Password is Strong!")
    else :
        print("provide a password containing alphabets, special characters and then numbers")
        userPassword = "none"


# 1- git init (initialize an empty repo)

# 2- git add . (tells git what folders/files it need to track and "." means all the files of the current folder)

# 3- git commit -am "any msg" (-a : Stands for "all" and stages all changes to tracked files (files that are already  being tracked by Git). -m : As before, this allows you to specify a commit message) -> now local git repo is initialized

# 4- fir pushing it to a git URL we have to run this command "git remote add origin _the repo URL_"

# 5- to check if remote URL is sucessfully added or not we have to run "git remote -v"