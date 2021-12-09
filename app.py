from tkinter import *
import sys
sys.path.append('..')
import ai



# When button is clicked, the run_command() function from the ai module will be executed
def btn_clicked():
    ai.run_command()



# Create window
window = Tk()


# Basic window for Tkinter
window.geometry("1024x768")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 768,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)



# Display and position Alfred questions
background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    255, 390,
    image=background_img)



# Display and position Alfred logo
logo_img = PhotoImage(file = f"logo.png")
logo = canvas.create_image(
    765, 125,
    image= logo_img)



# Display and style the button, command, and cursor
img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    cursor = "man",
    relief = "flat")



# Position the button
b0.place(
    x = 570, y = 260,
    width = 400,
    height = 400)


window.resizable(False, False)
window.mainloop()