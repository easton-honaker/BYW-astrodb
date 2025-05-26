from astrodb_utils import load_astrodb
from astrodb_utils.sources import ingest_source, ingest_name
from astrodb_utils.publications import ingest_publication
from astrodb_utils.photometry import ingest_photometry

# Load the database
db_file = "BYW_HON.sqlite"
felis_schema = "schema/schema.yaml"

reference_tables = [
    "Publications",
    "Telescopes"
    "Instruments",
    "PhotometryFilters",
    "Versions",
    "RegimeList",
    "ParameterList",
    "SourceTypeList"
]

db = load_astrodb(
    db_file,
    recreatedb=True,
    felis_schema=felis_schema,
    reference_tables=reference_tables,
)

def ingest_CWISEJ_1721(db): ##- question: is it better to leave columns as "None" or just not import them?
    ingest_publication(
        db,
        description="HONAKER BYW sample",
        reference="HONA26",
        ignore_ads=True,
    )

    ingest_source(db,
                  source = "CWISEJ172138.58-064311.4",
                  reference = "HONA26",
                  ra = 260.4107662,
                  dec = -6.7198597,
                  epoch = 2000.0,
                  equinox = "J2000",
                  comment="CatWISE2020",
                  ra_col_name = "ra_deg",
                  dec_col_name = "dec_deg",
                  epoch_col_name = "epoch_year"
                  )
    
    ingest_name(db,
                 source = "CWISEJ172138.58-064311.4",
                 other_name = "1712-0543")
    

def ingest_photometry_CWISEJ_1721(db):
    ingest_publication(db, 
                       reference="Goodstuff", 
                       description="BYW goodstuff sheet",
                       ignore_ads=True)
    

    ingest_photometry(db,
                      source = "CWISEJ172138.58-064311.4",
                      band="VISTA.J",
                      magnitude = 16.444,
                      magnitude_error = 0.011,
                      telescope = "VISTA",
                      reference = "Goodstuff")
    ingest_photometry(db,
                      source = "CWISEJ172138.58-064311.4",
                      band="2MASS.H",
                      magnitude = 15.424,
                      magnitude_error = 0.096,
                      telescope = "2MASSS",
                      reference = "Goodstuff")
    ingest_photometry(db,
                      source = "CWISEJ172138.58-064311.4",
                      band="VISTA.Ks",
                      magnitude = 14.978,
                      magnitude_error = 0.012,
                      telescope = "VISTA",
                      reference = "Goodstuff")
    
def ingest_propermotions_CWISEJ_1721(db):
    ingest_publication(db, 
                       reference="Goodstuff", 
                       description="BYW goodstuff sheet",
                       ignore_ads=True)   
    propermotiondata = [
        {
            "source": "CWISEJ172138.58-064311.4",
            "pm_ra": 115.13,
            "pm_ra_error": 8.7,
            "pm_dec": -97.56,
            "pm_dec_error": 9.7,
            "reference": "Goodstuff"
        }
    ]

    with db.engine.connect() as conn:
        conn.execute(db.ProperMotions.insert().values(propermotiondata))
        conn.commit()

DB_SAVE = True

ingest_CWISEJ_1721(db)
#ingest_photometry_CWISEJ_1721(db)
#ingest_propermotions_CWISEJ_1721(db)


if DB_SAVE:
    db.save_database("data/")