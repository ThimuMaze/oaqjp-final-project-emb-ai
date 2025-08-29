from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
# app creation
app = Flask("EmotionDetector")
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/emotionDetector")
def emotion_detect():
    text = request.args.get('textToAnalyze')
    emotion_obj = emotion_detector(text)
    print(emotion_obj)
    return "For the given statement, the system response is 'anger': {}, 'disgust': {} , 'fear' : {} , 'joy': {} and 'sadness' : {}. The dominant emotion is {}".format(emotion_obj["anger"] , emotion_obj["disgust"], emotion_obj["fear"], emotion_obj["joy"], emotion_obj["sadness"],emotion_obj["dominant_emotion"])


if __name__ == "__main__":
    app.run(debug=True)
