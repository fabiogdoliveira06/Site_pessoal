from django.shortcuts import render
# Create your views here.

posts = [
	{
		'author' : 'fabio',
		'title' : 'blog post 1',
		'content' : 'first post',
		'date_posted' : 'August 27, 2018'
	},
	{
		'author' : 'lyvia',
		'title' : 'blog post 2',
		'content' : 'second post',
		'date_posted' : 'August 30, 2018'
	}

]

def home(request):
	context = {
		'posts' : posts
	}
	return render(request, 'personalpage/home.html', context)

def about(request):
	return render(request, 'personalpage/about.html')	

def professional(request):
	return render(request, 'personalpage/professional.html')	
