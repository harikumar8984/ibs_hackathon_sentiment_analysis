# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask import request
from flask import abort
import spacy
from spacy.tokens import Doc
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
import en_core_web_sm
from obscenefilter import ObsceneFilter

app = Flask(__name__)
sentiment_analyzer = SentimentIntensityAnalyzer()
nlp = en_core_web_sm.load()
pf = ObsceneFilter()
pf.set_censor("@")

@app.route('/ibs_hackathon_2018/api/v1.0/sentiment_analyzer', methods=['POST'])
def analysis_sentiment():  
   if not request.json or not 'text' in request.json:
     abort(400) 
   Doc.set_extension('polarity_scores', getter=polarity_scores, force=True)
   text = request.json.get('text')
   doc = nlp(u"%s" % text)
   return jsonify({'score': doc._.polarity_scores, 'isProfane': pf.is_profane(text), 'analysedText': pf.censor(text) }), 201

def polarity_scores(doc):
    return sentiment_analyzer.polarity_scores(doc.text)

if __name__ == '__main__':
    app.run(debug=True)
