import locale
import os

from PIL import Image, ImageDraw, ImageFont
from django.utils.text import slugify

from easyparty import settings
from .models import Invite

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def make_invite(pk, slug):
    template_dir = os.path.abspath(settings.BASE_DIR + '/templates/modelos/')
    invite = Invite.objects.get(pk=pk, slug=slug)

    invite.image = Image.open(f'{template_dir}/convites/convite.jpg')
    draw = ImageDraw.Draw(invite.image)
    invite.date_string = invite.date.strftime("%d • %B • %Y")

    font_title = ImageFont.truetype(f'{template_dir}/fonts/Amatic-Bold.ttf', 170)
    font_body = ImageFont.truetype(f'{template_dir}/fonts/Roboto-Medium.ttf', 70)
    w_title, h_title = draw.textsize(invite.name, font=font_title)
    w_date, h_date = draw.textsize(invite.date_string, font=font_body)

    draw.text(
        ((1080 - w_title) / 2, 600),
        text=invite.name,
        fill='#3A317B',
        font=font_title
    )
    draw.text(
        ((1080 - w_date) / 2, 800),
        text=str(invite.date_string),
        fill='#3A317B',
        font=font_body
    )

    invite.file_name = gen_file_name(invite.name)

    return invite


def gen_file_name(text: str):
    return slugify(text)
