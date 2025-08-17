import random
import time
import threading
import ctypes
import os
import winsound
import keyboard
import subprocess
import pyautogui

"""
💀 Haunted PC Prank — Version 2 (Max Scare, Single Safe Exit)
- Extremely annoying but NON-DESTRUCTIVE prank.
- ONE guaranteed exit: press ESC to banish the ghost.
- No persistence, no self-spread, Cdocument no file changes.
- Windows-only (uses MessageBoxW, winsound, Notepad).
is now haunted. 👻Do not resist.
🕯️ The candles are lit...  😜
HOW TO STOP: Press ESC. That’s the ONLY control.
"""

# -------- Global Safety -------
# Only ESC should stop everything (requested). We disable PyAutoGUI corner failsafe.
pyautogui.FAILSAFE = True

# Shared stop event set by ESC
stop_event = threading.Event()

# Show start popup
ctypes.windll.user32.MessageBoxW(0, "👻 Your PC is haunted! Press ESC to banish the ghost.", "Keyboard Ghost", 1)

letters = "abcdefghijklmnopqrstuvwxyz!@$%^&*()_+-=[]{|;:',.<>?/~`}ABCDEFGHIJKLMNOPQRSTUVWXYZ"
emojis  = [" 😜", " 🤡", " 👻", " 💀", " 😱", " 🫠", " 🕯️", " 🐍", " 🧿", " 🩸"]
phrases = [
    "👁️ I see you... ",
    "Your PC is mine... ",
    "Don't look behind you... ",
    "💀 The ritual is almost done... ",
    "☠️ Your keyboard belongs to me... ",
    "🕯️ The candles are lit... ",
]

# ------------- ESC Listener -------------

def esc_listener():
    keyboard.wait("esc")
    print("\n👻 Ghost has been banished. Exiting...")
    os._exit(0)  # force quit all threads safely







def haunt_notepad_only():
    while True:
        if keyboard.is_pressed("esc"):
            break

        # Open Notepad
        subprocess.Popen("notepad.exe")
        time.sleep(1)  # give it a moment to openst... 👻👻 You can't escape the ghost... 👻👻 You can't escape the ghost... 👻👻 You can't escape the ghost... 👻👻 You can't escape the ghost... 👻👻 You can't escape the ghost... 👻👻 You can't escape the ghost... 👻👻 You can't escape the ghost... 👻👻 You can't escape the ghost... 👻👻 You can't escape the ghost... 👻
        

        # Spam creepy text super fast
        keyboard.write("👻 You can't escape the ghost... 👻\n" * 10, delay=0.005)

        # Short pause before the next haunting
        time.sleep(random.randint(1, 2))


# ------------- Keyboard Haunting -------------

def prank_typing(event):
    if stop_event.is_set():
        return True
    try:
        # Only prank letter keys and space/backspace events
        if event.name is None:
            return True
        name = event.name
        # Ignore holding modifier keys
        if name in {"shift", "ctrl", "alt", "alt gr", "caps lock", "tab", "windows"}:
            return True

        actions = ["replace", "double", "emoji", "caps", "backspace"]
        if name.isalpha():
            action = random.choice(actions)
            if action == "replace":
                keyboard.write(random.choice(letters), delay=0)
            elif action == "double":
                keyboard.write(name * 2, delay=0)
            elif action == "emoji":
                keyboard.write(random.choice(emojis), delay=0)
            elif action == "caps":
                keyboard.write(name.upper(), delay=0)
            elif action == "backspace":
                keyboard.send("backspace")
            return False  # block original key
        elif name == "space":
            # Sometimes inject spooky emoji/phrase on spaces
            if random.random() < 0.2:
                keyboard.write(random.choice(emojis), delay=0)
                return False
        elif name == "backspace":
            # Occasionally negate backspace to frustrate
            if random.random() < 0.3:
                keyboard.write(random.choice(letters), delay=0)
                return False
    except Exception:
        pass
    return True

keyboard.on_press(prank_typing)

# ------------- Auto-typing Spirits -------------

def ghost_autotyping():
    while not stop_event.is_set():
        time.sleep(random.randint(1, 2))
        if stop_event.is_set():
            break
        keyboard.write(random.choice(phrases), delay=0)
        if random.random() < 0.5:
            keyboard.write(random.choice(emojis), delay=0)

# ------------- Mouse Haunting -------------

def move_random(screen_w, screen_h):
    x = random.randint(30, screen_w - 30)
    y = random.randint(30, screen_h - 30)
    pyautogui.moveTo(x, y, duration=0)

def move_shake():
    cx, cy = pyautogui.position()
    for _ in range(15):
        if stop_event.is_set():
            return
        pyautogui.moveTo(cx + random.randint(-60, 60), cy + random.randint(-60, 60), duration=0.02)

def move_spiral(screen_w, screen_h):
    cx, cy = screen_w // 2, screen_h // 2
    r = random.randint(80, 220)
    steps = 28
    for i in range(steps):
        if stop_event.is_set():
            return
        angle = 2 * 3.14159 * (i / steps)
        x = int(cx + r * (i/steps) * 0.8 * (1 + 0.2*random.random()) * (1 if i % 2 else -1))
        y = int(cy + r * (i/steps) * 0.8 * (1 + 0.2*random.random()) * (1 if (i//3) % 2 else -1))
        pyautogui.moveTo(max(10, min(x, screen_w-10)), max(10, min(y, screen_h-10)), duration=0)

def lock_mouse(seconds=1.0):
    # Holds mouse in a tiny jittery jail
    cx, cy = pyautogui.position()
    end = time.time() + seconds
    while time.time() < end and not stop_event.is_set():
        pyautogui.moveTo(cx + random.randint(-5, 5), cy + random.randint(-5, 5), duration=0)


def prank_mouse():
    w, h = pyautogui.size()
    while not stop_event.is_set():
        style = random.choice(["random", "shake", "spiral", "lock"])
        if style == "random":
            for _ in range(random.randint(3, 8)):
                if stop_event.is_set(): break
                move_random(w, h)
        elif style == "shake":
            move_shake()
        elif style == "spiral":
            move_spiral(w, h)
        elif style == "lock":
            lock_mouse(seconds=random.uniform(1.5, 3.5))
        time.sleep(0)

# ------------- Ghost Whispers (Popups) -------------

def ghost_whispers():
    msgs = [
        "👻 I’m inside your PC...",
        "💀 You can’t escape...",
        "😜 Boo!",
        "😎 Ghost mode activated...",
        "🕯️ The ritual is complete...",
        "🩸 I see your hands shaking...",
        "🖤 Type faster, mortal...",
        "☠️ Your keyboard belongs to me...",
    ]
    while not stop_event.is_set():
        time.sleep(random.randint(6, 14))
        if stop_event.is_set():
            break
        ctypes.windll.user32.MessageBoxW(0, random.choice(msgs), "Ghost Whisper", 1)

# ------------- Fake System Glitches -------------

def fake_system_glitches():
    while not stop_event.is_set():
        time.sleep(random.randint(1, 2))
        if stop_event.is_set():
            break
        # Random fake error
        if random.random() < 0.6:
            ctypes.windll.user32.MessageBoxW(0, "⚠️ Critical Error: Unknown Ghost Process", "System Alert", 16)
        # Random Notepad possess
        if random.random() < 0.5:
            os.system("start notepad.exe")
            time.sleep(0)
            keyboard.write("This document is now haunted. 👻\nDo not resist.\n", delay=0)

# ------------- Creepy Sounds -------------

def creepy_sounds():
    while not stop_event.is_set():
        time.sleep(random.uniform(4.0, 9.0))
        if stop_event.is_set():
            break
        # Random beeps like static/whispers
        for _ in range(random.randint(1, 3)):
            if stop_event.is_set():
                return
            winsound.Beep(random.randint(220, 880), random.randint(120, 320))
            time.sleep(1)

# ------------- Screen Flicker (cosmetic) -------------

def screen_flicker():
    while not stop_event.is_set():
        time.sleep(random.randint(1, 2))
        if stop_event.is_set():
            break
        if random.random() < 0.8:
            ctypes.windll.user32.MessageBoxW(0, "⚡ Screen glitch...", "Ghost Glitch", 1)

# ------------- Run Everything -------------

threads = [
    threading.Thread(target=haunt_notepad_only, daemon=True),
    threading.Thread(target=esc_listener, daemon=True),
    threading.Thread(target=prank_mouse, daemon=True),
    threading.Thread(target=ghost_whispers, daemon=True),
    threading.Thread(target=fake_system_glitches, daemon=True),
    threading.Thread(target=creepy_sounds, daemon=True),
    threading.Thread(target=screen_flicker, daemon=True),
    threading.Thread(target=ghost_autotyping, daemon=True),
]

for t in threads:
    t.start()

print("Keyboard & Mouse Ghost v2 is running... Press ESC to banish it 👻")

# Block until ESC pressed
stop_event.wait()

# Goodbye message
ctypes.windll.user32.MessageBoxW(0, "✨ The ghost has been banished... for now.", "Exorcism Complete", 1)
