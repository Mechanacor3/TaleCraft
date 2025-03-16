from pydub import AudioSegment

def merge_audio_clips(clips):
    """Merge multiple audio clips into a single audio segment."""
    combined = AudioSegment.silent(duration=0)
    for clip in clips:
        combined += clip
    return combined

def adjust_volume(audio_segment, db_change):
    """Adjust the volume of an audio segment by a specified number of decibels."""
    return audio_segment + db_change

def export_audio(audio_segment, file_path, format='mp3'):
    """Export the audio segment to a file in the specified format."""
    audio_segment.export(file_path, format=format)