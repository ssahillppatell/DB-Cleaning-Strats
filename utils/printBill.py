from fpdf import FPDF

def printBill(data):
	myPdf = FPDF()
	myPdf.add_page()

	myPdf.set_font("Arial", 'B', size = 25)
	myPdf.cell(200, 10, txt = "Bill:", ln = 1, align = 'C')

	myPdf.set_font("Arial", size = 15)
	myPdf.cell(200, 10, txt = f"Customer Name: {data['full_name']}", ln = 1, align = 'L')
	myPdf.cell(200, 10, txt = f"Film Title: {data['film_title']}", ln = 1, align = 'L')
	myPdf.cell(200, 10, txt = f"Rental Date & Time: {data['rental_date']}", ln = 1, align = 'L')
	myPdf.cell(200, 10, txt = f"Rental Duration: {data['rental_duration']} days", ln = 1, align = 'L')
	myPdf.cell(200, 10, txt = f"Cost: $ {data['rental_rate']}", ln = 1, align = 'L')

	myPdf.output('bill.pdf')