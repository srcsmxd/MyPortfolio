from django.shortcuts import render,redirect,get_object_or_404
from .models import BlogCreate
# Create your views here.
def home(request,count=1):
    allblogs = None
    if count == 1:
        allblogs = BlogCreate.objects.all().order_by('blogid')[:10]
    else:
        allblogs = BlogCreate.objects.all().order_by('blogid')[10*(count-1):10*count]
    allcount = BlogCreate.objects.all().count() / 10
    if allcount < 1:
        allcount = 1
    return render(request, 'blog/home.html',{'allblogs':allblogs, 'allcount':range(1,allcount+1)})

def create(request):
    context = None
    if request.method == 'POST':
        blogcreate = BlogCreate()
        blogcreate.blogtitle = request.POST['blogtitle']
        blogcreate.blogdescription = request.POST['blogdescription']
        blogcreate.blogimage = request.FILES['blogimage'] #request.FILES.get('blogimage', False)
        blogcreate.save()
        if blogcreate.blogid != None:
            return redirect('/blog/detail/' + str(blogcreate.blogid))
    else:
        return render(request, 'blog/blogcreate.html',{'created':context})

def detail(request, blog_id):
    blogcreate = get_object_or_404(BlogCreate,pk=blog_id)
    return render(request, 'blog/blogdetail.html', {'blogcreate':blogcreate })
