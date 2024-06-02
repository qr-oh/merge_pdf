from tkinter import *
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter

# Global Variables
filenames = []


def merge_pdfs(paths):
    pdf_writer = PdfWriter()

    for path in paths:
        pdf_reader = PdfReader(path)
        for page in range(len(pdf_reader.pages)):
            # Add each page to the writer object
            pdf_writer.add_page(pdf_reader.pages[page])

    # Write out the merged PDF
    with open("merged_output.pdf", 'wb') as out:
        pdf_writer.write(out)

    return 1
    
def selectFiles():
    global filenames
    filenames = filedialog.askopenfilenames(title = "Select PDF Files")

def get_output():
    merge_pdfs(filenames)
    
def main():
    # Declare main frame
    main_frame = Tk()
    main_frame.title("Merge PDFs")

    # Set parameters for GUI (x-axis, y-axis)
    main_frame.geometry("180x220")
    main_frame.configure(bg='khaki')
    
    # Widgets within GUI
    #------------------------------------------------------
    # Get required files from user
    prompt = Label(main_frame,
                   text = 'Select PDF files\n to merge:',
                   font=('Arial',12,),
                   bg='khaki')
    # User input - Select files
    select_button = Button(main_frame,
                            text = "Browse Files",
                            font=('Arial',12,),
                            command = selectFiles)
    # User input - Get output
    submit = Button(main_frame,
                    text = "Get Merged PDF",
                    font=('Arial',12,),
                    command = get_output)
    
    # Alignment of widgets
    prompt.grid(row=1, column=1, padx=20, pady=20)
    select_button.grid(row=2, column=1, padx=20, pady=20)
    submit.grid(row=3, column=1, padx=20, pady=20)

    main_frame.mainloop()

if __name__ == "__main__":
    main()
