import subprocess
from pathlib import Path


class VideoClip:
    VLC_EXE_PATH = r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"

    def __init__(self, filename):
        self.filename = Path(filename)

    def play(self):
        cmd_line = [
            self.VLC_EXE_PATH,
            "--no-video-title-show",
            "--quiet",
            "--video-on-top",
            self.filename.as_uri(),
            "vlc://quit"
        ]
        subprocess.call(cmd_line)


if __name__ == '__main__':
    clip = VideoClip(r"C:\Users\grownups\PycharmProjects\Mom50\resources\VID-20201209-WA0002.mp4")
    clip.play()
