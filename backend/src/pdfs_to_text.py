from pypdf import PdfReader                # Bibliotek för att läsa PDF-filer
from backend.constants import DATA_PATH    # Sökväg (Path-objekt) till mappen med datafiler

def extract_text_from_pdf(path) -> str:
    all_text = ""                          # Samlar all text från PDF:en

    reader = PdfReader(path)               # Öppnar PDF-filen
    for page in reader.pages:              # Går igenom varje sida
        text = page.extract_text()         # Hämtar texten från sidan
        if text:                           # Hoppar över sidor utan text
            all_text += text + "\n"        # Lägger till texten + radbrytning
    return all_text                        # Returnerar all text som en sträng

def export_txt(text, path):
    with open(path, "w") as f:             # Öppnar (eller skapar) filen för skrivning
        f.write(text)                      # Skriver texten till filen


if __name__ == "__main__":                 # Körs bara när filen startas direkt
    for pdf_path in DATA_PATH.glob("*pdf"):            # Hittar alla filer som slutar på "pdf" i DATA_PATH
        pdf_text = extract_text_from_pdf(pdf_path)     # Extraherar texten ur PDF:en

        filename = pdf_path.stem + ".txt"              # Filnamn utan ändelse + ".txt"

        export_txt(pdf_text, DATA_PATH / filename)     # Sparar texten som .txt i samma mapp