import lancedb                                         # Vektordatabas (lagras lokalt i en mapp)
import time                                            # Används för att pausa mellan filer
from backend.constants import VECTOR_DATABASE_PATH, DATA_PATH   
from backend.data_models import Article
from pathlib import Path                               

def setup_vector_db(path):
    Path(path).mkdir(exist_ok=True)                    # Skapar databasmappen om den inte finns
    vector_db = lancedb.connect(uri = path)            # Ansluter till databasen i mappen
    vector_db.create_table("articles", schema=Article, exist_ok=True)  # Skapar tabellen "articles" om den inte redan finns

    return vector_db                                   # Returnerar databasanslutningen

def ingest_docs_to_vector_db(table):
    for file in DATA_PATH.glob("*.txt"):               # Går igenom alla .txt-filer i datamappen
        with open(file, "r") as f:                     # Öppnar filen för läsning
            content = f.read()                         # Läser hela innehållet

        doc_id = file.stem                             # Använder filnamnet (utan ändelse) som ID

        # idempotent
        table.delete(f"doc_id = '{doc_id}'")           # Tar bort gammal version av dokumentet (undviker dubbletter)

        table.add([                                    # Lägger till dokumentet i tabellen
            {
                "doc_id": doc_id,                      # Unikt ID
                "filepath": str(file),                 # Fullständig sökväg
                "filename": file.stem,                 # Filnamn utan ändelse
                "content": content                     # Textinnehållet
            }
        ])
        print(table.to_pandas().shape)
        print(table.to_pandas()["filename"])           # Skriver ut alla filnamn i tabellen (för kontroll)
        time.sleep(30)                                 # Pausar 30 sekunder (troligen för att undvika API-gränser)

if __name__ == "__main__":                             # Körs bara när filen startas direkt
    vector_db = setup_vector_db(VECTOR_DATABASE_PATH)  # Skapar/ansluter till databasen
    ingest_docs_to_vector_db(vector_db["articles"])    # Läser in alla dokument i tabellen "articles"