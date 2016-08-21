from django.shortcuts import render
#haciendo la vista

#def archive (request)


#definiendo la vista de suma 
def sumar(request):

	a=9
	b=4
	c=a+b
	hola="cualquier cosa hahahaha"
	return render(request, 'sumar.html', {'hola': hola})

# Create your views here.
