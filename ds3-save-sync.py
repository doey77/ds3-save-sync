from fabric import Connection
from pathlib import Path
from os.path import join
from platform import system

windows_dir = join(Path.home(), "")
steam_deck_dir = join(Path.home(), ".local", "share", "Steam", "steamapps",
                      "compatdata", "374320", "pfx", "drive_c", "users", "steamuser")

if system() == 'Windows':
    local_dir = windows_dir
else:
    local_dir = steam_deck_dir

save_name = "DS30000.sl2"

app_data_dir = join(local_dir, "AppData", "Roaming",
                    "DarkSoulsIII", "0110000105712264", save_name)
server_dir = "/home/ubuntu/gamesaves/ds3"

conn = Connection("flybucks-ubuntu")
server_save_timestamp = conn.run(f"ls {server_dir} -l | grep {save_name}")
