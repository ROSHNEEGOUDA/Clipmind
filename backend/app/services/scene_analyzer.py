import cv2
import numpy as np
from typing import List

def detect_scene_type(frame_paths: List[str]) -> str:
    """
    Detect scene type using motion intensity.
    """

    if len(frame_paths) < 2:
        return "generic"

    motion_scores = []

    prev = cv2.imread(frame_paths[0], cv2.IMREAD_GRAYSCALE)

    for path in frame_paths[1:]:
        curr = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if curr is None or prev is None:
            continue

        diff = cv2.absdiff(prev, curr)
        score = np.mean(diff)
        motion_scores.append(score)
        prev = curr

    if not motion_scores:
        return "generic"

    avg_motion = sum(motion_scores) / len(motion_scores)

    # 🔥 Thresholds (tuned for anime)
    if avg_motion > 18:
        return "action"
    elif avg_motion < 6:
        return "emotional"
    else:
        return "calm"
