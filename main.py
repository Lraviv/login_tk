'''
-----------user login with tkinter----------------------------------
a login system - user types username and password, if they're in the
existing users, they are successfully logged in. if they fail all
3 attempts, it closes tkinter window
--------------------------------------------------------------------
creator - Lihi Raviv
date created - 10/10/2021
'''
import tkinter as tk
import tkinter.messagebox as mb
import tkinter.font as tkFont
import datetime


def display():
    # initiate and display all objects on screen
    root.title("Login")
    root.geometry("450x250")
    fontStyle = tkFont.Font(family="Lucida Grande", size=20)
    global login_button

    # user name
    user_label = tk.Label(root, text="Username:", font=fontStyle)
    user_box = tk.Text(root, bg="light yellow", height=1, width=20, font=fontStyle)
    user_label.pack()
    user_box.pack()

    # password
    pass_label = tk.Label(root, text="Password:", font=fontStyle)
    pass_box = tk.Text(root, bg="light yellow", height=1, width=20, font=fontStyle)
    pass_label.pack()
    pass_box.pack()

    # login button
    log_button = tk.Button(root, text='Login', height=2, width=30,
                           command=lambda : check(user_box, pass_box))
    log_button.pack()
    root.mainloop()  # run tkinter display


def check(user, password):
    # check the password that the user typed
    # if there are 3 failed tried disable the login button
    global logs
    global atmp
    global login_state
    # get text from boxes:
    user= user.get("1.0", "end-1c")
    password = password.get("1.0", "end-1c")
    # add attempt to logs_ file
    add_to_logs(user, f"{user} has tried to log in.")
    atmp += 1
    print(user)
    # check for the username and password in the file:
    for log in logs:
        if log[0] == user and log[1] == password:
            # pop up login succeed
            login_state = True
            success_msg = f"Hello {user}, you logged in successfully"
            add_to_logs(user, f"{user} logged in successfully after {atmp} attempts")
            mb.showinfo(title="login succeed!", message=success_msg)
            root.destroy()

    # if user failed to login:
    if not login_state:
        if 0 < atmp <= 2:
            # pop up warning msg with left attempts to log in
            warning_msg = "you have " + str(3 - atmp) + " more attempts left"
            mb.showwarning(title="warning!", message=warning_msg)
        else:
            # pop up error msg if user failed all 3 attempts
            # and disable the login button
            error_msg = "too many failed attempts to login"
            mb.showerror(title="login failed", message=error_msg)
            root.destroy()


def get_from_file():
    # get from the login_users.txt all users & passwords
    # format in file - username|password
    logs = []
    with open('login_users.txt', 'r') as f:
        for line in f:
            cur = line.strip('\n\r')
            cur = cur.split("|")
            logs.append(cur)
        f.close()
    print(logs)
    return logs


def add_to_logs(user,line):
    # add attempt to record (logs_.txt)
    now = datetime.datetime.now()
    with open('logs_.txt', 'a') as f:
        f.write(line + " " + str(now) + "\n")
        f.close()


if __name__ == '__main__':
    login_state = False     # if true = user typed correct login details
    logs = get_from_file()  # file which stores all users
    atmp = 0  # counts user attempts to login
    root = tk.Tk()
    display()