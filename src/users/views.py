from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import SignUpForm, ContactForm

# Create your views here.
def home(request):
	title = "Welcome"
	
	#add a form
	if request.method == 'POST':
		print request.POST
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form": form,
	}
	if form.is_valid():
		#form.save()
		instance = form.save(commit=False)
		# full_name = form.cleaned_data.get('full_name')
		# if not
		instance.save()
		context = {
			"title": "Thanks!"
		}
		# print instance.email
		# print instance.timestamp

	
	return render(request, "home.html", context)

def myprofile(request):
	title = "My Profile"
	title_align_center = True

	context = {
	"title": title,
	"title_align_center":title_align_center,
	}
	return render(request, "myprofile.html", context)

def myprojects(request):
	title = "My Projects"
	title_align_center = True

	context = {
	"title": title,
	"title_align_center":title_align_center,
	}
	return render(request, "myprojects.html", context)

	
def contact(request):
	title = "Have feedback? Leave us a message!"
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value
			#print form.cleaned_data.get(key)
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")

		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email,'nattanichpoon@gmail.com']
		contact_message = "%s: %s via %s"%(
			form_full_name, 
			form_message, 
			form_email)
		some_html_message = """
		<h2> %s </h2>
		<h3> - %s  </h3>
		<p> %s </p>
		""" %(form_message,form_full_name, form_email)
	
		send_mail(subject, 
			contact_message, 
			from_email, 
			to_email, html_message=some_html_message,
			fail_silently=True)

	context = {
		"form": form,
		"title": title,
		"title_align_center": title_align_center,

	}
	return render(request, "contact.html", context)