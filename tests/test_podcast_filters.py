import unittest
from pydub import AudioSegment
from filters.women.podcast import women_podcast_filter
from filters.men.podcast import men_podcast_filter

class TestPodcastFilters(unittest.TestCase):
    def setUp(self):
        # Generate a 1-second silent audio segment for testing
        self.audio = AudioSegment.silent(duration=1000)

    def test_women_podcast_filter_runs(self):
        processed = women_podcast_filter(self.audio)
        self.assertIsInstance(processed, AudioSegment)
        self.assertEqual(len(processed), len(self.audio))

    def test_men_podcast_filter_runs(self):
        processed = men_podcast_filter(self.audio)
        self.assertIsInstance(processed, AudioSegment)
        self.assertEqual(len(processed), len(self.audio))

if __name__ == "__main__":
    unittest.main()
