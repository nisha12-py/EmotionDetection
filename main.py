from textblob import TextBlob
import text2emotion as te


def detect_emotion(text):


    emotiondict = te.get_emotion(text)
    for i, j in emotiondict.items():
        emotiondict[i] = int(j * 100)

    return emotiondict

def polar_detect(text):

        blob = TextBlob(text)

        for sentence in blob.sentences:
            pol=sentence.sentiment.polarity
            return pol


