import PyPDF2
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Descargar datos adicionales de nltk
nltk.download('punkt')
nltk.download('stopwords')

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        num_pages = pdf_reader.numPages
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    return text

def summarize_text(text, num_sentences=3):
    # Tokenizar el texto en oraciones
    sentences = sent_tokenize(text)
    
    # Eliminar palabras vacías
    stop_words = set(stopwords.words('spanish'))
    filtered_sentences = [sentence for sentence in sentences if sentence.lower() not in stop_words]
    
    # Calcular la frecuencia de las palabras
    word_freq = Counter(filtered_sentences)
    
    # Obtener las oraciones más frecuentes
    summary_sentences = word_freq.most_common(num_sentences)
    
    # Construir el resumen
    summary = [sentence[0] for sentence in summary_sentences]
    return ' '.join(summary)

# Ruta del archivo PDF
pdf_path = 'doc.pdf'

# Extraer texto del PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Resumir el texto
summary = summarize_text(pdf_text)
print("Resumen del PDF:")
print(summary)
