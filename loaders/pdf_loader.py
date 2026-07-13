from pypdf import PdfReader


def load_pdf_text(file_path):
    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


if __name__ == "__main__":

    pdf_path = r"C:\Users\DELL\Desktop\shubhangi\JD - ML Engineer - Data Scientist.pdf"

    text = load_pdf_text(pdf_path)

    print(f"Total Characters : {len(text)}")

    print()

    print(text[:1000])