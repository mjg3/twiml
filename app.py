from twilio.rest import Client
from twilio.twiml.voice_response import Gather, VoiceResponse, Say
from flask import request

from flask import Flask
app = Flask(__name__)
#
# Your Account SID from twilio.com/console


@app.route('/', methods=['GET', 'POST'])
def main():
    content = get_file('index.xml')


@app.route('/make_call', methods=['GET', 'POST'])    
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

    return "Main"

@app.route('/handle_data', methods=['GET', 'POST'])
def handle_data():
    print "Handle Data"
    # return "Handle Data"
    # resp = VoiceResponse()

    # Start our <Gather> verb
    # gather = Gather(num_digits=1)
    # gather.say('For sales, press 1. For support, press 2.')
    # resp.append(gather)

    # If the user doesn't select an option, redirect them into a loop
    # resp.redirect('/voice')

    return str(resp)
    # response = VoiceResponse()
    # gather = Gather(input='speech dtmf', timeout=3, num_digits=1)
    # gather.say('Please press 1 or say sales for sales.')
    # response.append(gather)

    # print response

    # return 'Welcome'

if __name__ == "__main__":
    app.run()
