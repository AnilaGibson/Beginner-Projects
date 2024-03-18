import pyttsx3
import PyPDF2

def pdf_to_audio_book(pdf_file_path):
    # Open the PDF file
    book = open(pdf_file_path, 'rb')

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(book)
    num_pages = pdf_reader.numPages

    # Initialize the text-to-speech engine
    speaker = pyttsx3.init()

    # Extract text from each page and convert to audio
    for page_num in range(num_pages):
        page = pdf_reader.getPage(page_num)
        text = page.extractText()

        # Read the text aloud
        speaker.say(text)
        speaker.runAndWait()

    # Close the PDF file
    book.close()

if __name__ == "__main__":
    # Specify the path to the PDF file
    pdf_file_path = 'file.pdf'  # Replace 'file.pdf' with the path to your PDF file
    pdf_to_audio_book(pdf_file_path)
