def detect_highlights(duration: float):
    """
    Non-continuous highlight sampling.
    Takes small portions from across the entire video
    and combines them into ONE reel.
    """

    if duration < 10:
        return []

    CHUNK_DURATION = 10   # seconds per portion
    TOTAL_CHUNKS = 3      # 3 x 10s = 30s reel

    highlights = []

    # Divide video into equal regions
    step = duration / (TOTAL_CHUNKS + 1)

    for i in range(1, TOTAL_CHUNKS + 1):
        start = int(step * i)

        # Safety check
        if start + CHUNK_DURATION > duration:
            start = max(0, duration - CHUNK_DURATION)

        highlights.append({
            "start": start,
            "duration": CHUNK_DURATION
        })

    return highlights
