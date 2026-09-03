TEXTS = {
    "en": {
        "app_title": "LanCheck",
        "about_btn": "About",
        "start_btn": "Start Scan",
        "stop_btn": "Stop",
        "start_btn_scanning": "Scanning...",
        "lang_label": "Language:",
        "lang_en": "EN",
        "lang_ru": "RU",
        "description": "Scans your computer for open network ports and warns about potential vulnerabilities.",
        "about_title": "About",
        "about_author": "Author: KiziName",
        "about_version": "Version: V1.0",
        "about_desc": "A simple tool for scanning open ports and identifying potential vulnerabilities in your local network.",
        "about_github_text": "GitHub: KIziName/LanCheck",
        "about_close": "Close",
        "scan_start": "=== System check (127.0.0.1) ===",
        "port_open_system": "🟢 Port {}: Open (Windows system service)",
        "port_open_suspicious": "⚠️ Port {}: OPEN! Possible vulnerability",
        "port_closed": "⚪ Port {}: Closed",
        "port_error": "❌ Port {}: Check error - {}",
        "result_title": "\n=== Scan result ===",
        "result_safe": "✅ Everything is fine. Your computer is protected.",
        "result_safe_note": "Open ports 135/445 are needed for Windows to work. They are blocked from the internet by your router.",
        "result_vulnerable": "🔍 Attention! Suspicious ports found: {}",
        "scan_stopped": "⚠️ Scan stopped by user.",
        "stopping": "Stopping...",
    }
}

SETTINGS = {
    # --- Сетевое сканирование ---
    "target_ip": "127.0.0.1",
    "ports": [21, 22, 23, 25, 80, 135, 139, 443, 445, 3389, 8080],
    "system_ports": [135, 445],          # порты, считающиеся безопасными
    "timeout": 0.4,                      # таймаут подключения 

    # --- Окна ---
    "main_window_size": "500x700",
    "github_url": "https://github.com/KIziName/LanCheck/releases",

    # --- Шрифты (общие) ---
    "font_family": "Segoe UI",
    "font_title_size": 18,
    "font_normal_size": 13,
    "font_button_size": 14,

    # --- Главное окно ---
    "progress_width": 440,
    "textbox_width": 440,
    "textbox_height": 280,

    # --- Окно "О программе" ---
    "about": {
        "window_size": "420x340",
        "card_corner_radius": 12,
        "card_padx": 20,
        "card_pady": 20,
        "title_pady": (20, 10),
        "author_pady": 2,
        "version_pady": 2,
        "desc_pady": 15,
        "desc_padx": 20,
        "desc_wraplength": 340,
        "link_pady": 5,
        "close_button_width": 120,
        "close_button_height": 32,
        "close_button_pady": (10, 20),
        "card_fg_color": ("white", "#212121"),
        "title_text_color": ("#1f538d", "#3b8ed0"),
        "link_text_color": ("#1f538d", "#1abc9c"),
    }
}
