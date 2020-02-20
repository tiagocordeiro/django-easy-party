from io import BytesIO

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .facade import make_invite
from .forms import InviteForm
from .models import Invite


@login_required
def invite_create(request):
    if request.method == 'POST':
        form = InviteForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, "Convite cadastrado.")
                return redirect('invites_list')
        except Exception as e:
            messages.warning(request, f'Ocorreu um erro ao atualizar: {e}')

    else:
        form = InviteForm()

    return render(request, 'invitation/create.html', {'form': form})


@login_required
def invite_update(request, pk):
    invite = get_object_or_404(Invite, pk=pk)

    if request.method == 'POST':
        form = InviteForm(request.POST, instance=invite)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, "Convite atualizado.")
                return redirect('invite_update', pk)
        except Exception as e:
            messages.warning(request, f'Ocorreu um erro ao atualizar: {e}')

    else:
        form = InviteForm(instance=invite)

    return render(request, 'invitation/update.html', {'form': form})


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
    byte.seek(0)

    response = FileResponse(byte, 'rb')
    response['Content-Disposition'] = f'attachment; filename={content.file_name}-{content.date}.jpg'
    return response


@login_required
def invite_share(request, pk):
    invite = get_object_or_404(Invite, pk=pk)
    url = request.build_absolute_uri(reverse('invite_public', kwargs={'pk': pk}))

    return render(request, 'invitation/share.html', {'invite': invite,
                                                     'url': url})


def invite_public(request, pk):
    invite = get_object_or_404(Invite, pk=pk)

    return render(request, 'invitation/public.html', {'invite': invite})
