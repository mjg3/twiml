from twilio.rest import Client
from twilio.twiml.voice_response import Gather, VoiceResponse, Say
from flask import request

from flask import Flask
app = Flask(__name__)
#
# Your Account SID from twilio.com/console


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        print request.form
    else:
        account_sid = "AC17aff2a74960a87c99ce7037342c1982"
        # Your Auth Token from twilio.com/console
        auth_token  = "2900ed6c5c3dff153f90fee834d37a82"

        client = Client(account_sid, auth_token)
        #
        print "About to call"
        call = client.calls.create(
            to="+19737382206",
            from_="+18026130730",
            url="https://twiml-xml.herokuapp.com/index.xml"
        )

# def collect():

    # response = VoiceResponse()
    # gather = Gather(input='speech dtmf', timeout=3, num_digits=1)
    # gather.say('Please press 1 or say sales for sales.')
    # response.append(gather)

    # print response

    # return 'Welcome'

def collection():
    print "collecting"

if __name__ == "__main__":
    app.run()
