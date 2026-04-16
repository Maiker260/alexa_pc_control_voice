# import json

# def send_music_command(command):
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

import subprocess

def send_music_command(command):

    command = r'''
    $pipe = new-object System.IO.Pipes.NamedPipeClientStream(".", "mpvsocket", [System.IO.Pipes.PipeDirection]::Out);
    $pipe.Connect();
    $sw = new-object System.IO.StreamWriter($pipe);
    $sw.WriteLine('{ "command": ["add", "volume", 30] }');
    $sw.Flush();
    $sw.Dispose();
    $pipe.Dispose()
    '''

    try:
        subprocess.run(["powershell", "-Command", command])
    except Exception as e:
        print(f"Error sending command: {e}")
        return False