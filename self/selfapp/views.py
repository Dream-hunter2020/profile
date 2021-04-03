from django.shortcuts import render

# Create your views here.
import datetime
from django.http import HttpResponse


def welcome(request):
	
	date=datetime.datetime.now()
	hour=int(datetime.datetime.now().hour)
	msg='Hello,Good'
	if hour>0 and hour<12 :
		msg=msg+'Morning'
	elif hour>12 and hour<16:
		msg=msg+'Afternoon'
	elif hour>16 and hour<21:
		msg=msg+'Evening'
	else:
		msg=msg+'Night'
	msg=msg

	my_dict={'date':date,'msg':msg}


	return render(request=request, template_name='selfapp/self.html',context=my_dict)

'''def Education(request):
	msg = 'Hello here is my Education'
	my_dict={'msg':msg}

	return render(request=request, template_name='',context=my_dict)'''