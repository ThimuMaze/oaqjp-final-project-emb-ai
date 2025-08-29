"""
Server file of emotion detector app
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("EmotionDetector")


@app.route("/")
def index():
    """
    this is to render initial page of the app
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detect():
    """
    this method calls the emotion detector and produces output
    """
    text = request.args.get('textToAnalyze')
    emotion_obj = emotion_detector(text)
    if emotion_obj["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    anger = emotion_obj["anger"]
    disgust = emotion_obj["disgust"]
    fear = emotion_obj["fear"]
    joy = emotion_obj["joy"]
    sadness = emotion_obj["sadness"]
    dominant = emotion_obj["dominant_emotion"]
    return (f"For the given statement, the system response is 'anger': {anger},"
            f" 'disgust': {disgust} , 'fear' : {fear} , 'joy': {joy} and 'sadness' "
            f": {sadness}. The dominant emotion is {dominant}")


if __name__ == "__main__":
    app.run(debug=True)
