from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        result_1 = emotion_detection('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        result_2 = emotion_detection('I am really mad about this')
        self.assertEqual(result_1['dominant_emotion'], 'anger')
        result_3 = emotion_detection('I feel disgusted just hearing about this')
        self.assertEqual(result_1['dominant_emotion'], 'disgust')
        result_4 = emotion_detection('I am so sad about this')
        self.assertEqual(result_1['dominant_emotion'], 'sadness')
        result_5 = emotion_detection('I am really afraid that this will happen')
        self.assertEqual(result_1['dominant_emotion'], 'fear')



unittest.main()