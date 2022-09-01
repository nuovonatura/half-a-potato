from asyncio.subprocess import STDOUT
import subprocess
from sys import stdout
from flask import Flask, request, Response

server = Flask(__name__)

SINGLEFILE_EXECUTABLE = "/usr/app/node_modules/single-file-cli/single-file"
BROWSER_PATH = "/usr/bin/chromium-browser"
BROWSER_ARGS = "[\"--no-sandbox\"]"

@server.route('/', methods=['POST'])
def singlefile():
    url = request.form.get('url')
    index = request.form.get('index')
    filename = index + ".html"
    if url:
        p = subprocess.Popen([
            SINGLEFILE_EXECUTABLE,
            '--browser-executable-path=' + BROWSER_PATH,
            "--browser-args='%s'" % BROWSER_ARGS,
            url,
            '--dump-content=false',
            filename,
            ],
            stdout=subprocess.PIPE)
    else:
        return Response('Error: url parameter not found.',
                        status=500)
    singlefile_html = p.stdout.read()
    return Response(
        singlefile_html,
        mimetype="text/plain",
    )


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=80)
