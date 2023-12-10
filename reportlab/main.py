from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart

c = canvas.Canvas("my_report.pdf")

c.line(10*mm, 20*mm, 50*mm, 60*mm)
c.rect(100*mm, 100*mm, 50*mm, 70*mm)
c.circle(200*mm, 200*mm, 30*mm)

c.setFont("Helvetica", 12)
c.drawString(10*mm, 10*mm, "Hello, World!")
c.setFillColor(colors.red)
c.drawString(100*mm, 100*mm, "This is bold text.")

# Define chart data
data = [(1, 2, 3, 4, 5)]
chart = VerticalBarChart()
chart.data = data

# Draw the chart
drawing = Drawing(100, 100)
drawing.add(chart)
drawing.drawOn(c, 100*mm, 100*mm)

c.save()