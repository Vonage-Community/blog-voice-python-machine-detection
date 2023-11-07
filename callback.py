from flask import Flask, request

app = Flask(__name__)

action_when_human = { "action": "connect", "from": "<YOUR_VIRTUAL_NUMBER>", "endpoint": [{ "type": "phone", "number": "<CALL_CAMPAIGNER_PHONE_NUMBER>" }] }
action_when_beep = { "action": "talk", "text": "We tried to reach you, please contact us immediately."}

@app.route("/", methods=["GET", "POST"])
def callback_listener():
    ncco = ""
    if request.is_json and "status" in request.get_json():
        req_json = request.get_json()
        if req_json["status"] == "machine" and "sub_state" in req_json and req_json["sub_state"] == "beep_start":
            ncco = [action_when_beep]
            print(f'status received --> {req_json["status"]}:{req_json["sub_state"]}')
            print(f'response to send --> {ncco}')
        elif req_json["status"] == "human":
            ncco = [action_when_human]
            print(f'status received --> {req_json["status"]}')
            print(f'response to send --> {ncco}')
    else:
        print(f'event received --> {request.data}')
    return (ncco if ncco != "" else "", 200)