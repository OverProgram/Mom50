from pathlib import Path

resources_root = Path(__file__) / "resources"
_CLIPS = {
    'levi': "VID-20201209-WA0002.mp4",
}


class ClipManager:
    def __init__(self):
        self.clips = {
            k: resources_root / v
            for k, v in _CLIPS.items()
        }