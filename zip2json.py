import csv
import io
import json
import re
import sys
import zipfile


def csv_files(filelist):
    regexp = re.compile(r'^.*\.csv$')
    for filename in filelist:
        if regexp.search(filename):
            yield filename


with zipfile.ZipFile('oklahoma_offender_data.zip') as z:
    csvfiles = csv_files(z.namelist())
    for csvname in csvfiles:
        with z.open(csvname) as f:
            sys.stdout.write('\n')
            print(csvname)
            x = 0
            for line in f:
                if x % 500 == 0:
                    sys.stdout.write('.')
                x += 1
