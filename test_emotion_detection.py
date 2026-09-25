import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    def test_anger(self):
        result = emotion_detector("I am furious about this")
        self.assertIsNotNone(result)

    def test_disgust(self):
        result = emotion_detector("This is disgusting")
        self.assertIsNotNone(result)

    def test_fear(self):
        result = emotion_detector("I am afraid")
        self.assertIsNotNone(result)

    def test_joy(self):
        result = emotion_detector("I am very happy")
        self.assertIsNotNone(result)

    def test_sadness(self):
        result = emotion_detector("I am feeling sad")
        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main()
