import re
import sys
import zipfile

from neo4j.v1 import GraphDatabase, basic_auth
from decouple import config

GRAPHENEDB_BOLT_PASSWORD=config('GRAPHENEDB_BOLT_PASSWORD', default='')
GRAPHENEDB_BOLT_URL=config('GRAPHENEDB_BOLT_URL', default='')
GRAPHENEDB_BOLT_USER=config('GRAPHENEDB_BOLT_USER', default='')
GRAPHENEDB_URL=config('GRAPHENEDB_URL', default='')

NEO4J_BOLT_URL = config('NEO4J_BOLT_URL', default='')
NEO4J_USER = config('NEO4J_USER', default='')
NEO4J_PASSWORD = config('NEO4J_PASSWORD', default='')


def csv_files(filelist):
    regexp = re.compile(r'^.*\.csv$')
    for filename in filelist:
        if regexp.search(filename):
            yield filename

        # statement = "MERGE (u:User {name: {name}, id: {id}, email: {email}})"

class Node(object):

    def clean_line(self, line):
        return re.findall('^(.*)\\r\\n$', line)[0]

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        header_string = self.clean_line(
            kwargs['headers'].decode(encoding='UTF-8'))
        self.headers = header_string.split(',')

    def statement(self, row):
        data_string = self.clean_line(row.decode(encoding='UTF-8'))
        data = data_string.split(',')
        props = []
        for i in range(0, len(self.headers)):
            if self.headers[i] != 'LastName':
                value = data[i] if data[i] else ''
                props.append(' %s: "%s"' % (self.headers[i],value))
        properties = ','.join(props)
        return "MERGE (%s {%s})" % (self.name, properties)


# driver = GraphDatabase.driver(GRAPHENEDB_BOLT_URL, auth=basic_auth(
#     GRAPHENEDB_BOLT_USER, GRAPHENEDB_BOLT_PASSWORD)
# )

driver = GraphDatabase.driver(NEO4J_BOLT_URL, auth=basic_auth(
    NEO4J_USER, NEO4J_PASSWORD)
)

session = driver.session()

NodeNames = {'offender/Offender.csv': 'Tenant',
                'offender/OffenderSentence.csv': 'Sentence',
                'offender/OffenderExit.csv': 'Exit',
                'offender/OffenderReception.csv': 'Reception',
                'offender/OffenderAlias.csv': 'Alias',
            }
with zipfile.ZipFile('oklahoma_offender_data.zip') as z:
    csvfiles = csv_files(z.namelist())
    for csvname in csvfiles:
        sys.stdout.write('%s\n' % csvname)

        with z.open(csvname) as f:

            header_row = next(f)
            node_name = NodeNames[csvname]
            node = Node(name=node_name, headers=header_row)
            for row in f:
                statement = node.statement(row)
                import ipdb; ipdb.set_trace()
                session.run(statement)
                session.sync()


# MATCH (n) DETACH DELETE n
