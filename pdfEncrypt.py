import sys, getopt
import argparse
import os
import PyPDF2
import getpass

directory = ""
pdf = ""
password = ""

def Main(argv):
    global directory, password, pdf

    try:
        argParser = argparse.ArgumentParser()
        argParser.add_argument("-d","--DIR", type=str, help="Directory where PDF file is located")
        argParser.add_argument("-f","--FILE", type=str, help="PDF File that you want to Encrypt")
        argParser.parse_args()
        opts, args = getopt.getopt(argv,"d:f:")

        for opt, arg in opts:
            if opt == '-d':
                directory = arg
            elif opt == '-f':
                pdf = arg
        
        if directory == "":
            print("Missing Directory. pdfEncrypt.py [-h]")
            sys.exit(2)
        if pdf == "":
            print("Missing File. pdfEncrypt.py [-h]")
            sys.exit(2)
        if not os.path.exists(f'{directory}\\{pdf}'):
            print(f'{pdf} does not exist in {directory}')
            sys.exit(2)
        
        password = getpass.getpass("Enter a Password: ")
        EncryptPDF(pdf,directory,password)

    except getopt.GetoptError:
        print('pdfEncrypt.py [-h]')
        sys.exit(2)

def EncryptPDF(pdfFile, dir, password):
    pdfSplit = pdfFile.split(".")
    pdfFileSecure = f'{pdfSplit[0]}_secured.{pdfSplit[1]}'
    file = open(f'{dir}\\{pdfFile}','rb')
    reader = PyPDF2.PdfReader(file)
    writer = PyPDF2.PdfWriter()
    for pageNum in range(len(reader.pages)):
        writer.add_page(reader.pages[pageNum])

    writer.encrypt(password)
    encryptedPDF = open(f'{dir}\\{pdfFileSecure}','wb')
    writer.write(encryptedPDF)
    encryptedPDF.close()
    print("File was Encrypted.")

if(__name__ == "__main__"):
    Main(sys.argv[1:]) 