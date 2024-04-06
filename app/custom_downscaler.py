import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from moviepy.editor import VideoFileClip

def downscale_video():
    filepath = filedialog.askopenfilename(title="Select a video file", filetypes=(("Video files", "*.mp4;*.avi;*.mov"), ("All files", "*.*")))
    if not filepath:
        return
    
    target_height = simpledialog.askinteger("Input", "Enter the target width (pixels):", minvalue=10, maxvalue=5000)
    if not target_height:
        return

    clip = VideoFileClip(filepath)

    target_height = int(target_height * clip.aspect_ratio)

    resized_clip = clip.resize(newsize=(target_height, target_height)) # type: ignore

    save_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=(("MP4 file", "*.mp4"), ("All files", "*.*")))
    if not save_path:
        return

    resized_clip.write_videofile(save_path, codec="libx264", audio_codec="aac")

    messagebox.showinfo("Success", "Video downscaled successfully!")

def main():
    root = tk.Tk()
    root.withdraw()
    downscale_video()

if __name__ == "__main__":
    main()
