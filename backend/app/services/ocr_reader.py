import easyocr
import os


reader = easyocr.Reader(['en'], gpu=False)

def extract_text_from_frames(frame_paths):
    """
    Extract text from a list of image frames using EasyOCR.
    """

    detected_texts = set()

    for frame in frame_paths:
        try:
            results = reader.readtext(frame, detail=0)
            for text in results:
                clean = text.strip()
                if len(clean) > 3:
                    detected_texts.add(clean)
        except Exception:
            continue
    
    return list(detected_texts)