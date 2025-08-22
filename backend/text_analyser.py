import requests


def detect_ai(text):
    try:
        url = "https://ai-content-detection-ai-detector-humanize-ai-text.p.rapidapi.com/detectAIContent"
        querystring = {"noqueue":"1","language":"en"}
        payload = { "text": text }
        headers = {
            "x-rapidapi-key": "be0482bc4amshd1fb5bde054fcc4p1e78e7jsne29c42ca2f60",
            "x-rapidapi-host": "ai-content-detection-ai-detector-humanize-ai-text.p.rapidapi.com",
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=payload, headers=headers, params=querystring)
    except Exception:
        print(Exception)
    if(response['status'] == 'success'):
        return response['result']['aiProbability']
    return "error"

# x = {'status': 'success', 'message': 'Content detection completed successfully', 'result': {'aiProbability': '10%', 'confidence': '85', 'indicators': [{'feature': 'Natural language patterns', 'description': 'The text exhibits smooth, vivid, and cohesive language typical of human artistic writing, with a poetic flow and detailed imagery.', 'significance': 'High (85)'}, {'feature': 'Consistency in writing style', 'description': 'The descriptive style remains consistent throughout, with nuanced emotional expression and human-like attention to sensory details.', 'significance': 'High (80)'}, {'feature': 'Human-like errors or nuances', 'description': 'There are no obvious grammatical errors or awkward phrasing; the style reflects human creative writing more than mechanical output.', 'significance': 'Moderate (70)'}, {'feature': 'Contextual understanding', 'description': 'The passage demonstrates a deep understanding of mood, scenery, and emotional nuance, suggesting human insight.', 'significance': 'High (85)'}, {'feature': 'Emotional expression', 'description': 'The emotional tone is subtle and evocative, conveying wonder and calm, which are characteristic of human poetic description.', 'significance': 'High (80)'}], 'overallAssessment': 'The passage is evocative, descriptive, and emotionally nuanced, reflecting qualities typical of human creative writing. While AI can generate similar text, the richness in imagery and emotional depth strongly suggest human authorship. The language patterns and consistency point toward a human writer, although advanced AI models can produce comparable content. Overall, it appears more likely to be written by a human.', 'recommendations': ['Include more intentionally imperfect phrasing or minor errors to introduce subtle human nuances.', 'Add personal reflections or unique idiosyncrasies to enhance authenticity.', 'Vary sentence structures more widely to mimic natural speech and thought patterns.'], 'textMetrics': {'basicMetrics': {'wordCount': 101, 'sentenceCount': 6, 'averageWordLength': 4.554455445544554, 'uniqueWordRatio': 0.7623762376237624, 'paragraphCount': 1, 'charactersCount': 560, 'punctuationCount': 12}, 'complexityMetrics': {'longWordCount': 18, 'longSentenceCount': 4, 'averageSentenceLength': 16.833333333333332, 'complexityScore': None}, 'readabilityScore': 0, 'textStyle': {'isFormal': False, 'isVerbose': False, 'hasGoodReadability': False, 'textType': 'General/Mixed'}}}, 'cacheTime': 1755784358944}
# print(x['status'])
# print(x['result']['aiProbability'])