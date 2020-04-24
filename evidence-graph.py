import flask, stardog, logging
import pandas as pd
from flask import Flask, render_template, request, redirect,jsonify

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/<ark>')
def homepage(ark):

    logger.info('Homepage handling request %s', request)

    try:
        exists, eg_id = eg_exists(ark)
    except:
        logger.error('Ark does not exists')
        return jsonify({'error':'Given ark does not exist.'}),503

    if exists:
        logger.info('Request for existing evidence graph: %s', ark)
        return existing_eg(eg_id)

    logger.info('Creating Evidence Graph for %s', ark)

    try:
        eg = create_eg(ark)
    except:
        logger.error('Failed to create eg for ark: %s',ark)
        return jsonify('error':'Server failed to create evidence graph.'),503

    try:
        eg_id = mint_eg_id(eg)
        add_eg_to_og_id(ark,eg)
    except:
        logger.error('Minting evidence graph failed.')
        return eg
        
    return eg
