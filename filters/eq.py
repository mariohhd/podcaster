from pydub.effects import high_pass_filter, low_pass_filter

def band_pass_filter(audio_segment, low_cutoff, high_cutoff):
    """
    Simulate a band-pass filter by applying high-pass then low-pass.
    """
    filtered = high_pass_filter(audio_segment, cutoff=low_cutoff)
    filtered = low_pass_filter(filtered, cutoff=high_cutoff)
    mids = filtered + 3  # boost by 3dB
    audio_segment = audio_segment.overlay(mids)
    return audio_segment