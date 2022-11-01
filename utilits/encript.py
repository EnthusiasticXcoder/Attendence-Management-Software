import base64

def encode64(string):
    arr = bytes(string, 'utf-8')
    barr=base64.b64encode(arr)
    return barr


def decode64(data):
    b=base64.b64decode(data)
    string=b.decode("utf-8")
    return string
