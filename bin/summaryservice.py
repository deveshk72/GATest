# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 17:19:50 2020

@author: saz2n
"""

import flask
from flask import Flask, request
from summarizer import SummarizeDoc

app = Flask(__name__)

@app.route('/get_summary',methods=['GET'])
def findSummary():
    summarizeObj = SummarizeDoc()
    summary = summarizeObj.findSummary()
    return summary

app.run('localhost',8023)