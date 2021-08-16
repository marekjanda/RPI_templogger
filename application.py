# Flask app to work as a web socket for for data transmission
import os

from flask import Flask, session, jsonify, redirect, request
from flask_session import Session
from flask_api import status
import requests

app = Flask(__name__)