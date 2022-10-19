import streamlit as st
import pandas as pd


import plotly.express as px





import requests
from decimal import Decimal
from collections import defaultdict

from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

import seaborn as sns

import json

with open('identities.json') as f:
   d = json.load(f)
   
   
   
data = d
df = pd.DataFrame.from_dict(data, orient='columns')
#df = pd.DataFrame.from_dict(pd.json_normalize(data), orient='columns')
df = df.T

df['strength'] = df['sum'] - df['attractiveness'] - df['cool'] - df['intelligence'] - df['techSkill']



import barchartrace

df

