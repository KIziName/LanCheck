import socket
import threading
import customtkinter as ctk

from config import TEXTS
from about_window import AboutWindow

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class LanCheck(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.lang = "ru"
        self.github_url = "https://github.com/KIziName/LanCheck/releases"

        self.title(TEXTS[self.lang]["app_title"])
        self.geometry("500x700")
        self.resizable(False, False)

        self.is_scanning = False
        self.stop_scan = False
        self.about_window = None

        self.top_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.top_frame.pack(fill="x", padx=15, pady=(15, 0))
        self.label_title = ctk.CTkLabel(
            self.top_frame, text="🛡️ LanCheck",
            font=("Segoe UI", 22, "bold")
        )
        self.label_title.pack(side="left")

        self.desc_label = ctk.CTkLabel(
            self,
            text=TEXTS[self.lang]["description"],
            font=("Segoe UI", 12),
            wraplength=460,
            justify="center",
            text_color=("gray30", "gray70")
        )
        self.desc_label.pack(pady=(15, 10))

        self.ip_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.ip_frame.pack(pady=10)
        self.ip_label = ctk.CTkLabel(
            self.ip_frame, text="🌐 127.0.0.1 (localhost)",
            font=("Segoe UI", 14, "bold"), text_color=("gray40", "gray60")
        )
        self.ip_label.pack()

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=10)

        self.btn_start = ctk.CTkButton(
            self.button_frame,
            text=TEXTS[self.lang]["start_btn"],
            command=self.start_scan_thread,
            font=("Segoe UI", 14, "bold"),
            width=150
        )
        self.btn_start.pack(side="left", padx=5)

        self.btn_stop = ctk.CTkButton(
            self.button_frame,
            text=TEXTS[self.lang]["stop_btn"],
            command=self.stop_scanning,
            font=("Segoe UI", 14),
            width=100,
            state="disabled",
            fg_color="gray"
        )
        self.btn_stop.pack(side="left", padx=5)

        self.progress = ctk.CTkProgressBar(self, width=440)
        self.progress.set(0)

        self.result_text = ctk.CTkTextbox(self, width=440, height=280, font=("Segoe UI", 13))
        self.result_text.pack(pady=15)
        self.result_text.configure(state="disabled")

        self.bottom_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.bottom_frame.pack(fill="x", padx=15, pady=(0, 10))

        self.btn_about = ctk.CTkButton(
            self.bottom_frame, text=TEXTS[self.lang]["about_btn"], width=100, height=30,
            font=("Segoe UI", 12), command=self.open_about_window
        )
        self.btn_about.pack(side="left", padx=5)

        self.lang_label = ctk.CTkLabel(self.bottom_frame, text=TEXTS[self.lang]["lang_label"], font=("Segoe UI", 12))
        self.lang_label.pack(side="right", padx=5)

        self.lang_switch = ctk.CTkComboBox(
            self.bottom_frame, width=70, height=30,
            values=[TEXTS[self.lang]["lang_ru"], TEXTS[self.lang]["lang_en"]],
            command=self.change_language,
            font=("Segoe UI", 12)
        )
        self.lang_switch.pack(side="right")
        self.lang_switch.set(TEXTS[self.lang]["lang_ru"])

    def get_text(self, key, *args):
        text = TEXTS[self.lang].get(key, key)
        if args:
            text = text.format(*args)
        return text

    def update_ui_texts(self):
        self.title(TEXTS[self.lang]["app_title"])
        self.btn_about.configure(text=TEXTS[self.lang]["about_btn"])
        self.btn_start.configure(text=TEXTS[self.lang]["start_btn"])
        self.btn_stop.configure(text=TEXTS[self.lang]["stop_btn"])
        self.desc_label.configure(text=TEXTS[self.lang]["description"])
        self.lang_label.configure(text=TEXTS[self.lang]["lang_label"])
        self.lang_switch.configure(values=[TEXTS[self.lang]["lang_ru"], TEXTS[self.lang]["lang_en"]])
        self.lang_switch.set(TEXTS[self.lang]["lang_ru" if self.lang == "ru" else "lang_en"])

        if not self.is_scanning:
            self.result_text.configure(state="normal")
            self.result_text.delete("1.0", "end")
            self.result_text.configure(state="disabled")

        if self.about_window and self.about_window.winfo_exists():
            self.about_window.update_language(self.lang)
        else:
            self.about_window = None

    def open_about_window(self):
        if self.about_window is None or not self.about_window.winfo_exists():
            self.about_window = AboutWindow(self, self.lang, self.github_url)
        else:
            self.about_window.focus()
            self.about_window.center_on_parent()

    def log_message(self, message):
        self.result_text.configure(state="normal")
        self.result_text.insert("end", message + "\n")
        self.result_text.see("end")
        self.result_text.configure(state="disabled")

    def update_progress(self, value):
        self.progress.set(value)

    def show_progress_bar(self):
        if not self.progress.winfo_ismapped():
            self.progress.pack(pady=5, before=self.result_text)

    def hide_progress_bar(self):
        if self.progress.winfo_ismapped():
            self.progress.pack_forget()

    def clear_result_text(self):
        self.result_text.configure(state="normal")
        self.result_text.delete("1.0", "end")
        self.result_text.configure(state="disabled")

    def set_controls_state(self, scanning):
        if scanning:
            self.btn_start.configure(state="disabled", text=self.get_text("start_btn_scanning"))
            self.btn_stop.configure(state="normal", fg_color=("#c42b1c", "#e05a4a"))
            self.lang_switch.configure(state="disabled")
        else:
            self.btn_start.configure(state="normal", text=self.get_text("start_btn"))
            self.btn_stop.configure(state="disabled", fg_color="gray")
            self.lang_switch.configure(state="normal")

    def stop_scanning(self):
        if self.is_scanning:
            self.stop_scan = True
            self.log_message(self.get_text("stopping"))

    def change_language(self, choice):
        if self.is_scanning:
            current = TEXTS[self.lang]["lang_ru"] if self.lang == "ru" else TEXTS[self.lang]["lang_en"]
            self.lang_switch.set(current)
            return
        new_lang = "ru" if choice == TEXTS["ru"]["lang_ru"] else "en"
        if new_lang == self.lang:
            return
        self.lang = new_lang
        self.update_ui_texts()

    def start_scan_thread(self):
        if self.is_scanning:
            return
        self.is_scanning = True
        self.stop_scan = False

        self.after(0, self.set_controls_state, True)
        self.after(0, self.update_progress, 0)
        self.after(0, self.show_progress_bar)
        self.after(0, self.clear_result_text)

        threading.Thread(target=self.scan_ports, daemon=True).start()

    def scan_ports(self):
        target_ip = "127.0.0.1"
        ports = [21, 22, 23, 25, 80, 135, 139, 443, 445, 3389, 8080]
        total_ports = len(ports)

        self.after(0, self.log_message, self.get_text("scan_start"))
        suspicious_ports = 0

        for index, port in enumerate(ports):
            if self.stop_scan:
                self.after(0, self.log_message, self.get_text("scan_stopped"))
                break

            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.4)
                    result = s.connect_ex((target_ip, port))

                    if result == 0:
                        if port in [135, 445]:
                            self.after(0, self.log_message, self.get_text("port_open_system", port))
                        else:
                            self.after(0, self.log_message, self.get_text("port_open_suspicious", port))
                            suspicious_ports += 1
                    else:
                        self.after(0, self.log_message, self.get_text("port_closed", port))
            except socket.error as e:
                self.after(0, self.log_message, self.get_text("port_error", port, str(e)))
            except Exception:
                self.after(0, self.log_message, self.get_text("port_error", port, "unknown error"))

            self.after(0, self.update_progress, (index + 1) / total_ports)

        if not self.stop_scan:
            self.after(0, self.log_message, self.get_text("result_title"))
            if suspicious_ports == 0:
                self.after(0, self.log_message, self.get_text("result_safe"))
                self.after(0, self.log_message, self.get_text("result_safe_note"))
            else:
                self.after(0, self.log_message, self.get_text("result_vulnerable", suspicious_ports))

        self.after(0, self.finish_ui)

    def finish_ui(self):
        self.hide_progress_bar()
        self.set_controls_state(False)
        self.is_scanning = False
        self.stop_scan = False


if __name__ == "__main__":
    app = LanCheck()
    app.mainloop()
