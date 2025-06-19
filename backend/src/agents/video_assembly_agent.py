from __future__ import annotations

from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import ImageClip
from moviepy.video.compositing.CompositeVideoClip import concatenate_videoclips
from itertools import zip_longest

from ..config import Config


class VideoAssemblyAgent:
    def __init__(self, fps: int = 24):
        self.fps = fps

    def assemble_video(
        self, images: list[str], audio_clips: list[str], output_path: str
    ) -> str:
        if Config.DEMO_MODE:
            with open(output_path, "w", encoding="utf-8") as f:
                for idx, (img, aud) in enumerate(zip_longest(images, audio_clips)):
                    line = f"frame{idx}: image={img or ''}, audio={aud or ''}\n"
                    f.write(line)
            return output_path

        clips = []
        for img_path, audio_path in zip(images, audio_clips):
            audio = AudioFileClip(audio_path)
            clip = ImageClip(img_path).with_duration(audio.duration).with_audio(audio)
            clips.append(clip)
        for img_path in images[len(audio_clips) :]:
            clips.append(ImageClip(img_path).with_duration(1))
        final_clip = concatenate_videoclips(clips, method="compose")
        final_clip.write_videofile(
            output_path,
            fps=self.fps,
            codec="libx264",
            audio_codec="aac",
            logger=None,
        )
        final_clip.close()
        for c in clips:
            c.close()
        return output_path

    def preview_video(self, video_path: str) -> dict:
        return {"message": "Preview generated", "video_path": video_path}

    def upload_to_shortvideo(
        self, video_path: str, title: str, description: str
    ) -> dict:
        return {
            "message": "Video uploaded to ShortVideo",
            "video_path": video_path,
            "title": title,
        }
