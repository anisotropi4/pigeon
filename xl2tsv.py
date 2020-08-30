#!/usr/bin/env python3

import pandas as pd
import argparse
import os
import sys

PARSER = argparse.ArgumentParser(description='Dump xls(x) files tab(s) to .tsv files, to the (default output) path')

PARSER.add_argument('inputfiles', type=str, nargs='*', help='name of xls-file to process')

TABGROUP = PARSER.add_mutually_exclusive_group()

TABGROUP.add_argument('--tabnames', dest='tabnames', action='store_true',
                    default=False, help='dump name of tabs')

TABGROUP.add_argument('--tab', type=str, dest='tab', default=None,
                    help='name of tab to process')

TABGROUP.add_argument('--ffill', dest='ffill', action='store_true',
                      default=False, help='forward fill missing values')

FILEGROUP = PARSER.add_mutually_exclusive_group()

FILEGROUP.add_argument('--path', dest='path', type=str, default='output',
                    help='output directory file')

FILEGROUP.add_argument('--stdout', dest='stdout', action='store_true',
                    default=False, help='dump a tab to stdout')

PARSER.add_argument('--sourcename', dest='sourcename', action='store_true',
                    default=False, help='prepend filename to output tab file')

ARGS = PARSER.parse_args()

PATH = ARGS.path

if not os.path.exists(PATH):
    os.makedirs(PATH)

if ARGS.tabnames:
    for filename in ARGS.inputfiles:
        if len(ARGS.inputfiles) > 1:
            print(filename)
        df = pd.read_excel(filename, None)
        print('\t'.join(df.keys()))
    sys.exit(0)

def get_filebase(filepath):
    print(filepath)
    r = os.path.basename(filepath)
    if '.' in filepath:
        r = r.rsplit('.', 1)[0]
    return r + ':'

for filename in ARGS.inputfiles:    
    if ARGS.tab:
        tab = ARGS.tab
        filebase = ''
        if ARGS.sourcename:
            filebase = get_filebase(filename)
        try:
            df = pd.read_excel(filename, tab)
            if ARGS.ffill:
                df = df.fillna(method='ffill')
            if ARGS.stdout:
                df.to_csv(sys.stdout, index=False, sep='\t')     
            else:
                df.to_csv('{}/{}{}.tsv'.format(PATH, filebase, tab), index=False, sep='\t')
        except KeyError:
            pass
    else:
        df = pd.read_excel(filename, None)
        filebase = ''
        if ARGS.sourcename:
            filebase = get_filebase(filename)
        for tab in df.keys():
            if ARGS.ffill:
                df[tab] = df[tab].fillna(method='ffill')
            df[tab].to_csv('{}/{}{}.tsv'.format(PATH, filebase, tab), index=False, sep='\t')

