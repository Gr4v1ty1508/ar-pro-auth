from flask import Flask, request, jsonify

app = Flask(__name__)

HWIDS = ["8BB90611F7D212AE"]  # add HWIDs here

@app.route("/check")
def check():
    hwid = request.args.get("hwid", "")
    return jsonify({"allowed": hwid in HWIDS})

if __name__ == "__main__":
    app.run()
