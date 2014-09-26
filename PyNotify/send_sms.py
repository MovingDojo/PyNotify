import sys
import twilio
from twilio.rest import TwilioRestClient

def send_notification(body):
	account_sid = ""
	auth_token = ""
	try:
		client = TwilioRestClient(account_sid, auth_token)
		message = client.messages.create(
			body = "Hello World",
			to   = "",
			from_ = ""
		)
	except twilio as e:
		print e

if __name__ == "__main__":
	body = raw_input()
	send_notification(body)

