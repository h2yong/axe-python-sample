import urllib3
import unittest
import json


host = "http://192.168.2.91:8091"
api_url = {
    "postag": "/v1/nlp/ENGLISH/postag",
    "ner": "/v1/nlp/ENGLISH/ner",
    "batch": "/v1/nlp/ENGLISH/batch",
}


test_sentences = [
    "Autonomous cars shift insurance liability toward manufacturers",
    "Apple is looking at buying U.K. startup for $1 billion",
    "Credit and mortgage account holders must submit their requests",
    "San Francisco considers banning sidewalk delivery robots"
]


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.http = urllib3.PoolManager()


    def test00_sentence_postag(self):
        for test_sentence in test_sentences:
            body = {
                'sentence': test_sentence,
                'language': 'ENGLISH'
            }
            body = json.dumps(body).encode('utf-8')
            response = self.http.request('POST', host + api_url['postag'],
                                         body=body,
                                         headers={'Content-Type': 'application/json'})
            result = json.loads(response.data.decode('utf-8'))
            print(result)


    def test01_sentence_ner(self):
        for test_sentence in test_sentences:
            body = {
                'sentence': test_sentence,
                'language': 'ENGLISH'
            }
            body = json.dumps(body).encode('utf-8')
            response = self.http.request('POST', host + api_url['ner'],
                                         body=body,
                                         headers={'Content-Type': 'application/json'})
            result = json.loads(response.data.decode('utf-8'))
            print(result)


    def test02_batch_analyze(self):
        body = {
            "sentences": test_sentences,
            "language": 'ENGLISH'
        }
        body = json.dumps(body).encode('utf-8')
        response = self.http.request('POST', host + api_url['batch'],
                                body=body,
                                headers={'Content-Type': 'application/json'})
        result = json.loads(response.data.decode('utf-8'))
        print(result)


if __name__ == "__main__":
    suite = unittest.TestSuite()

    suite.addTest(TestAPI("test00_sentence_postag"))
    suite.addTest(TestAPI("test01_sentence_ner"))
    suite.addTest(TestAPI("test02_batch_analyze"))

    runner = unittest.TextTestRunner()
    runner.run(suite)