from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

w, h = A4
c = canvas.Canvas("shapes.pdf", pagesize=A4)
c.drawString(30, h - 50, "Line")
x = 120
y = h - 45
c.line(x, y, x + 100, y)
c.drawString(30, h - 100, "Rectangle")
c.rect(x, h - 120, 100, 50)
c.drawString(30, h - 170, "Circle")
c.circle(170, h - 165, 20)
c.drawString(30, h - 240, "Ellipse")
c.ellipse(x, y - 170, x + 100, y - 220)
c.showPage()
c.save()