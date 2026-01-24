import wave
import struct
import math

SAMPLE_RATE = 44100  # CD音質
VOLUME = 0.3         # 音量（0.0〜1.0）

def make_bgm(filename, tempo, notes):
    """
    notes: [(周波数Hz, 長さ(拍)), ...]
    """
    wf = wave.open(filename, "w")
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(SAMPLE_RATE)

    for freq, length in notes:
        duration = 60 / tempo * length
        samples = int(SAMPLE_RATE * duration)

        for i in range(samples):
            t = i / SAMPLE_RATE
            value = VOLUME * math.sin(2 * math.pi * freq * t)
            data = struct.pack("<h", int(value * 32767))
            wf.writeframesraw(data)

    wf.close()

# ----------------------------
# Stage1 BGM（通常戦）
# ----------------------------
stage1_notes = [
    (440, 1), (523, 1), (659, 2),
    (523, 1), (440, 1), (392, 2),
]

make_bgm(
    filename="bgm_stage1.wav",
    tempo=120,
    notes=stage1_notes
)

# ----------------------------
# Stage2 BGM（ボス戦）
# ----------------------------
stage2_notes = [
    (220, 1), (262, 1), (294, 1), (330, 1),
    (294, 2), (262, 2), (220, 2),
]

make_bgm(
    filename="bgm_stage2.wav",
    tempo=90,
    notes=stage2_notes
)

print("🎵 BGM生成完了！")
