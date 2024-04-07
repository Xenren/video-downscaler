import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
from moviepy.editor import VideoFileClip

class App:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.setup_gui()

    def setup_gui(self):
        self.root.title("Video Downscaling")
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=400, mode='determinate')
        self.progress.pack(pady=20)
        tk.Button(self.root, text="Select Video", command=self.select_and_process_video).pack(pady=20)

    def update_progress(self, progress: float):
        self.progress['value'] = progress
        self.root.update_idletasks()

    def downscale_video(self, filepath: str):
        target_widths = [1920, 1280, 854]
        output_files = []
        
        confirm = messagebox.askyesno("Downscale Commence", "Start Downscale?")
        if not confirm:
            return
        for task_no, target_width in enumerate(target_widths, start=1):
            clip = VideoFileClip(filepath)
            target_height = int(target_width / clip.aspect_ratio)
            extension = filepath.split('.')[-1]
            save_path = f"{filepath.rsplit('.', 1)[0]}_{target_width}x{target_height}.{extension}"
            clip.resize(newsize=(target_width, target_height)).write_videofile(save_path, codec="libx264", audio_codec="aac", verbose=False, logger=None) # type: ignore
            clip.close()
            output_files.append(save_path)

            self.update_progress((task_no / len(target_widths)) * 100)

        self.root.after(0, messagebox.showinfo, "Success", "Videos downscaled successfully!\n\n" + "\n".join(output_files))
        self.update_progress(0)

    def select_and_process_video(self):
        filepath = filedialog.askopenfilename(title="Select a video file", filetypes=(("Video files", "*.mp4* *.avi* *.mov*"), ("All files", "*.*")))
        if not filepath:
            return

        threading.Thread(target=self.downscale_video, args=(filepath,), daemon=True).start()

def main():
    root = tk.Tk()
    App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
