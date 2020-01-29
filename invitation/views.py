from PIL import Image, ImageDraw, ImageFont
from django.http import HttpResponse
from django.shortcuts import render

from easyparty import settings
from .models import Invite


def list_invites(request):
    invites = Invite.objects.all()
    return render(request, 'invitation/invites.html', context={'invites': invites})


def download_invite(request, pk):
    invite = Invite.objects.get(pk=pk)
    content = invite.name + str(invite.date)
    image = Image.open(f'{settings.STATIC_ROOT}/convites/convite-revelacao.jpg')
    draw = ImageDraw.Draw(image)

    font_title = ImageFont.truetype(f'{settings.STATIC_ROOT}/fonts/Magneton-Bold.ttf', 70)
    w, h = draw.textsize(content, font=font_title)

    draw.text(
        ((1180 - w) / 2, 700),
        text=content,
        fill='#000',
        font=font_title
    )

    response = HttpResponse(content_type='image/jpeg')
    response['Content-Disposition'] = f'attachment; filename={invite.name}-{invite.date}.jpg'
    image.save(response, 'JPEG')
    return response
