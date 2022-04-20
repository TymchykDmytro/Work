
import requests
import pytest
import base64


img = requests.get("http://apimeme.com/meme?meme=Alarm-Clock&top=Top+text&bottom=Bottom+text")
with open("example.jpeg", 'wb') as file:
    file.write(img.content)
with open("example.jpeg", 'rb') as f:
    base64dec = base64.b64decode(f.read())
    base64 = base64.b64encode(base64dec)

def test_equal1():
    assert base64[0] == 74 , 'It must be J'
    assert base64[1] == 70 , 'It must be F'
    assert base64[2] == 73 , 'It must be I'
    assert base64[3] == 70 , 'It must be F'

ask = img.headers['Content-Type']
def test_equal():
    assert ask == 'image/jpeg'
