# import json

# def send_music_comand(command):
#     import win32pipe
#     import win32file

#     pipe_name = r'\\.\pipe\mpvsocket'
#     message = json.dumps({"command": command}) + "\n"

#     try:
#         win32pipe.WaitNamedPipe(pipe_name, 2000)

#         handle = win32file.CreateFile(
#             pipe_name,
#             win32file.GENERIC_WRITE,
#             0,
#             None,
#             win32file.OPEN_EXISTING,
#             0,
#             None
#         )

#         win32file.WriteFile(handle, message.encode())
#         handle.close()

#         return True

#     except Exception as e:
#         print(f"Error sending command: {e}")
#         return False

import json
import win32pipe
import win32file

def send_music_command(command):
    pipe_name = r'\\.\pipe\mpvsocket'
    message = json.dumps({"command": command}) + "\n"

    try:
        win32pipe.WaitNamedPipe(pipe_name, 2000)

        handle = win32file.CreateFile(
            pipe_name,
            win32file.GENERIC_READ | win32file.GENERIC_WRITE,
            0,
            None,
            win32file.OPEN_EXISTING,
            0,
            None
        )

        win32file.WriteFile(handle, message.encode())

        buffer = b""
        while True:
            result, chunk = win32file.ReadFile(handle, 4096)
            buffer += chunk

            if b"\n" in buffer:
                break

        win32file.CloseHandle(handle)

        lines = buffer.decode().strip().split("\n")
        return [json.loads(line) for line in lines]

    except Exception as e:
        print(f"Error: {e}")
        return None