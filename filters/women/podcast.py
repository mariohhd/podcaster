from pydub.effects import normalize, high_pass_filter, low_pass_filter, compress_dynamic_range
from filters.eq import band_pass_filter

def women_podcast_filter(audio_segment):
    """
    Apply a series of audio filters for women's podcasting.
    Recommended order: normalize, high-pass, low-pass, compression, EQ.
    """
    # Normalize volume
    audio_segment = normalize(audio_segment)
    # Remove low-frequency rumble (cutoff ~150 Hz)
    audio_segment = high_pass_filter(audio_segment, cutoff=150)
    # Remove high-frequency hiss (cutoff ~10000 Hz)
    audio_segment = low_pass_filter(audio_segment, cutoff=10000)
    # Simple EQ: boost upper-mids (band-pass 1000-5000 Hz and overlay)
    audio_segment = band_pass_filter(audio_segment, low_cutoff=1000, high_cutoff=5000)
    # Compress dynamic range for clarity
    audio_segment = compress_dynamic_range(audio_segment, threshold=-18.0, ratio=3.0, attack=5.0, release=50.0)
    return audio_segment
