import fitz
from pathlib import Path

# PDF
input_folder = Path(r"E:\pdf")

# JPG
output_folder = Path(r"E:\jpeg")
output_folder.mkdir(exist_ok=True)

counter = 1

for pdf_file in sorted(input_folder.glob("*.pdf")):
    doc = fitz.open(pdf_file)

    for page_num in range(len(doc)):
        page = doc[page_num]

        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))

        # 0001.jpg, 0002.jpg, ...
        output_path = output_folder / f"{counter:04d}.jpg"
        pix.save(output_path)

        counter += 1

    doc.close()

print(f"แปลงเสร็จแล้ว {counter - 1} หน้า")