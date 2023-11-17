import tkinter as tk
import subprocess

# Function to execute different Python scripts
def execute_script(script_path):
    subprocess.Popen(['python', script_path])

# Function to handle button clicks
def button_click(script):
    execute_script(script)

# Create the main window
root = tk.Tk()
root.title("Button Launcher")
root.geometry("400x300")
root.configure(bg="blue")

# List of script paths
scripts = [
    "script1.py",
    "script2.py",
    "script3.py",
    # Add paths for other scripts here
]

# Create and place buttons
for i in range(9):
    if i < len(scripts):
        button = tk.Button(root, text=f"Script {i+1}", command=lambda idx=i: button_click(scripts[idx]))
        button.pack(pady=10)

# Run the main loop
root.mainloop()
  
