from gtts import gTTS
import os
import glob
import tkinter.filedialog
import tkinter as tk
import tkinter.ttk as ttk
import configparser

def generate(file_path, target_path, lang):
  if file_path == "":
    tk.messagebox.showerror("Error", "Please choose file")
    return
  if os.path.exists(file_path) == False:
    tk.messagebox.showerror("Error", "File does not exist")
    return
  if target_path == "":
    tk.messagebox.showerror("Error", "Please choose target folder")
    return
  if os.path.exists(target_path) == False:
    tk.messagebox.showerror("Error", "Target folder does not exist")
    return
  
  config = configparser.ConfigParser()
  config.read('config.ini')
  config['DEFAULT']['target_path'] = target_path
  config['DEFAULT']['lang'] = lang
  with open('config.ini', 'w') as configfile:
    config.write(configfile)
  
  name = os.path.splitext(os.path.basename(file_path))[0]
  # files = glob.glob(f'{name}_*.mp3')
  files = glob.glob(f'{target_path}/{name}_*.mp3')
  for f in files:
    os.remove(f)
  with open(file_path, 'r', encoding="utf-8") as f:
    text = f.read()
    text = text.split('\n')
    text = list(filter(None, text))
    text = [x.strip() for x in text]

    for i in range(len(text)):
      tts = gTTS(text=text[i], lang=lang or "en", slow=False)
      tts.save(f"{target_path}/{name}_{i}.mp3")
      print(f"Convert {name}_{i} success!")
  tk.messagebox.showinfo("Success", "Convert success")


config = configparser.ConfigParser()
config.read('config.ini')
target_path = config["DEFAULT"] and config['DEFAULT']['target_path'] or ""
lang = config["DEFAULT"] and config['DEFAULT']['lang'] or "en"

file_path = ""

window = tk.Tk()
window.title("Text to Speech")
window.resizable(False, False)

label = tk.Label(window, text="What file do you want to convert?")
label.grid(column=0, row=0, padx=10, pady=10)
label.config(font=("Arial", 12))

# browse file
def browse_file(initialdir: str):
  file = tk.filedialog.askopenfilename(initialdir = initialdir or "/",title = "Select file")
  label.configure(text=file)
  global file_path
  file_path = file

button_browse = tk.Button(window, text="Select File", command=lambda :browse_file(target_path))
button_browse.grid(column=1, row=0, padx=10, pady=10)

label2 = tk.Label(window, text="Where do you want to save?")
label2.grid(column=0, row=1, padx=10, pady=10)
label2.config(font=("Arial", 12))

def browse_target(initialdir: str):
  target = tk.filedialog.askdirectory(initialdir = initialdir or "/",title = "Select target folder")
  label2.configure(text=target)
  global target_path
  target_path = target

button_browse2 = tk.Button(window, text="Select Target Folder", command=lambda :browse_target(target_path))
button_browse2.grid(column=1, row=1, padx=10, pady=10)

langSelect = ttk.Combobox(window, values=["en", "th"])
langSelect.grid(column=0, row=2)
langSelect.set(lang)

button = tk.Button(window, text="Convert")
button.grid(column=0, row=3, padx=10, pady=10)
button.config(width=20, height=2, font=("Arial", 12))
button.config(command=lambda: generate(file_path, target_path, langSelect.get()))

window.mainloop()