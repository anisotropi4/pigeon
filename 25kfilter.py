#!/usr/bin/env python3

import sys
import json
import calendar
from os import path

MONTHS = {v: str(k).zfill(2) for k, v in enumerate(calendar.month_name) if v}

for line in sys.stdin:
    data = json.loads(line.strip())
    if isinstance(data, str):
        continue
    if 'a' not in data:
        continue
    r = data['a']
    if 'value' not in r:
        continue
    if '£25,000' in r['value']:
        u = r['href']
        v = u.split('/').pop()
        v = v.split('.').pop(0)
        v = v.split('-')[-2::][::-1]
        v[-1] = MONTHS[v[-1]]
        q = 'Spend-over-£25000-{}.xlsx'.format(''.join(v))
        s = {'name': q, 'url': r['href']}
        print(json.dumps(s))
