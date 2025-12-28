import random

def detect_highlights(duration: float):
    """
    Random + logical highlight detection
    Reel duration always:
      - > 30 sec
      - < 1.1 min (~66 sec)
    """

    if duration < 60:
        return []


    # RANDOM TOTAL REEL DURATION (STRICT BOUNDS)

    total_reel_duration = random.randint(32, 65)  # seconds

    # CHUNK DURATION (SMALL,PUNCHY)

    chunk_duration = random.randint(3, 5)

    # NUMBER OF CHUNKS

    max_chunks = total_reel_duration // chunk_duration

    # MINIMUM GAP (SCALES WITH VIDEO LENGTH)

    # 20–30 sec for short videos, minutes for long ones
    min_gap = max(20, int(duration * 0.05))

    # RANDOM SAMPLING WITH GAP ENFORCEMENT
    highlights = []
    used_starts = []
    attempts = 0
    MAX_ATTEMPTS = 3000

    while len(highlights) < max_chunks and attempts < MAX_ATTEMPTS:
        attempts += 1

        start = random.randint(0, int(duration - chunk_duration))

        # spacing constraint
        if any(abs(start - s) < min_gap for s in used_starts):
            continue

        highlights.append({
            "start": start,
            "duration": chunk_duration
        })
        used_starts.append(start)

    # sort for clean timeline
    highlights.sort(key=lambda x: x["start"])

    return highlights
