from flask import Flask, render_template_string

app = Flask(__name__)

systems = [
    {
        "name": "Web Server",
        "status": "OK",
        "note": "Nginx service is running"
    },
    {
        "name": "Database",
        "status": "Warning",
        "note": "Disk space should be checked"
    },
    {
        "name": "Backup",
        "status": "OK",
        "note": "Last backup completed"
    },
    {
        "name": "Firewall",
        "status": "OK",
        "note": "Rules are active"
    }
]

html = """
<!doctype html>
<html>
<head>
    <title>Secure IT Operations Dashboard</title>
</head>
<body>
    <h1>Secure IT Operations Dashboard</h1>
    <p>DevOps and DevSecOps home lab project.</p>

    <table border="1" cellpadding="8">
        <tr>
            <th>System</th>
            <th>Status</th>
            <th>Note</th>
        </tr>
        {% for system in systems %}
        <tr>
            <td>{{ system.name }}</td>
            <td>{{ system.status }}</td>
            <td>{{ system.note }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html, systems=systems)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
