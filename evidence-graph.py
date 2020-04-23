import flask, stardog, logging
import pandas as pd
from flask import Flask, render_template, request, redirect,jsonify

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/<ark>')
def homepage(ark):

    logger.info('Homepage handling request %s', request)

    if eg_exists(ark):
        logger.info('Request for existing evidence graph: %s', ark)
        return existing_eg(ark)

    logger.info('Creating Evidence Graph for %s', ark)
    eg = create_eg(ark)
    id = mint_eg_id(ark)
    add_eg_to_og_id(ark,eg)

    return eg
