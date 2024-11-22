# NORTH METROPOLITAN TAFE
# DIPLOMA IN INFORMATION TECHNOLOGY (ADVANCED NETWORKING)
# ICTPRG443 - APPLY INTERMEDIATE PROGRAMMING

# STUDENT: ALEXANDER THIEN (20093897@tafe.wa.edu.au)
# ASSESSMENT 3: PART A - PDF Manager
# This is the Python program used to manage *.pdf files

# Import the PyPDF2 package and dependencies
import os
#from PyPDF import PdfMerger, PdfReader, PdfWriter
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

# Define the file path
file_path = os.getcwd()

# Define the list of files to be managed
pdf_files = ["encrypted.pdf", "meetingminutes.pdf", "meetingminutes2.pdf", "watermark.pdf"]



# Merge targeted PDF files into single PDF file function
def merge_pdfs(file_path, pdf_files):
    """The merge_pdfs function merges multiple PDF documents, creating a new single document. Arguments: pdf1, pdf2"""
    merger = PdfMerger()

    # Iterate through available files
    for files in pdf_files:
        if files.startswith("meetingminutes"):
            merger.append(files)
    
    # Save the merged file
    merger.write("finalmerged.pdf")
    
    # Close the merged file
    merger.close()
    
    print("Documents have been merged.")

# Rotate page in a pdf file function
def rotate_page(file_path):
    """The rotate_page function will rotate a page from a specified document 90 degrees. Arguments: file_path, file"""
    with open(file_path+"\\watermark.pdf", "rb") as rotatedfile:

        # Read the PDF file, select a page from the document, and rotate the page
        file_handler = PdfReader(rotatedfile)
        page = file_handler.pages[0]
        page.rotate(90)

        # Add the rotated page to a new PDF document
        writer = PdfWriter()
        writer.add_page(page)

        # Save the new PDF document with the now rotated page
        with open(file_path+"\\rotatedPage.pdf", "wb") as resultPdfFile:
            writer.write(resultPdfFile)
        
        # Confirm page rotate
        print("Page has been rotated.")

# Encrypt a PDF file function
def encrypt_pdf(file_path):
    """The encrypt_pdf function decrypts PDF files and stores the decrypted PDF file in a new document. Arguments: file_path"""
    with open(file_path+"\\meetingminutes.pdf", "rb") as minutesFile:

        # Read the PDF file
        file_handler = PdfReader(minutesFile)
        # Create a pdfWrite object
        writer = PdfWriter()

        # Iterate through the pages of the file and add each page to a new file
        for pageNum in range(len(file_handler.pages)):
            writer.add_page(file_handler.pages[pageNum])
        
        # Set the password
        writer.encrypt("zerocool")

        # Save the encypted file
        with open(file_path+"\\encryptedminutes2.pdf", "wb") as resultPdf:
            writer.write(resultPdf)
            resultPdf.close()
        
        print("Document has been encrypted.")

# Decrypt a PDF file function
def decrypt_pdf(file_path):
    """The decrypt_pdf function will take an encrypted PDF file and decrypt it in a new file. Arguments: file_path"""
    with open(file_path+"\\encryptedminutes.pdf", "rb") as decryptFile:
        
        # Read the PDF file
        file_handler = PdfReader(decryptFile)
        
        # Creating an empty PDF file
        writer = PdfWriter()
        
        # Set password for decryption
        file_handler.decrypt("swordfish")
        
        # Iterate through pages of the file and add them to the created PDF document
        for pageNum in range(len(file_handler.pages)):
            writer.add_page(file_handler.pages[pageNum])
        
        # Save the decrypted file
        with open(file_path + "\\minutes_decrypted.pdf", "wb") as resultPdf:
            writer.write(resultPdf)
            resultPdf.close()
        
        print("Document has been decrypted.")
        

if __name__ == '__main__':
    
    merge_pdfs(file_path, ["meetingminutes.pdf", "meetingminutes2.pdf"])
    rotate_page(file_path)
    encrypt_pdf(file_path)
    decrypt_pdf(file_path)
    
# Sources: https://www.geeksforgeeks.org/encrypt-and-decrypt-pdf-using-pypdf2/
