from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('IUfzoYF0IBR3KjUQ7KtmGx3hWVYlq6XS8Q/0Y7pKl3pRFpLf8RHkfojlCh5qlKrGhRyQ7SyO4Ceo8M9TZf9P6aLX1zMfXz7jVQ/RFk/LHotcygFLpU4r96/lg4J2O35dn+7BQOEDs5ub2+K3bvfy0wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9dbf1a57741ae5614d615a38363fae3c')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="你吃飯了嗎?"))


if __name__ == "__main__":
    app.run()