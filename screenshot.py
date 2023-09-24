import tkinter as tk
import pyautogui
from PIL import Image, ImageTk
from tkinter import filedialog

# main window
root = tk.Tk()
root.title("Screenshot Tool")

# track if the screenshot has been captured
screenshot_taken = False

# capture a screenshot
def capture_screenshot():
    global screenshot_taken
    if not screenshot_taken:
        try:
            # Minimize the main window
            root.iconify()
            screenshot = pyautogui.screenshot()
            
            # save location
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
            
            if file_path:
                screenshot.save(file_path)
                display_screenshot(file_path)
                screenshot_taken = True
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Restore the main window
            root.deiconify()

#display the screenshot
def display_screenshot(file_path):
    screenshot_image = Image.open(file_path)
    screenshot_photo = ImageTk.PhotoImage(screenshot_image)
    screenshot_label.config(image=screenshot_photo)
    screenshot_label.image = screenshot_photo

# buttons with colors
capture_button = tk.Button(root, text="Capture Screenshot", command=capture_screenshot, bg="lightblue", padx=10, pady=5)
quit_button = tk.Button(root, text="Quit", command=root.quit, bg="salmon", padx=10, pady=5)

# displaying the screenshot
screenshot_label = tk.Label(root)

# title label
title_label = tk.Label(root, text="Take Screenshot", font=("Arial", 14))

# Place widgets in the window
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 5))  # Reduced pady for title
screenshot_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
capture_button.grid(row=2, column=0, padx=10, pady=(5, 10))  # Reduced pady for button
quit_button.grid(row=2, column=1, padx=10, pady=(5, 10))  # Reduced pady for button

# Start main loop
root.mainloop()
