import textwrap
from pytubefix import YouTube
from urllib.parse import urlparse, parse_qs

def extract_video_id(url: str):
    parsed = urlparse(url)
    if parsed.hostname in ["www.youtube.com", "youtube.com"]:
        return parse_qs(parsed.query).get("v", [None])[0]
    elif parsed.hostname == "youtu.be":
        return parsed.path[1:]
    else:
        return None

async def getvideotranscript(url: str):
    video_id = extract_video_id(url)
    if not video_id:
        return "Error: Could not extract video ID from URL."

    yt = YouTube(url)
    header = f"{'='*80}\nTitle: {yt.title}\n{'='*80}\n"
    description = f"Description:\n{textwrap.fill(yt.description, width=80)}\n{'-'*80}\n"

    # Get English captions
    captions = yt.captions.get_by_language_code('en')
    if not captions:
        transcript_text = "No English transcript available."
    else:
        transcript_text = captions.generate_srt_captions()  # includes timestamps

    transcript_text = textwrap.fill(transcript_text, width=80)
    return header + description + "Transcript:\n" + transcript_text + f"\n{'='*80}\n"

async def get_transcript_with_timestamps(url: str, wrap_width: int = 80):
    video_id = extract_video_id(url)
    if not video_id:
        return "Error: Could not extract video ID from URL."

    yt = YouTube(url)
    header = f"{'='*80}\nTitle: {yt.title}\n{'='*80}\n"
    description = f"Description:\n{textwrap.fill(yt.description, width=wrap_width)}\n{'-'*80}\n"

    captions = yt.captions.get_by_language_code('en')
    if not captions:
        transcript_text = "No English transcript available."
    else:
        transcript_text = captions.generate_srt_captions()

    transcript_lines = transcript_text.splitlines()
    transcript_text = "\n".join(textwrap.fill(line, width=wrap_width) for line in transcript_lines)

    return header + description + "Transcript:\n" + transcript_text + f"\n{'='*80}\n"
