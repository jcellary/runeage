from flask import Flask

app = Flask(__name__)
from app import api

#use for signing cookies
app.secret_key = 's_%17p-chevg1i_igdv7))b!6-^ucf7-fu55%*9*wr6)#-_ni4'