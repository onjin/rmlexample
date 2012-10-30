# -*- coding: utf-8 -*-
from z3c.rml import rml2pdf
import reportlab.rl_config
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
import os


"""Configure reportlab, add fonts and map them"""

reportlab.rl_config.warnOnMissingFontGlyphs = 0

font_dir = os.path.join(os.path.dirname(__file__), 'fonts')

# add necessary fonts
pdfmetrics.registerFont(TTFont('DejaVuSans',
    os.path.join(font_dir, 'DejaVuSans.ttf'), 'UTF-8'))
pdfmetrics.registerFont(TTFont('DejaVuSans-Bold',
    os.path.join(font_dir, 'DejaVuSans-Bold.ttf'), 'UTF-8'))
pdfmetrics.registerFont(TTFont('DejaVuSans-Oblique',
    os.path.join(font_dir, 'DejaVuSans-Oblique.ttf'), 'UTF-8'))
pdfmetrics.registerFont(TTFont('DejaVuSans-BoldOblique',
    os.path.join(font_dir, 'DejaVuSans-BoldOblique.ttf'), 'UTF-8'))

# and map them
addMapping('DejaVuSans', 0, 0, 'DejaVuSans')
addMapping('DejaVuSans-Bold', 1, 0, 'DejaVuSans')
addMapping('DejaVuSans-Oblique', 0, 1, 'DejaVuSans')
addMapping('DejaVuSans-BoldOblique', 1, 1, 'DejaVuSans')



with open('example.rml') as rml:
    data = rml.read()


pdf = rml2pdf.parseString(data.decode('utf-8'))

with open('example.pdf', 'w') as output:
    output.write(pdf.read())
