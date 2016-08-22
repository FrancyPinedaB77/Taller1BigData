from django.shortcuts import render
#haciendo la vista

#def archive (request)


#definiendo la vista de suma 
def sumar(request):

	a=9
	b=4
	c=a+b
	x="cualquier cosa hahahaha"
	return render(request, 'sumar.html', {'x': x})

# Create your views here.
