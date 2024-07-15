#!/usr/bin/env python3

import json
import os
import re
from pprint import pp

import requests

location = os.environ["CMTEB_LOCATION"]

resp = requests.get(
    "https://cmteb.ro/harta_stare_sistem_termoficare_bucuresti.php",
    headers={"User-Agent": "curl/8.6.0"},
)
for line in resp.text.splitlines():
    m = re.match(r"var passedFeatures_(?P<color>\w+) = (?P<json>.*);$", line.strip())
    if m:
        features = json.loads(m.group("json"))
        for feature in features:
            if feature["denumire"].strip() == location:
                print(m.group("color"))
                pp(feature)
