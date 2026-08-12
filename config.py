TEXTS = {
    "ru": {
        "app_title": "LanCheck V1.0",
        "about_btn": "О программе",
        "start_btn": "Запустить проверку",
        "stop_btn": "Остановить",
        "start_btn_scanning": "Сканирование...",
        "lang_label": "Язык:",
        "lang_en": "EN",
        "lang_ru": "RU",
        "description": "Сканирует компьютер на наличие открытых сетевых портов и предупреждает о потенциальных уязвимостях.",
        "about_title": "О программе",
        "about_author": "Автор: KiziName",
        "about_version": "Версия: V1.0",
        "about_desc": "Простой инструмент для сканирования открытых портов и выявления потенциальных уязвимостей в локальной сети.",
        "about_github_text": "GitHub: KIziName/LanCheck",
        "about_close": "Закрыть",
        "scan_start": "=== Проверка системы (127.0.0.1) ===",
        "port_open_system": "🟢 Порт {}: Открыт (Системная служба Windows)",
        "port_open_suspicious": "⚠️ Порт {}: ОТКРЫТ! Возможная уязвимость",
        "port_closed": "⚪ Порт {}: Закрыт",
        "port_error": "❌ Порт {}: Ошибка проверки - {}",
        "result_title": "\n=== Итог проверки ===",
        "result_safe": "✅ Всё в порядке. Компьютер защищен.",
        "result_safe_note": "Открытые порты 135/445 нужны для работы Windows. Из интернета они заблокированы вашим роутером.",
        "result_vulnerable": "🔍 Внимание! Найдено подозрительных портов: {}",
        "scan_stopped": "⚠️ Сканирование прервано пользователем.",
        "stopping": "Остановка...",
    },
    "en": {
        "app_title": "LanCheck V1.0",
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

# ==================== НАСТРОЙКИ ПРИЛОЖЕНИЯ ====================

SETTINGS = {
    # --- Сетевое сканирование ---
    "target_ip": "127.0.0.1",
    "ports": [21, 22, 23, 25, 80, 135, 139, 443, 445, 3389, 8080],
    "system_ports": [135, 445],          # порты, считающиеся безопасными
    "timeout": 0.4,                      # таймаут подключения (сек)

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