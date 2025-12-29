import random
from typing import Tuple, List

# =======================
# LONG-FORM CAPTIONS
# =======================

ACTION_CAPTIONS = [
    "This scene doesn’t give you time to breathe.\n"
    "Every second hits harder than the last 🔥",

    "No buildup. No warning.\n"
    "Just pure intensity from start to end 👀🔥",

    "You think it’s over… and then THIS happens.\n"
    "Watch closely 🔥",
]

EMOTIONAL_CAPTIONS = [
    "Some moments don’t need dialogue.\n"
    "If you’ve felt this before, you’ll understand 👀",

    "This scene stays with you long after it ends.\n"
    "It’s not loud, but it hits deep 💔",

    "Nothing dramatic.\n"
    "Just a moment that quietly breaks you.",
]

CALM_CAPTIONS = [
    "Not every powerful scene is loud.\n"
    "Sometimes, it’s the silence that matters 🌙",

    "A quiet moment, easy to miss.\n"
    "But it changes everything.",

    "No rush. No chaos.\n"
    "Just a scene that feels different.",
]

GENERIC_CAPTIONS = [
    "This moment feels different every time you watch it.\n"
    "Hard to explain, harder to forget 👀",

    "You might miss it the first time.\n"
    "But once you notice it, it stays with you.",
]

# =======================
# HASHTAG SETS (SEPARATE)
# =======================

ANIMATED_ACTION_HASHTAGS = [
    "#animation",
    "#animated",
    "#animeedit",
    "#actionscene",
    "#epicmoment",
    "#reels",
    "#shorts",
    "#clipmind"
]

ANIMATED_EMOTIONAL_HASHTAGS = [
    "#animation",
    "#animated",
    "#animeedit",
    "#emotional",
    "#storytelling",
    "#reels",
    "#shorts",
    "#clipmind"
]

ANIMATED_CALM_HASHTAGS = [
    "#animation",
    "#animated",
    "#animeedit",
    "#cinematic",
    "#vibes",
    "#reels",
    "#shorts",
    "#clipmind"
]

REAL_ACTION_HASHTAGS = [
    "#actionscene",
    "#epicmoment",
    "#highintensity",
    "#reels",
    "#shorts",
    "#clipmind"
]

REAL_EMOTIONAL_HASHTAGS = [
    "#emotional",
    "#storytelling",
    "#cinematic",
    "#reels",
    "#shorts",
    "#clipmind"
]

REAL_CALM_HASHTAGS = [
    "#cinematic",
    "#visualstorytelling",
    "#vibes",
    "#reels",
    "#shorts",
    "#clipmind"
]

REAL_GENERIC_HASHTAGS = [
    "#cinematic",
    "#storymoment",
    "#reels",
    "#shorts",
    "#clipmind"
]

# =======================
# MAIN GENERATOR
# =======================

def generate_caption_and_hashtags(
    scene_type: str,
    is_animated: bool
) -> Tuple[str, List[str]]:

    # 🎬 CAPTION SELECTION
    if scene_type == "action":
        caption = random.choice(ACTION_CAPTIONS)
    elif scene_type == "emotional":
        caption = random.choice(EMOTIONAL_CAPTIONS)
    elif scene_type == "calm":
        caption = random.choice(CALM_CAPTIONS)
    else:
        caption = random.choice(GENERIC_CAPTIONS)

    # 🏷️ HASHTAG SELECTION (NO MERGING)
    if is_animated:
        if scene_type == "action":
            hashtags = ANIMATED_ACTION_HASHTAGS
        elif scene_type == "emotional":
            hashtags = ANIMATED_EMOTIONAL_HASHTAGS
        else:
            hashtags = ANIMATED_CALM_HASHTAGS
    else:
        if scene_type == "action":
            hashtags = REAL_ACTION_HASHTAGS
        elif scene_type == "emotional":
            hashtags = REAL_EMOTIONAL_HASHTAGS
        elif scene_type == "calm":
            hashtags = REAL_CALM_HASHTAGS
        else:
            hashtags = REAL_GENERIC_HASHTAGS

    return caption, hashtags
