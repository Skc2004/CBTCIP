from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

def cre_rec(name, trans_id, date, items, total_amount, output):
    doc = SimpleDocTemplate(output, pagesize=A4)
    styles = getSampleStyleSheet()
    temp = []
    title = Paragraph("Payment Receipt", styles['Title'])
    temp.append(title)
    temp.append(Spacer(1, 15))
    details = f"Customer Name: {name}<br/>Transaction ID: {trans_id}<br/>Date: {date}"
    para = Paragraph(details, styles['Normal'])
    temp.append(para)
    temp.append(Spacer(1, 15))
    table_columns = [['Item', 'Quantity', 'Price', 'Total_Amount']]
    for item in items:
        table_columns.append([item['name'], item['quantity'], f"Rs.{item['price']:.2f}", f"Rs.{item['total']:.2f}"])
    
    table = Table(table_columns)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.yellow),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.brown),
    ]))
    temp.append(table)
    temp.append(Spacer(1, 15))
    total_para = Paragraph(f"Total Amount: ${total_amount:.2f}", styles['Heading3'])
    temp.append(total_para)
    doc.build(temp)
    
def get_input():
    name = input("Enter customer name: ")
    id = input("Enter transaction ID: ")
    date = input("Enter date (YYYY-MM-DD): ")
    
    items = []
    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        total = quantity * price
        items.append({'name': item_name, 'quantity': quantity, 'price': price, 'total': total})
    
    total_amount = sum(item['total'] for item in items)
    output_file = input("Enter output PDF file name : ")
    output_file=output_file+".pdf"
    
    return name,id, date, items, total_amount, output_file

name,id, date, items, total_amount, output_file = get_input()
cre_rec(name, id, date, items, total_amount, output_file)
