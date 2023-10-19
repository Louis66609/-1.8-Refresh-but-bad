import customtkinter as ctk
import tkinter
from PIL import ImageTk, Image
import re

def create_window(title):
    ctk.set_default_color_theme("green")
    window = ctk.CTk()
    window.geometry("1400x800")
    ctk.set_appearance_mode("light")
    window.resizable(width=False, height=False)
    center_window(window)
    frame = create_frame(window)
    window.wm_title(title)
    return window, frame 

def center_window(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = 1400
    window_height = 800
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

def create_frame(window):
    frame = ctk.CTkFrame(master=window, width=750, height=600)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    return frame

def login_refresh(login_window):
    login_window.destroy()
    login_page()

def admin_refresh(login_window):
    admin_registration_page(login_window)

def employee_refresh(login_window):
    employee_registration_page(login_window)

def login_page():
    Login_page_window, frame = create_window("Login Page")
    
    LogPg_refresh_button = ctk.CTkButton(master=frame, width=100, corner_radius=20, text="Refresh Page", font=('Roboto', 15))
    LogPg_refresh_button.place(x=5, y=5)
    LogPg_refresh_button.configure(command=lambda:login_refresh(Login_page_window))

    LogPg_emp_reg_button = ctk.CTkButton(master=frame, width=115, text="Employee", corner_radius=20, font=('Roboto', 15))
    LogPg_emp_reg_button.configure(command=lambda: employee_registration_page(Login_page_window))
    LogPg_emp_reg_button.place(x=610, y=565)
    
    LogPg_ad_reg_button = ctk.CTkButton(master=frame, width=115, text="Admin", corner_radius=20, font=('Roboto', 15))
    LogPg_ad_reg_button.configure(command=lambda: admin_registration_page(Login_page_window))
    LogPg_ad_reg_button.place(x=400, y=565)

    Login_page_window.mainloop()
    return Login_page_window

def admin_registration_page(login_window):
    login_window.destroy()
    Admin_registration_window, admin_frame = create_window("Admin Registration")
    
    AdPg_refresh_button = ctk.CTkButton(master=admin_frame, width=100, text="Refresh Page", font=('Roboto', 15), corner_radius=20)
    AdPg_refresh_button.place(x=5, y=5)
    AdPg_refresh_button.configure(command=lambda: admin_refresh(Admin_registration_window))
    
    AdPg_return_button = ctk.CTkButton(master=admin_frame, width=100, corner_radius=20, text="Return", font=('Roboto', 15))
    AdPg_return_button.configure(command=lambda: return_to_login(Admin_registration_window))
    AdPg_return_button.place(x=645, y=5)
    
    Admin_registration_window.mainloop()
    return Admin_registration_window

def employee_registration_page(login_window):
    login_window.destroy()
    Employee_registration_window, employee_frame = create_window("Employee Registration")

    EmpReg_refresh_button = ctk.CTkButton(master=employee_frame, width=100, text="Refresh Page", font=('Roboto', 15), corner_radius=20)
    EmpReg_refresh_button.place(x=5, y=5)
    EmpReg_refresh_button.configure(command=lambda: employee_refresh(Employee_registration_window))
    
    EmpReg_return_button = ctk.CTkButton(master=employee_frame, width=100, corner_radius=20, text="Return", font=('Roboto', 15))
    EmpReg_return_button.configure(command=lambda: return_to_login(Employee_registration_window))
    EmpReg_return_button.place(x=645, y=5)
    
    Employee_registration_window.mainloop()
    return Employee_registration_window

def return_to_login(login_window):
    login_window.destroy()
    login_page()


if __name__ == "__main__":
    login_page()
