from datetime import datetime
import os

ANIMATE_OUTPUT = True
OUTPUT_DELAY = 0.005

def splash_text() -> str:
    user: str = os.environ["USER"]
    shell: str = os.environ["SHELL"].split("/")[-1]
    distro: str = os.popen("uname -a").read().split(" ")[1].title()
    current_time: str = datetime.today().strftime("%I:%M:%S %p")

    text: str = f"< User: {user} | Shell: {shell} | Distribution: {distro} | {current_time} >"
    padding = " " * (os.get_terminal_size().columns//2 - len(text)//2)

    return f"\n{padding}{text}\n"