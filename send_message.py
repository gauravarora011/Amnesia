from twilio.rest import Client

account_sid = "AC71e6105c8c48c7a3c4f64ecbae8f180d"
auth_token = "e7abd2684f35ef717f267d2b1837d75d"
client = Client(account_sid, auth_token)

def Send_Message():
    counter = 0
    while counter<5:
        message = client.messages.create(
                "+917508819230",
                body="Hi John!!",from_="+13213514652")
        counter = counter + 1
        if message.error_code != None:
            return True
    return False

if __name__ == "__main__":
    print Send_Message()
