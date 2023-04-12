from twilio.rest import Client
 
# replace PATH_TO_CURRENT_DIRECTORY with the current direcotry where the exported emacs agenda is stored
with open('PATH_TO_CURRENT_DIRECTORY/org-agenda.txt', 'r') as f:
    agenda = f.read()

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)

# Replace the "from" with the number assigned to you from twilio and the variable "to" with the number you signed up to twilio with country codes mentioned
# note: you cannot send messages to a number other than the one you signed up with while using a twilio free account 
message = client.messages.create(
    to="", 
    from_="",
    body= agenda)

print(message.sid)
