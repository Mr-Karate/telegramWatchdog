import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import telegram_send
import argparse



class EventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        file = event.src_path
        with open(file, 'r') as f:
            lines = f.read().splitlines()
            last_line = lines[-1]
            telegram_send.send(messages=[last_line], conf="telegram-send.conf")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Watch for changes on any file in current directory  and send the last line of the file to a telegram chat using a pre-configured bot account. ")
    parser.add_argument("-p", type=str, help='Especify a File or Directory to watch (default: ".")')
    parser.parse_args()

    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = EventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()