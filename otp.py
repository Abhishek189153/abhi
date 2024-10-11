# import tkinter as tk
# from tkinter import messagebox
# def verify_otp():
#     otp="12345"
#     user_input=otp_entry.get()
#     if user_input==otp:
#         messagebox.showinfo("success","OTP is verified")
#     else:
#         messagebox.showinfo("Failed","Try again")


# window=tk.Tk()
# window.title("OTP Verification")
# otp_label=tk.Label(window,text="Enter OTP")
# otp_label.pack()
# otp_entry=tk.Entry(window,show='*')
# otp_entry.pack()
# button=tk.Button(window,text="submit", command=verify_otp)
# button.pack()
# window.mainloop()





# count=0
import math, random
import tkinter as tk
from tkinter import messagebox
# def verify_otp():
#     otp="12345"
def generateOTP():
    digits = "0123456789"
    OTP=" "
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]

    messagebox.showinfo("success",OTP)
    printopt=tk.Label(window,text=OTP)
    printopt.pack()
    

# if __name__ == "__main__" :
#     generateOTP()
#     print("your OTP is :",generateOTP())


    
    # user_input=otp_Entry.get()
    # if button==Generate():
    # messagebox.showinfo("success",generateOTP())
    # else:
    #     messagebox.showinfo("Failed","Try again")
def check_otp():
    user_input=otp_entry.get()
    if user_input==OTP:
        messagebox.showinfo("success","OTP is verified")
    else:
        messagebox.showinfo("Failed","Try again")


window=tk.Tk()
window.title("OTP Generate")

# otp_entry=tk.Entry(window,show='*')
# otp_entry.pack()
button=tk.Button(window,text="Generate", command=generateOTP)
button.pack()

otp_label=tk.Label(window,text="Enter OTP")
otp_label.pack()
otp_entry=tk.Entry(window,show='*')
otp_entry.pack()
button=tk.Button(window,text="submit",command=check_otp)
button.pack()
# printopt=tk.Label(window,text="")
# printopt.pack()


# messagebox.showinfo("success",generateOTP())
# label=tk.Label(OTP)
# label.pack()


window.mainloop()
