import customtkinter as ctk
import webbrowser

from config import TEXTS, SETTINGS


class AboutWindow(ctk.CTkToplevel):
    def __init__(self, parent, lang, github_url):
        super().__init__(parent)
        self.lang = lang
        self.github_url = github_url
        self.build_ui()
        self.title(TEXTS[self.lang]["about_title"])
        about_cfg = SETTINGS["about"]
        self.geometry(about_cfg["window_size"])
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()
        self.center_on_parent()

    def center_on_parent(self):
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
        about_cfg = SETTINGS["about"]

        font_title = (SETTINGS["font_family"], SETTINGS["font_title_size"], "bold")
        font_normal = (SETTINGS["font_family"], SETTINGS["font_normal_size"])
        font_link = (SETTINGS["font_family"], SETTINGS["font_normal_size"], "underline")

        self.card = ctk.CTkFrame(
            self,
            fg_color=about_cfg["card_fg_color"],
            corner_radius=about_cfg["card_corner_radius"]
        )
        self.card.pack(
            expand=True,
            fill="both",
            padx=about_cfg["card_padx"],
            pady=about_cfg["card_pady"]
        )

        self.card.grid_columnconfigure(0, weight=1)
        self.card.grid_columnconfigure(2, weight=1)
        self.card.grid_rowconfigure(0, weight=1)
        self.card.grid_rowconfigure(6, weight=1)

        self.lbl_title = ctk.CTkLabel(
            self.card,
            text="LANCHECK",
            font=font_title,
            text_color=about_cfg["title_text_color"]
        )
        self.lbl_title.grid(row=1, column=1, pady=about_cfg["title_pady"])

        self.lbl_author = ctk.CTkLabel(
            self.card,
            text=t["about_author"],
            font=font_normal
        )
        self.lbl_author.grid(row=2, column=1, pady=about_cfg["author_pady"])

        self.lbl_version = ctk.CTkLabel(
            self.card,
            text=t["about_version"],
            font=font_normal,
            text_color="gray"
        )
        self.lbl_version.grid(row=3, column=1, pady=about_cfg["version_pady"])

        self.lbl_desc = ctk.CTkLabel(
            self.card,
            text=t["about_desc"],
            font=font_normal,
            wraplength=about_cfg["desc_wraplength"],
            justify="center"
        )
        self.lbl_desc.grid(
            row=4, column=1,
            pady=about_cfg["desc_pady"],
            padx=about_cfg["desc_padx"]
        )

        self.lbl_link = ctk.CTkLabel(
            self.card,
            text=t["about_github_text"],
            font=font_link,
            text_color=about_cfg["link_text_color"],
            cursor="hand2"
        )
        self.lbl_link.grid(row=5, column=1, pady=about_cfg["link_pady"])
        self.lbl_link.bind("<Button-1>", lambda e: webbrowser.open(self.github_url))

        self.close_button = ctk.CTkButton(
            self.card,
            text=t["about_close"],
            height=about_cfg["close_button_height"],
            width=about_cfg["close_button_width"],
            font=font_normal,
            corner_radius=8,
            command=self.destroy
        )
        self.close_button.grid(row=6, column=1, pady=about_cfg["close_button_pady"])

    def update_language(self, new_lang):
        if new_lang == self.lang:
            return
        self.lang = new_lang
        self.card.destroy()
        self.build_ui()
        self.title(TEXTS[self.lang]["about_title"])