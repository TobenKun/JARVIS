from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class ConfigReloadHandler(FileSystemEventHandler):
    def __init__(self, broker, config_path="config/agents.yaml"):
        self.broker = broker
        self.config_path = config_path
        self.last_reload = 0
        self.debounce_seconds = 1

    def on_modified(self, event):
        if event.src_path.endswith(self.config_path):
            now = time.time()
            if now - self.last_reload > self.debounce_seconds:
                print("🔁 Config file changed. Reloading agents...")
                try:
                    self.broker.reload_agents()
                    self.last_reload = now
                except Exception as e:
                    print("❌ Reload failed:", e)

def start_config_watcher(broker, config_path="config/agents.yaml"):
    from pathlib import Path
    import os

    abs_config_path = os.path.abspath(config_path)
    config_dir = str(Path(abs_config_path).parent)

    observer = Observer()
    handler = ConfigReloadHandler(broker, abs_config_path)
    observer.schedule(handler, config_dir, recursive=False)
    observer.start()
    print("👁️ Watching config.yaml for changes...")
    return observer

