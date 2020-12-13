import json
import subprocess

from common import RESOURCE_FOLDER


class ClipManager:
    VLC_EXE_PATH = r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"

    def __init__(self):
        with open(RESOURCE_FOLDER / 'clips.json') as f:
            _clips = json.load(f)

        self.clips = {
            k: RESOURCE_FOLDER / v
            for k, v in _clips.items()
        }

    def play(self, clip_name):
        cmd_line = [
            self.VLC_EXE_PATH,
            "--no-video-title-show",
            "--quiet",
            "--video-on-top",
            self.clips[clip_name].as_uri(),
            "vlc://quit"
        ]
        subprocess.call(cmd_line)
