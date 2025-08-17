import random
import keyboard
import time
import ctypes
import threading
import pyautogui

# Ultimate Haunted Mode 👻
pyautogui.FAILSAFE = True  # keep emergency escape by moving mouse to corner

letters = "abcdefghijklmnopqrstuvwxyz!@$%^&*()_+-=[]{|;:',.<>?/~`}ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Fun popup at start
ctypes.windll.user32.MessageBoxW(0, "👻 Your PC is haunted! Press ESC to banish the ghost.", "Keyboard Ghost", 1)

# --- Keyboard Prank ---
def prank_typing(event):
    if event.name.isalpha():
        action = random.choice(["replace", "double", "emoji", "reverse", "caps"])

        if action == "replace":
            fake_letter = random.choice(letters)
            keyboard.write(fake_letter, delay=0)
        elif action == "double":
            keyboard.write(event.name * 2, delay=0)
        elif action == "emoji":
            keyboard.write(random.choice([" 😜", " 🤡", " 👻", " 💀", " 😱", " 🫠"]), delay=0)
        elif action == "reverse":
            keyboard.write(event.name[::-1], delay=0)  # just same char but looks creepy
        elif action == "caps":
            keyboard.write(event.name.upper(), delay=0)

        return False  # block original key

keyboard.on_press(prank_typing)

# --- Mouse Prank ---
def prank_mouse():
    screen_w, screen_h = pyautogui.size()
    while True:
        if keyboard.is_pressed("esc"):
            break
        move_style = random.choice(["random", "circle", "shake"])

        if move_style == "random":
            x = random.randint(50, screen_w - 50)
            y = random.randint(50, screen_h - 50)
            pyautogui.moveTo(x, y, duration=0.05)

        elif move_style == "circle":
            for i in range(0, 360, 30):
                if keyboard.is_pressed("esc"): break
                angle = i * 3.14 / 180
                x = screen_w//2 + int(200 * random.random() * (1 + random.random()) * (random.choice([-1,1])))
                y = screen_h//2 + int(200 * random.random() * (1 + random.random()) * (random.choice([-1,1])))
                pyautogui.moveTo(x, y, duration=0.05)

        elif move_style == "shake":
            current_x, current_y = pyautogui.position()
            for _ in range(10):
                if keyboard.is_pressed("esc"): break
                pyautogui.moveTo(current_x + random.randint(-50, 50), current_y + random.randint(-50, 50), duration=0.01)

        time.sleep(0)

# --- Ghost Whispers ---
def ghost_whispers():
    messages = [
        "👻 I’m inside your PC...",
        "💀 You can’t escape...",
        "😜 Boo!",
        "😎 Ghost mode activated...",
        "🕯️ The ritual is complete...",
        "🩸 I see your hands shaking...",
        "🖤 Type faster, mortal...",
        "☠️ Your keyboard belongs to me..."
    ]
    while True:
        if keyboard.is_pressed("esc"):
            break
        time.sleep(random.randint(0,1))  # random delay
        ctypes.windll.user32.MessageBoxW(0, random.choice(messages), "Ghost Whisper", 1)

# --- Screen Flicker ---
def screen_flicker():
    while True:
        if keyboard.is_pressed("esc"):
            break
        # Invert colors effect using fake full-screen popups
        if random.random() < 0.1:  # sometimes flicker
            ctypes.windll.user32.MessageBoxW(0, "⚡ Screen glitch...", "Ghost Glitch", 1)
        time.sleep(0)

# Run pranks in background threads
threading.Thread(target=prank_mouse, daemon=True).start()
threading.Thread(target=ghost_whispers, daemon=True).start()
threading.Thread(target=screen_flicker, daemon=True).start()

print("Keyboard & Mouse Ghost is running... Press ESC to banish it 👻")
keyboard.wait("esc")

# Goodbye message
ctypes.windll.user32.MessageBoxW(0, "✨ The ghost has been banished... for now.", "Exorcism Complete", 1)
