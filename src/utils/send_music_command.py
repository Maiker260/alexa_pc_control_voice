import json

def send_music_comand(command):
    pipe_path = r"\\.\pipe\mpvsocket"

    message = json.dumps({"command": command})

    try:
        with open(pipe_path, "w") as pipe:
            pipe.write(message + "\n")
            pipe.flush()
        
        return True
    except Exception as e:
        print(f"Error sending command: {e}")
        return False