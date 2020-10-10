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

    try:
        invite.image = Image.open(invite.invite_template.background_image)
    except ValueError:
        invite.image = Image.open(f'{template_dir}/convites/convite.jpg')

    draw = ImageDraw.Draw(invite.image)
    invite.date_string = invite.date.strftime("%d • %B • %Y")

    try:
        font_title = ImageFont.truetype(invite.invite_template.title_font,
                                        invite.invite_template.title_size)
    except ValueError:
        font_title = ImageFont.truetype(
            f'{template_dir}/fonts/Amatic-Bold.ttf', 170)

    try:
        font_body = ImageFont.truetype(invite.invite_template.body_font,
                                       invite.invite_template.body_size)
    except ValueError:
        font_body = ImageFont.truetype(
            f'{template_dir}/fonts/Roboto-Medium.ttf', 70)

    w_title, h_title = draw.textsize(invite.name, font=font_title)
    w_date, h_date = draw.textsize(invite.date_string, font=font_body)

    draw.text(
        ((invite.image.width - w_title) / 2, invite.invite_template.title_pos),
        text=invite.name,
        fill='#3A317B',
        font=font_title
    )
    draw.text(
        ((invite.image.width - w_date) / 2, invite.invite_template.body_pos),
        text=str(invite.date_string),
        fill='#3A317B',
        font=font_body
    )

    invite.file_name = gen_file_name(invite.name)

    return invite


def gen_file_name(text: str):
    return slugify(text)
