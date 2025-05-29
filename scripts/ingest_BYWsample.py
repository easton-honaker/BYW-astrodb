# copy over from single source example

from astrodb_utils import load_astrodb
from astrodb_utils.sources import ingest_source, ingest_name
from astrodb_utils.publications import ingest_publication
from astrodb_utils.photometry import ingest_photometry

# Load the database
db_file = "BYW_HON.sqlite"
felis_schema = "schema/schema.yaml"

DB_SAVE = True
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


# unlike single source, let's loop by table

def ingest_BYWsample_pubs(db):
    #check if hona26 and goodstuff already in db. add if not
    exists_hona26 = find_publication(db, "HONA26")
    if exists_hona26 == True:
        continue
    elif exists_hona26 == False:
        ingest_publication(
            db,
            description="HONAKER BYW sample",
            reference="HONA26",
            ignore_ads=True,
        )

    exists_goodstuff = find_publication(db, "Goodstuff")
    if exists_goodstuff == True:
        continue
    elif exists_goodstuff == False:
        ingest_publication(db, 
                           reference="Goodstuff", 
                           description="BYW goodstuff sheet",
                           ignore_ads=True)

def ingest_BYWsample_sources(db):
    #loop over all sources and ingest their source and name
    ingest_source(db,
                  source = ,
                  ra =,
                  dec = ,
                  equinox = "J2000",
                  comment = "CatWISE2020"
                  )
    
    ingest_name(db,
                source = ,
                other_name =
                )
    