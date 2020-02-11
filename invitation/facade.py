import locale

from PIL import Image, ImageDraw, ImageFont
from django.templatetags.static import static
from django.utils.text import slugify

from easyparty import settings
from .models import Invite

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def make_invite(pk):
    invite = Invite.objects.get(pk=pk)
    invite_image = invite.invite_template.background_image.url
    invite_font_title = invite.invite_template.title_font.url
    invite_font_body = invite.invite_template.body_font.url
    print(invite_font_body)
    print(invite_font_title)
    print(invite_image)
    print(static('convites/convite.jpg'))
    print(f'{settings.STATIC_ROOT}/convites/convite.jpg')
    invite.image = Image.open(invite_image)
    draw = ImageDraw.Draw(invite.image)
    invite.date_string = invite.date.strftime("%d • %B • %Y")

    font_title = ImageFont.truetype(invite_font_title, 170)
    font_body = ImageFont.truetype(invite_font_body, 70)
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
