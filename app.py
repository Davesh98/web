import eel
import subprocess

eel.init('web')

@eel.expose
def run_command(command):
    commands = {
        "go_to_kitchen": "/path/to/go_to_kitchen.py",
        "wait": "/path/to/wait.py",
        "go_docking": "/path/to/go_docking.py",
        "kangriboque": "/path/to/kangriboque.py",
        "mantalai": "/path/to/mantalai.py",
        "sentinel": "/path/to/sentinel.py"
    }
    script = commands.get(command)
    if script:
        try:
            result = subprocess.run(['python3', script], capture_output=True, text=True)
            return result.stdout or "Executed Successfully!"
        except Exception as e:
            return str(e)
    return "Command not found!"

eel.start('index.html', size=(800, 480), mode='firefox', port='8080')  # Assuming 800x480 is suitable for your 7-inch display

