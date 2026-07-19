import sys
import os
import ctypes
import atexit

def init_system_wide_mutex():
    kernel32 = ctypes.windll.kernel32
    clean_name = os.path.basename(sys.argv[0]).replace('.', '_').replace(' ', '_')
    mutex_name = f"Global\\AutoGuard_{clean_name}_Mutex"
    mutex_handle = kernel32.CreateMutexW(None, False, mutex_name)
    
    if kernel32.GetLastError() == 183:
        if mutex_handle:
            kernel32.CloseHandle(mutex_handle)
            
        try:
            is_russian = ctypes.windll.kernel32.GetUserDefaultUILanguage() == 1049
        except Exception:
            is_russian = True
            
        if is_russian:
            msg = "Приложение уже запущено!\nРазрешена только одна активная копия."
            title = "Защита от повторного запуска"
        else:
            msg = "The application is already running!\nOnly one active instance is allowed."
            title = "Already Running"
            
        ctypes.windll.user32.MessageBoxW(0, msg, title, 0x10 | 0x00)
        sys.exit(0)
        
    atexit.register(lambda: kernel32.CloseHandle(mutex_handle) if mutex_handle else None)


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
