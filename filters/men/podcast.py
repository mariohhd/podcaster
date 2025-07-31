from pydub.effects import normalize, high_pass_filter, low_pass_filter, compress_dynamic_range
from filters.eq import band_pass_filter

def men_podcast_filter(audio_segment):
    """
    Apply a series of audio filters for men's podcasting.
    Recommended order: normalize, high-pass, low-pass, compression.
    """
    # Normalize volume
    audio_segment = normalize(audio_segment)
    # Remove low-frequency rumble (cutoff ~100 Hz)
    audio_segment = high_pass_filter(audio_segment, cutoff=100)
    # Remove high-frequency hiss (cutoff ~9000 Hz)
    audio_segment = low_pass_filter(audio_segment, cutoff=9000)
    # Simple EQ: boost mids (band-pass 300-3000 Hz and overlay)
    audio_segment = band_pass_filter(audio_segment, low_cutoff=300, high_cutoff=3000)
    # Compress dynamic range for clarity
    audio_segment = compress_dynamic_range(audio_segment, threshold=-20.0, ratio=4.0, attack=5.0, release=50.0)
    return audio_segment

