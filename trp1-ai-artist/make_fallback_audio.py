import math, wave, struct
from pathlib import Path

out_path = Path("artifacts/audio/fallback_tone_10s.wav")
out_path.parent.mkdir(parents=True, exist_ok=True)

duration = 10.0
sample_rate = 44100
freq = 440.0
amplitude = 0.2

n_samples = int(duration * sample_rate)

with wave.open(str(out_path), "wb") as wf:
    wf.setnchannels(2)
    wf.setsampwidth(2)
    wf.setframerate(sample_rate)

    for i in range(n_samples):
        t = i / sample_rate
        sample = amplitude * math.sin(2 * math.pi * freq * t)
        s16 = int(sample * 32767)
        wf.writeframesraw(struct.pack("<hh", s16, s16))

print(f"Saved {out_path}")
