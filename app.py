import subprocess
import datetime
import getpass
import pytz
from flask import Flask

app = Flask(__name__)

@app.route("/htop")
def htop():
    my_name = "Vaibhav_Pratap_Singh"
    username = getpass.getuser()
    ist_tz = pytz.timezone("Asia/Kolkata")
    ist_time = datetime.datetime.now(ist_tz).strftime("%Y-%m-%d %H:%M:%S %Z")
    top_output = subprocess.getoutput("top -b -n 1")

    response_html = f"""
    <h1>/htop Endpoint</h1>
    <p><b>Name:</b> {my_name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {ist_time}</p>
    <pre>{top_output}</pre>
    """
    return response_html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
