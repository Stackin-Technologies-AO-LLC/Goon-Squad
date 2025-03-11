import os
import psutil

def check_system():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    print(f"🖥️ CPU: {cpu}% | RAM: {mem}%")

if __name__ == "__main__":
    check_system()
