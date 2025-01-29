from pypdf import PdfWriter
import argparse


def merge_pdfs(pdf_list, output_filename):
    merger = PdfWriter()
    
    for pdf in pdf_list:
        merger.append(pdf)
    
    merger.write(output_filename)
    merger.close()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Merge multiple PDFs into one.")
	parser.add_argument("pdfs", nargs="+", help="List of Pdfs to merge")
	parser.add_argument("-o", "--output", default="merged.pdf", help="output filename (default: merged.pdf)")

	args = parser.parse_args()
	merge_pdfs(args.pdfs, args.output)
	print(f"success -> {args.output}")
