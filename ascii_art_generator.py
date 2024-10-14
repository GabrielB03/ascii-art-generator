import tkinter as tk
import pyfiglet
import re

# Function to generate ASCII art without ANSI color codes
def generate_ascii_art():
    text = entry.get()
    font = font_var.get()
    selected_font = pyfiglet.Figlet(font=font)

    ascii_text = selected_font.renderText(text)

    # Remove ANSI color codes [30m and [0m using regex
    cleaned_ascii_text = re.sub(r'\[\d+m', '', ascii_text)

    output_text.config(text=cleaned_ascii_text, fg="black")  # Display text without ANSI color codes

# GUI setup
root = tk.Tk()
root.title("ASCII Art Generator")

# Text entry
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Font options
font_var = tk.StringVar()
font_var.set("standard")
font_dropdown = tk.OptionMenu(root, font_var, *pyfiglet.FigletFont.getFonts())
font_dropdown.pack(pady=5)

# Button to generate ASCII art
generate_button = tk.Button(root, text="Generate ASCII Art", command=generate_ascii_art)
generate_button.pack(pady=10)

# Output for ASCII art
output_text = tk.Label(root, text="", font=("Courier", 8))
output_text.pack(pady=10)

root.mainloop()