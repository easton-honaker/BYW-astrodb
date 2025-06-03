# copy over from single source example

from astrodb_utils import load_astrodb
from astrodb_utils.sources import ingest_source, ingest_name
from astrodb_utils.publications import ingest_publication
from astrodb_utils.photometry import ingest_photometry
import astropy
from astropy.table import Table

# Load the database
db_file = "BYW_HON.sqlite"
felis_schema = "schema/schema.yaml"

DB_SAVE = False
DB_RECREATE = True

reference_tables = [
    "Publications",
    "Telescopes",
    "Instruments",
    "PhotometryFilters",
    "RegimeList",
    "ParameterList",
    "SourceTypeList",
    "Versions"
]

db = load_astrodb(
    db_file,
    recreatedb=DB_RECREATE,
    felis_schema=felis_schema,
    reference_tables=reference_tables,
)


# unlike single source, let's loop by table.

# first check if we have the relevant publications. for now, manually check the two that are important for the sources

def ingest_BYWsample_pubs(db):
    #check if hona26 and goodstuff already in db. add if not
    exists_hona26 = find_publication(db, "HONA26")
    if exists_hona26 == False:
        ingest_publication(
            db,
            description="HONAKER BYW sample",
            reference="HONA26",
            ignore_ads=True,
        )

    exists_goodstuff = find_publication(db, "Goodstuff")
    if exists_goodstuff == False:
        ingest_publication(db, 
                           reference="Goodstuff", 
                           description="BYW goodstuff sheet",
                           ignore_ads=True)

def ingest_BYWsample_source(db):
    #loop over all sources and ingest their source and name
    ingest_source(db,
                  source = source_name,
                  ra =source_ra,
                  dec = source_dec,
                  equinox = "J2000",
                  comment = "CatWISE2020",
                  reference= "HONA26",
                  raise_error=False,
                  )
    
    ingest_name(db,
                source = source_name,
                other_name = shortname
                )
    
#read in the partial dataset (first 20)
BYWsubsample = Table.read('BYWfirst20.csv',format='csv')

# Loop through the subsample and ingest each source
for entry in BYWsubsample:
    source_name = 'CWISE '+str(entry['Jname'])

    source_ra = entry['catWISE RA']
    source_dec = entry['catWISE Dec']
    shortname = entry['shortname']
    
    # Ingest the source and name
    ingest_BYWsample_source(db)


if DB_SAVE:
    db.save_database("data/")