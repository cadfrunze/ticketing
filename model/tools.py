import random
import time
from qrcode import QRCode
from qrcode.constants import ERROR_CORRECT_L
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from io import BytesIO
import os


def generare_ticket()->str:
    """Generare serie ticket"""
    LETTERS:str = "qwertyuiopasdfghjklzxcvbnm"
    begin:int = random.randint(1, 2)
    serie_ticket:str = ''
    if begin == 1:
        while len(serie_ticket) < 10:
            serie_ticket += random.choice(LETTERS.upper())
            if len(serie_ticket) == 3 or len(serie_ticket) == 7:
                serie_ticket += '-'
            else: serie_ticket += str(random.randint(1, 9))
        serie_ticket += random.choice(LETTERS.upper())
    else:
        while len(serie_ticket) < 10:
            serie_ticket += str(random.randint(1, 9))
            if len(serie_ticket) == 3 or len(serie_ticket) == 7:
                serie_ticket += '-'
            else: serie_ticket += random.choice(LETTERS.upper())
        serie_ticket += str(random.randint(1, 9))
    return serie_ticket

def extragere_numar()->int:
    return random.randint(1, 21)
    # return 10
    # return 20
    # return 1


def bon_fiscal(
        nume:str,
        prenume:str,
        cnp:str,
        email:str,
        tip_ticket: str,
        nr_bilete: int,
        serie_ticket:str,
        premiu: str,
        nr_extras: str
)->None:


    qr = QRCode(
        version=1,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(serie_ticket)
    # qr.add_data(client_final["nume"])
    # qr.add_data(client_final["prenume"])
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    qr_buffer = BytesIO()
    img.save(qr_buffer, format="PNG")
    qr_buffer.seek(0)

    pdf_file = f"{nume.lower()}-{prenume.lower()}.pdf"
    pdf_canvas = canvas.Canvas(filename=pdf_file)

    x: int = 200
    y: int = 600

    textul: list = [
        f"Nume: {nume.upper()}",
        f"Prenume: {prenume.upper()}",
        f"CNP: {cnp}",
        f"Email: {email}",
        f"Tip Ticket: {tip_ticket.upper()}",
        f"Nr bilete achizitionate: {nr_bilete}",
        f"Serie ticket: {serie_ticket}",
        f"Premiu: {premiu}",
        f"Nr. extras: {nr_extras}"
    ]

    for linie in textul:
        pdf_canvas.drawString(x, y, linie)
        y = y - 15

    image_reader = ImageReader(qr_buffer)
    pdf_canvas.drawImage(image_reader, 100, 650, width=150, height=150)

    pdf_canvas.save()
    time.sleep(1)
    os.startfile(f"{nume.lower()}-{prenume.lower()}.pdf")