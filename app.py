import openai
import twilio
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

app = Flask(__name__)

#OpenAI API Key 
openai.api_key = "YOUR_API_KEY"

#Twilio Account SID and Auth Token 
account_sid = "YOUR_SID"
auth_token = "YOUR_AUTHTOKEN"
client = Client(account_sid, auth_token)

@app.route("/sms", methods=["POST"])
def sms_reply():
    incoming_msg = request.values.get("Body", "").lower()
    response = generate_response(incoming_msg)
    twiml = MessagingResponse()
    twiml.message(response)
    return str(twiml)

#Note: You can adjust the ChatGPT model and max tokens for the response depending on specific use case or the desired length of the generated text 
def generate_response(prompt):
    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, max_tokens=1000).choices[0].text
    return response


if __name__ == "__main__":
     app.run(debug=True)
