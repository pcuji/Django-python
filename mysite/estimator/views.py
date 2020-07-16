from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Choice, Poll
from django.http import HttpResponse ,HttpResponseRedirect
from django.urls import reverse



# Create your views here.
@login_required
def polls_list(request):

    """list all polls """
    polls = Poll.objects.all()
    paginator = Paginator(polls , 5)
    page = request.GET.get('page')
    polls = paginator.get_page(page)
    return render(request, 'estimator/estimator.html', { 'polls': polls })



def poll_detail(request, poll_id ):
    """ this part will allow the user to use certai tools to find out how much a
        a service willcost"""

    # poll= Poll.objects.get(id= poll_id)
    poll= get_object_or_404(Poll,id= poll_id )
    context = {'poll': poll}
    return render(request, 'estimator/tool.html', context)

def poll_vote(request, poll_id ):
    choice_id = request.POST.get('choice')
    poll= get_object_or_404(Poll,id= poll_id )
    if choice_id:
        choice = Choice.objects.get(id=choice_id)
        choice.votes +=1
        choice.save()
    else:
        messages.error(request, 'No choice was found!!')
        return HttpResponseRedirect(reverse('estimator:detail', args= (poll_id,)))
    return render(request, 'estimator/results.html',{'poll': poll})
