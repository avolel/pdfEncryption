# pdfEncrypt

A simple command-line tool to password-encrypt PDF files using Python.

## Description

`pdfEncrypt.py` takes an existing PDF file and produces a new, password-protected copy of it. The original file is left untouched, and the encrypted version is saved alongside it with a `_secured` suffix (e.g., `document_secured.pdf`).

## Requirements

- Python 3.x
- [PyPDF2](https://pypi.org/project/PyPDF2/)

Install the dependency with:

```bash
pip install PyPDF2
```

## Usage

```bash
python pdfEncrypt.py -d <directory> -f <filename>
```

### Arguments

| Flag | Long Form | Description |
|------|-----------|-------------|
| `-d` | `--DIR`  | Path to the directory containing the PDF file |
| `-f` | `--FILE` | Name of the PDF file to encrypt |
| `-h` | `--help` | Show help message |

You will be prompted to enter a password securely after the arguments are validated.

## Example

```bash
python pdfEncrypt.py -d "C:\Users\John\Documents" -f "report.pdf"
```

**Output:**

```
Enter a Password:
File was Encrypted.
```

This will create `report_secured.pdf` in the same directory as the original file.

## Notes

- The original PDF is **not** modified. A new file with the `_secured` suffix is created.
- The password prompt uses `getpass`, so the password will not be visible as you type it.
- The script currently uses Windows-style path separators (`\`). If running on macOS or Linux, update the path separator to `/`.
