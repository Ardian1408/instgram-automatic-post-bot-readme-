from tkinter import Tk, Label, Entry, Button, filedialog
from instabot import Bot
from datetime import datetime

def select_file():
    file_path = filedialog.askopenfilename(initialdir="/", title="Pilih File", filetypes=[("Image Files", "*.jpg")])
    file_entry.delete(0, 'end')
    file_entry.insert(0, file_path)

def upload_content():
    username = username_entry.get()
    password = password_entry.get()
    file_path = file_entry.get()
    caption = caption_entry.get()
    upload_date = date_entry.get()
    upload_time = time_entry.get()

    bot = Bot()
    bot.login(username=username, password=password)

    # Mengatur tanggal dan waktu unggah
    target_datetime = datetime.strptime(upload_date + ' ' + upload_time, '%Y-%m-%d %H:%M')

    # Menghitung selisih waktu hingga unggahan
    current_datetime = datetime.now()
    time_diff = (target_datetime - current_datetime).total_seconds()

    if time_diff > 0:
        # Menunggu hingga waktu yang ditentukan
        print(f"Menunggu {time_diff} detik hingga unggahan...")
        time.sleep(time_diff)

    # Mengunggah konten
    bot.upload_photo(file_path, caption=caption)

    print("Konten berhasil diunggah ke Instagram.")

# Membuat jendela GUI
window = Tk()
window.title("Uploader Instagram")
window.geometry("400x300")

# Membuat elemen-elemen UI
Label(window, text="Username:").pack()
username_entry = Entry(window)
username_entry.pack()

Label(window, text="Password:").pack()
password_entry = Entry(window, show="*")
password_entry.pack()

Label(window, text="File:").pack()
file_entry = Entry(window)
file_entry.pack()
Button(window, text="Pilih File", command=select_file).pack()

Label(window, text="Caption:").pack()
caption_entry = Entry(window)
caption_entry.pack()

Label(window, text="Tanggal (YYYY-MM-DD):").pack()
date_entry = Entry(window)
date_entry.pack()

Label(window, text="Waktu (HH:MM):").pack()
time_entry = Entry(window)
time_entry.pack()

Button(window, text="Unggah", command=upload_content).pack()

# Menjalankan loop UI
window.mainloop()
