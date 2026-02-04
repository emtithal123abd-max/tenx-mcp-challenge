from moviepy import VideoFileClip, AudioFileClip

video = VideoFileClip("artifacts/video/local_video_10s.mp4")
audio = AudioFileClip("artifacts/audio/lyria_jazz_10s.mp3")

final = video.with_audio(audio)

final.write_videofile("artifacts/combined/music_video_10s.mp4", fps=24)

print("Saved artifacts/combined/music_video_10s.mp4")
