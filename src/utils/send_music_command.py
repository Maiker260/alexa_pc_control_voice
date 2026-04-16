import subprocess
import json

def send_music_command(command):
    json_command = json.dumps({"command": command})
    print(json_command)
    ps_script = f'''
    $pipe = new-object System.IO.Pipes.NamedPipeClientStream(".", "mpvsocket", [System.IO.Pipes.PipeDirection]::Out);
    $pipe.Connect();
    $sw = new-object System.IO.StreamWriter($pipe);
    $sw.WriteLine('{json_command}');
    $sw.Flush();
    $sw.Dispose();
    $pipe.Dispose()
    '''
    print()
    print(ps_script)
    try:
        subprocess.run(["powershell", "-Command", ps_script])
    except Exception as e:
        print(f"Error sending command: {e}")
        return False