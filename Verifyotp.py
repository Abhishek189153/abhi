import tkinter as tk
from random import randint
import time

class OTPGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("OTP Generator and Verifier")
        self.otp = None
        self.expiry_time = None

        # Create GUI elements
        self.label = tk.Label(self.root, text="OTP Generator and Verifier")
        self.label.pack()

        self.generate_button = tk.Button(self.root, text="Generate OTP", command=self.generate_otp)
        self.generate_button.pack()

        self.otp_label = tk.Label(self.root, text="OTP: ")
        self.otp_label.pack()

        self.verify_label = tk.Label(self.root, text="Enter OTP: ")
        self.verify_label.pack()

        self.verify_entry = tk.Entry(self.root)
        self.verify_entry.pack()

        self.verify_button = tk.Button(self.root, text="Verify OTP", command=self.verify_otp)
        self.verify_button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def generate_otp(self):
        self.otp = str(randint(1000, 9999))
        self.expiry_time = time.time() + 60  # OTP expires in 1 minute
        self.otp_label['text'] = f"OTP: {self.otp}"
        self.result_label['text'] = "OTP generated successfully!"

    def verify_otp(self):
        user_otp = self.verify_entry.get()
        if time.time() < self.expiry_time and user_otp == self.otp:
            self.result_label['text'] = "OTP verified successfully!"
        else:
            self.result_label['text'] = "Invalid or expired OTP!"

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    otp_generator = OTPGenerator()
    otp_generator.run()