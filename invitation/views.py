from io import BytesIO

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render

from .facade import make_invite
from .models import Invite


@login_required
def invites_list(request):
    all_invites = Invite.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(all_invites, 10)
    try:
        invites = paginator.page(page)
    except PageNotAnInteger:
        invites = paginator.page(1)
    except EmptyPage:
        invites = paginator.page(paginator.num_pages)
    return render(request, 'invitation/invites.html', context={'invites': invites})


def invite_download_jpg(request, pk):
    content = make_invite(pk=pk)

    byte = BytesIO()
    content.image.save(byte, 'JPEG')

    response = HttpResponse(byte.getvalue(), content_type='image/jpeg')
    response['Content-Disposition'] = f'attachment; filename={content.file_name}-{content.date}.jpg'
    return response
