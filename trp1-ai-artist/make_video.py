from moviepy import ColorClip

# 10-second black cinematic background video
clip = ColorClip(size=(1280, 720), color=(10, 10, 10), duration=10)
clip.write_videofile("artifacts/video/local_video_10s.mp4", fps=24)

print("Saved artifacts/video/local_video_10s.mp4")
