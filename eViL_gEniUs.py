import threading
import time
import random
import ctypes
import os
import keyboard
import pyautogui
import tkinter as tk
from tkinter import ttk
import winsound

# --- Global Settings ---
# Shared event to signal all threads to stop
stop_event = threading.Event()
pyautogui.FAILSAFE = True

# --- Core Functions ---
def esc_listener():
    """Waits for the ESC key and sets the stop_event."""
    keyboard.wait("esc")
    print("\n[+] ESC pressed. Banishing the evil genius...")
    stop_event.set()

# --- Prank 1: Desktop Screenshot Wallpaper ---
def desktop_screenshot_wallpaper():
    """Takes a screenshot and sets it as the wallpaper."""
    try:
        # 1. Take a screenshot
        screenshot_path = os.path.join(os.environ["TEMP"], "desktop_screenshot.png")
        pyautogui.screenshot(screenshot_path)

        # 2. Set as wallpaper
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, screenshot_path, 3)
        print("[+] Desktop screenshot wallpaper prank activated.")
    except Exception as e:
        print(f"[-] Failed to run desktop screenshot prank: {e}")

# --- Prank 2: Fake File Deletion ---
def fake_file_deletion():
    """Displays a fake 'Deleting System32' progress bar."""
    def run_gui():
        root = tk.Tk()
        root.title("System Critical Task")
        root.geometry("400x120")
        root.attributes("-topmost", True)

        label = tk.Label(root, text="Deleting C:\\Windows\\System32...", pady=10)
        label.pack()

        progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        progress.pack(pady=10)

        percent_label = tk.Label(root, text="0%")
        percent_label.pack()

        def update_progress():
            for i in range(101):
                if stop_event.is_set():
                    break
                progress['value'] = i
                percent_label['text'] = f"{i}%"
                root.update_idletasks()
                time.sleep(random.uniform(0.05, 0.15))

            if not stop_event.is_set():
                label['text'] = "Deletion Complete. Your system is now compromised."
                time.sleep(3)

            try:
                root.destroy()
            except tk.TclError:
                pass

        # Ensure GUI closes when stop_event is set
        def check_stop():
            if stop_event.is_set():
                try:
                    root.destroy()
                except tk.TclError:
                    pass
            else:
                root.after(100, check_stop)

        root.after(100, check_stop)
        threading.Thread(target=update_progress, daemon=True).start()
        root.mainloop()

    if not stop_event.is_set():
        print("[+] Fake file deletion prank activated.")
        gui_thread = threading.Thread(target=run_gui, daemon=True)
        gui_thread.start()

# --- Prank 3: Screen Color Flash ---
def screen_color_flash():
    """Flashes the screen with unsettling colors."""
    def create_flash_window(color):
        try:
            window = tk.Tk()
            window.attributes("-fullscreen", True)
            window.attributes("-topmost", True)
            window.configure(bg=color)
            window.lift()
            window.after(150, window.destroy)
            window.mainloop()
        except Exception:
            pass

    colors = ["red", "black", "purple", "darkgreen"]
    while not stop_event.is_set():
        time.sleep(random.randint(10, 25))
        if stop_event.is_set():
            break
        print(f"[+] Flashing screen.")
        flash_thread = threading.Thread(target=create_flash_window, args=(random.choice(colors),), daemon=True)
        flash_thread.start()

# --- Prank 4: Audio Chaos ---
def audio_chaos():
    """Generates random, unsettling beeps."""
    while not stop_event.is_set():
        time.sleep(random.uniform(3, 8))
        if stop_event.is_set():
            break
        print("[+] Audio chaos prank activated.")
        for _ in range(random.randint(4, 12)):
            if stop_event.is_set():
                break
            try:
                winsound.Beep(random.randint(200, 1500), random.randint(70, 250))
            except Exception:
                pass # Can fail on some systems

# --- Prank 5: Ghost Cursor ---
def ghost_cursor():
    """A 'ghost' window that follows the cursor."""
    def run_ghost():
        try:
            root = tk.Tk()
            # A small, frameless, transparent window
            root.geometry("30x30+0+0")
            root.overrideredirect(True)
            root.attributes("-transparentcolor", "white")
            root.attributes("-topmost", True)

            canvas = tk.Canvas(root, bg="white", highlightthickness=0)
            canvas.pack()
            # Simple ghost shape
            canvas.create_oval(5, 5, 25, 25, fill="gray", outline="black")

            def update_position():
                while not stop_event.is_set():
                    try:
                        x, y = pyautogui.position()
                        root.geometry(f"+{x+15}+{y+15}")
                        root.update()
                    except tk.TclError:
                        break
                    time.sleep(0.01)

                try:
                    root.destroy()
                except tk.TclError:
                    pass

            update_thread = threading.Thread(target=update_position, daemon=True)
            update_thread.start()
            root.mainloop()
        except Exception:
            pass

    print("[+] Ghost cursor prank activated.")
    ghost_thread = threading.Thread(target=run_ghost, daemon=True)
    ghost_thread.start()

# --- Main Execution ---
def main():
    """Starts all the pranks in separate threads."""
    ctypes.windll.user32.MessageBoxW(0, "The Evil Genius has taken over. Press ESC to beg for mercy.", "eViL_gEniUs.py", 1)

    # Start the ESC listener
    esc_thread = threading.Thread(target=esc_listener, daemon=True)
    esc_thread.start()

    pranks = [
        desktop_screenshot_wallpaper,
        fake_file_deletion,
        screen_color_flash,
        audio_chaos,
        ghost_cursor,
    ]

    threads = []
    for prank in pranks:
        # Stagger the start of the pranks
        time.sleep(random.uniform(1, 3))
        if stop_event.is_set():
            break
        thread = threading.Thread(target=prank, daemon=True)
        thread.start()
        threads.append(thread)

    print("[+] eViL_gEniUs.py is running... Press ESC to stop.")

    stop_event.wait()

    ctypes.windll.user32.MessageBoxW(0, "You got lucky this time. The Evil Genius has been banished... for now.", "Mercy Granted", 1)

if __name__ == "__main__":
    main()
