import tkinter as tk

class LivePreviewApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Live Preview Example")
        self.geometry("400x300")

        # Entry for font size
        self.font_size_entry = tk.Entry(self)
        self.font_size_entry.pack(pady=5)
        self.font_size_entry.bind("<KeyRelease>", self.update_preview)

        # Entry for font color
        self.font_color_entry = tk.Entry(self)
        self.font_color_entry.pack(pady=5)
        self.font_color_entry.bind("<KeyRelease>", self.update_preview)

        # Text widget for live preview
        self.preview_text = tk.Text(self, height=5)
        self.preview_text.pack(pady=20)
        self.preview_text.insert(tk.END, "Live Preview Text")

    def update_preview(self, event):
        # Get the font size and color from the entries
        font_size = self.font_size_entry.get()
        font_color = self.font_color_entry.get()

        # Update the Text widget's font size and color
        try:
            if font_size:
                self.preview_text.config(font=("Arial", int(font_size)))
            if font_color:
                self.preview_text.config(fg=font_color)
        except ValueError:
            pass  # Ignore invalid font size

if __name__ == "__main__":
    app = LivePreviewApp()
    app.mainloop()
