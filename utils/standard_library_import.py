%load_ext autoreload
%autoreload 2

import GoH.verify_model
import gspread
import json
from matplotlib import pyplot as plt
from oauth2client.service_account import ServiceAccountCredentials
import os
import pandas as pd
import seaborn as sns

%matplotlib inline