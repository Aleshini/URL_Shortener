import tkinter as tk
from tkinter import messagebox
import pyshorteners
import validators
import pyperclip

# Function
def shorten_url():
    long_url = url_input.get().strip()  
    if validators.url(long_url):  
        try:
            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(long_url) 
            result_entry.delete(0, tk.END) 
            result_entry.insert(0, short_url)  
            copy_button.config(state=tk.NORMAL) 
        except Exception as e:
            messagebox.showerror("Error", f"Failed to shorten URL: {e}")
            copy_button.config(state=tk.DISABLED)
    else:
        messagebox.showwarning("Invalid URL", "Please enter a valid URL.")
        copy_button.config(state=tk.DISABLED)


def copy_to_clipboard():
    short_url = result_entry.get()
    pyperclip.copy(short_url)
    messagebox.showinfo("Copied", "Short URL copied to clipboard!")


root = tk.Tk()
root.title("URL Shortener")
root.geometry("400x500")
root.config(bg="#ffffff")


canvas = tk.Canvas(root, width=400, height=500, highlightthickness=0)
canvas.pack(fill="both", expand=True)

gradient_color1 = "#662D8C"
gradient_color2 = "#ED1E79"

for i in range(0, 500):
    r = int(int(gradient_color1[1:3], 16) + (int(gradient_color2[1:3], 16) - int(gradient_color1[1:3], 16)) * i / 500)
    g = int(int(gradient_color1[3:5], 16) + (int(gradient_color2[3:5], 16) - int(gradient_color1[3:5], 16)) * i / 500)
    b = int(int(gradient_color1[5:], 16) + (int(gradient_color2[5:], 16) - int(gradient_color1[5:], 16)) * i / 500)
    color = f'#{r:02x}{g:02x}{b:02x}'
    canvas.create_line(0, i, 400, i, fill=color)

canvas.create_rectangle(35, 45, 355, 465, fill="#662D8C", outline="white")
canvas.create_rectangle(45, 35, 365, 455, fill="#ED1E79", outline="white")
canvas.create_rectangle(40, 40, 360, 460, fill="white", outline="white")


title_label = tk.Label(root, text="URL Shortener", font=("Cooper Black", 24,"underline"), bg="white", fg="#2e4053")
canvas.create_window(200, 80, window=title_label)


url_label = tk.Label(root, text="Enter Long URL:", font=("Cooper Black", 12), bg="white", fg="black")
canvas.create_window(120, 160, window=url_label)

url_input = tk.Entry(root, font=("Bahnschrift", 12), width=30, relief="flat", bd=1, bg="white",fg="navy")
canvas.create_window(200, 190, window=url_input)
canvas.create_line(60, 205, 340, 205, fill="grey")



result_label = tk.Label(root, text="Shortened URL:", font=("Cooper Black", 12), bg="white", fg="black")
canvas.create_window(120, 230, window=result_label)

result_entry = tk.Entry(root, font=("Bahnschrift", 12), width=30, relief="flat", bd=1, bg="white",fg="green")
canvas.create_window(200, 260, window=result_entry)
canvas.create_line(60, 275, 340, 275, fill="grey")


copy_button = tk.Button(root, text="Copy Shortened URL", command=copy_to_clipboard, font=("Arial", 10,"underline"), bg="white",activebackground="white", fg="blue", relief="flat", state=tk.DISABLED)
canvas.create_window(272, 290, window=copy_button)

shorten_button = tk.Button(root, text="Short URL", command=shorten_url, font=("Mistral", 18), bg="#662D8C",activebackground="#ED1E79", fg="white", relief="flat",width=15,height=0)
canvas.create_window(200, 380, window=shorten_button)


root.mainloop()
