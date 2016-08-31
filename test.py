from django.template import Context, loader
from django.http import HttpResponse
from jobs.models import Job
 
from django.template import Context, loader
from django.http import HttpResponse
from jobs.models import Job
 
def index(request):
    object_list = Job.objects.order_by('-pub_date')[:10]
    t = loader.get_template('jobs/job_list.html')
    c = Context({
        'object_list': object_list,
    })
    return HttpResponse(t.render(c))