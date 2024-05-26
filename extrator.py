import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube
from moviepy.editor import *

def download_media():
    url = entry.get()
    try:
        yt = YouTube(url)
        if var.get() == 1:  # Se a opção selecionada for extrair vídeo
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path=os.getcwd())
            status_label.config(text="Download de vídeo concluído!")
        elif var.get() == 2:  # Se a opção selecionada for extrair áudio
            stream = yt.streams.filter(only_audio=True).first()
            stream.download(output_path=os.getcwd())
            video_path = stream.default_filename
            mp4_file = video_path
            mp3_file = video_path.split(".mp4")[0] + ".mp3"
            video = VideoFileClip(mp4_file)
            video.audio.write_audiofile(mp3_file)
            os.remove(mp4_file)  # Remover o vídeo MP4 após extrair o áudio
            status_label.config(text="Download de áudio concluído!")
        
        # Exibir pop-up de parabéns
        messagebox.showinfo("Parabéns", "Download concluído com sucesso!")

    except Exception as e:
        messagebox.showerror("Erro", "Erro durante o download: " + str(e))
        status_label.config(text="Erro durante o download: " + str(e))

# Interface gráfica
root = tk.Tk()
root.title("YouTube Downloader")

label = tk.Label(root, text="Insira o URL do vídeo do YouTube:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

var = tk.IntVar()
video_radio = tk.Radiobutton(root, text="Extrair Vídeo", variable=var, value=1)
video_radio.pack(anchor=tk.W)

audio_radio = tk.Radiobutton(root, text="Extrair Áudio", variable=var, value=2)
audio_radio.pack(anchor=tk.W)

download_button = tk.Button(root, text="Baixar", command=download_media)
download_button.pack(pady=5)

status_label = tk.Label(root, text="")
status_label.pack(pady=5)

root.mainloop()
