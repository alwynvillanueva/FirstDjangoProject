from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Tips
from .forms import newguide, contactus
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

def index(request):
	tip_list=Tips.objects.all().order_by('-date_added')
	paginator=Paginator(tip_list,15)
	page = request.GET.get('page')
	try:
		tip=paginator.page(page)
	except PageNotAnInteger:
		tip=paginator.page(1)
	except EmptyPage:
		tip=paginator.page(paginator.num_pages)
	return (render(request,'index.html',{'message':tip}))

def contact(request):
	form_class = contactus
	if request.method == 'POST':
		form = form_class(data=request.POST)
		if form.is_valid():
			contact_name = request.POST.get('name','')
			contact_email = request.POST.get('email','')
			form_content = request.POST.get('content','')
			template = get_template('contact_template.txt')
			context = Context({'contact_name': contact_name,'contact_email': contact_email,'form_content': form_content,})
			content = template.render(context)
			email = EmailMessage("New contact form submission",content,"Trickster" +'',['wynrar@gmail.com'],headers = {'Reply-To': contact_email })
			email.send()
			return HttpResponseRedirect('/mysite/home/')
        return render(request, 'contacts.html', {'form': form_class,})

def submitguide(request):
	form  = newguide(request.POST or None,request.FILES	 or None)
	if request.method == 'POST':
		form = newguide(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/mysite/home/')
	else:
		form = newguide()
	return render(request,'submit.html', {'form':form})
def postdelete(request,id=None):
	Tips.objects.filter(id=id).delete()
	return HttpResponseRedirect('/mysite/home/')