from pydub import AudioSegment
from filters.men.podcast import men_podcast_filter
 
# Load an example audio file (replace 'input.mp3' with your file)
audio = AudioSegment.from_file('input.mp3')

enhanced_audio = men_podcast_filter(audio)
# Export the processed audio
enhanced_audio.export('output_enhanced.mp3', format='mp3')

print('Audio processing complete. Output saved as output_enhanced.mp3')
