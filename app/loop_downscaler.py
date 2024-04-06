import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip

def downscale_video():
    filepath = filedialog.askopenfilename(title="Select a video file", filetypes=(("Video files", "*.mp4;*.avi;*.mov"), ("All files", "*.*")))
    if not filepath:
        return
    
    # list of target widths for different resolutions (e.g., 1080p, 720p, 480p)
    target_widths = [1920, 1280, 854]
    output_files = []

    for target_width in target_widths:
        clip = VideoFileClip(filepath)

        target_height = int(target_width / clip.aspect_ratio)

        resized_clip = clip.resize(newsize=(target_width, target_height)) # type: ignore

        extension = filepath.split('.')[-1]
        save_path = f"{filepath.rsplit('.', 1)[0]}_{target_width}x{target_height}.{extension}"

        resized_clip.write_videofile(save_path, codec="libx264", audio_codec="aac")
        output_files.append(save_path)

    messagebox.showinfo("Success", "Videos downscaled successfully!\n\n" + "\n".join(output_files))

def main():
    root = tk.Tk()
    root.withdraw()
    downscale_video()

if __name__ == "__main__":
    main()
