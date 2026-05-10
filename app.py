from flask import Flask

app = Flask(__name__)

@app.route("/")
def home ():
	return """
	<h1>Secure IT Operations Dashboard</h1>
	<p>DevOps and DevSecOps home lab project.</p>
	<ul>
		<li>Web Server: OK</li>
		<li>Web Database: Warning</li>
		<li>Web Backup: OK</li>
		<li>Firewall: OK</li>
	</ul>
	"""

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
