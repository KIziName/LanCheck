import customtkinter as ctk
import webbrowser
from config import TEXTS

class AboutWindow(ctk.CTkToplevel):
    def __init__(self, parent, lang, github_url):
        super().__init__(parent)
        self.lang = lang
        self.github_url = github_url
        self.build_ui()
        self.title(TEXTS[self.lang]["about_title"])
        self.geometry("420x340")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()
        self.center_on_parent()

    def center_on_parent(self):
        """Центрирует окно относительно родительского."""
        self.update_idletasks()
        parent = self.master
        parent_x = parent.winfo_x()
        parent_y = parent.winfo_y()
        parent_w = parent.winfo_width()
        parent_h = parent.winfo_height()
        w = self.winfo_width()
        h = self.winfo_height()
        x = parent_x + (parent_w // 2) - (w // 2)
        y = parent_y + (parent_h // 2) - (h // 2)
        self.geometry(f"+{x}+{y}")

    def build_ui(self):
        t = TEXTS[self.lang]
        font_title = ("Segoe UI", 18, "bold")
        font_normal = ("Segoe UI", 13)
        font_link = ("Segoe UI", 13, "underline")

        self.card = ctk.CTkFrame(self, fg_color=("white", "#212121"), corner_radius=12)
        self.card.pack(expand=True, fill="both", padx=20, pady=20)

        self.card.grid_columnconfigure(0, weight=1)
        self.card.grid_columnconfigure(2, weight=1)
        self.card.grid_rowconfigure(0, weight=1)
        self.card.grid_rowconfigure(6, weight=1)

        self.lbl_title = ctk.CTkLabel(
            self.card, text="LANCHECK",
            font=font_title, text_color=("#1f538d", "#3b8ed0")
        )
        self.lbl_title.grid(row=1, column=1, pady=(20, 10))

        self.lbl_author = ctk.CTkLabel(self.card, text=t["about_author"], font=font_normal)
        self.lbl_author.grid(row=2, column=1, pady=2)

        self.lbl_version = ctk.CTkLabel(
            self.card, text=t["about_version"],
            font=font_normal, text_color="gray"
        )
        self.lbl_version.grid(row=3, column=1, pady=2)

        self.lbl_desc = ctk.CTkLabel(
            self.card, text=t["about_desc"],
            font=font_normal, wraplength=340, justify="center"
        )
        self.lbl_desc.grid(row=4, column=1, pady=15, padx=20)

        self.lbl_link = ctk.CTkLabel(
            self.card, text=t["about_github_text"],
            font=font_link, text_color=("#1f538d", "#1abc9c"), cursor="hand2"
        )
        self.lbl_link.grid(row=5, column=1, pady=5)
        self.lbl_link.bind("<Button-1>", lambda e: webbrowser.open(self.github_url))

        self.close_button = ctk.CTkButton(
            self.card, text=t["about_close"], height=32, width=120,
            font=font_normal, corner_radius=8, command=self.destroy
        )
        self.close_button.grid(row=6, column=1, pady=(10, 20))

    def update_language(self, new_lang):
        if new_lang == self.lang:
            return
        self.lang = new_lang
        self.card.destroy()
        self.build_ui()
        self.title(TEXTS[self.lang]["about_title"])
