import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from moviepy.editor import VideoFileClip

def downscale_video():
    # Ask the user to select a video file
    filepath = filedialog.askopenfilename(title="Select a video file", filetypes=(("Video files", "*.mp4;*.avi;*.mov"), ("All files", "*.*")))
    if not filepath:
        return
    
    # Ask for the target width
    target_width = simpledialog.askinteger("Input", "Enter the target width (pixels):", minvalue=10, maxvalue=5000)
    if not target_width:
        return

    # Load the video file
    clip = VideoFileClip(filepath)

    # Calculate the new height to maintain aspect ratio
    target_height = int(target_width / clip.aspect_ratio)

    # Resize the video
    resized_clip = clip.resize(newsize=(target_width, target_height)) # type: ignore

    # Save the downscaled video
    save_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=(("MP4 file", "*.mp4"), ("All files", "*.*")))
    if not save_path:
        return

    resized_clip.write_videofile(save_path, codec="libx264", audio_codec="aac")

    # Show a completion message
    messagebox.showinfo("Success", "Video downscaled successfully!")

def main():
    root = tk.Tk()
    root.withdraw()  # we don't want a full GUI, so keep the root window from appearing
    downscale_video()

if __name__ == "__main__":
    main()
