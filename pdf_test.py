# NORTH METROPOLITAN TAFE
# DIPLOMA IN INFORMATION TECHNOLOGY (ADVANCED NETWORKING)
# ICTPRG443 - APPLY INTERMEDIATE PROGRAMMING

# STUDENT: ALEXANDER THIEN (20093897@tafe.wa.edu.au)
# ASSESSMENT 3: PART A - PDF Manager Test
# This is the unittest for the Python program used to manage *.pdf files

# Import the unittest and OS packages, along with the main pdf.py file
import unittest
import os
from pdf import merge_pdfs, rotate_page, encrypt_pdf, decrypt_pdf, file_path, pdf_files

# Unittest class
class TestPdf(unittest.TestCase):

    # Check directory for merged file
    def test_merge_pdfs(self):
        merge_pdfs(file_path, pdf_files)
        self.assertTrue(os.path.exists(file_path+"\\finalmerged.pdf"))

    # Check directory for rotated file
    def test_rotate_page(self):
        rotate_page(file_path)
        self.assertTrue(os.path.exists(file_path+"\\rotatedPage.pdf"))

    # Check directory for encrypted file
    def test_encrypt_pdf(self):
        encrypt_pdf(file_path)
        self.assertTrue(os.path.exists(file_path+"\\encryptedminutes2.pdf"))
    
    # Check directory for decrypted file
    def test_decrypt_pdf(self):
        decrypt_pdf(file_path)
        self.assertTrue(os.path.exists(file_path+"\\minutes_decrypted.pdf"))

# Call the main function to begin the unittests
if __name__ == '__main__':
    unittest.main()
