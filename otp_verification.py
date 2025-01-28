import twilio.rest
import random
from tkinter import messagebox
import tkinter as tk

# Creating Window
root = tk.Tk()
root.title("OTP Verification")
root.geometry("600x550")

# Twilio account details
account_sid = "your_account_sid_here"
auth_token = "your_auth_token_here"


# Function to send OTP
def sendOTP():
    global n
    n = random.randint(1000, 9999)
    client = twilio.rest.Client(account_sid, auth_token)
    client.messages.create(to=["your_phone_number"], from_="your_twilio_phone_number", body=str(n))


# Resend OTP
def resendOTP():
    sendOTP()


# Checking the OTP
def checkOTP():
    global n
    try:
        user_input = int(user.get())
        if user_input == n:
            messagebox.showinfo("showinfo", "Login Success")
            n = "done"
        elif n == "done":
            messagebox.showinfo("showinfo", "Already entered")
        else:
            messagebox.showinfo("showinfo", "Wrong OTP")
    except:
        messagebox.showinfo("showinfo", "Invalid OTP")


# Drawing the canvas
c = tk.Canvas(root, bg="white", width=400, height=300)
c.place(x=100, y=60)

# Label widget
login = tk.Label(root, text="OTP Verification", font="bold,20", bg="white")
login.place(x=210, y=90)

# Entry widget for OTP input
user = tk.Entry(root, borderwidth=2, width=29, font=("Arial", 14))
user.place(x=190, y=160)

# Sending the OTP initially
sendOTP()

# Submit button
submit_button = tk.Button(root, text="Submit", command=checkOTP, font=('bold', 15))
submit_button.place(x=258, y=250)

# Resend Button
resend_button = tk.Button(root, text="Resend OTP", command=resendOTP, font=("bold", 15))
resend_button.place(x=240, y=400)

# Event Loop
root.mainloop()
