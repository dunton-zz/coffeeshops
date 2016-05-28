"""Install catalog"""
from flask import Flask


# Start Flask app object
app = Flask(__name__)


# Import modules 
import catalog.fb_client_secrets
import catalog.final_project
