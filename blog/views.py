from django.shortcuts import render,redirect,get_object_or_404
from .models import BlogCreate
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    username = ''
    if request.GET.get('username') == '' or 'username' not in request.GET:
        allblogs = BlogCreate.objects.all()
    else:
        allblogs = BlogCreate.objects.filter(bloguser=request.GET.get('username'))
        username = request.user.username

    paginator = Paginator(allblogs, 10)
    page = request.GET.get('page')

    allblogs = paginator.get_page(page)

    return render(request, 'blog/home.html',{'allblogs':allblogs,'currentuser':request.user.username,'username':username})

    #allblogs = None
    #if count == 1:
    #    allblogs = BlogCreate.objects.all().order_by('-blogid')[:10]
    #else:
    #   allblogs = BlogCreate.objects.all().order_by('-blogid')[10*(count-1):10*count]
    #allcount = int( BlogCreate.objects.all().count() / 10 )
    #if allcount < 1:
    #    allcount = 1

    #prev = 1
    #if count == 1:
    #    prev = 1
    #else:
    #   prev = count - 1
    
    #next = count + 1
    #if next > allcount + 1:
    #    next = allcount + 1
    #return render(request, 'blog/home.html',{'allblogs':allblogs,'prev':prev,'next':next ,'allcount':range(1,allcount+2)})

def create(request):
    if request.user.is_authenticated:
        context = None
        if request.method == 'POST':
            blogcreate = BlogCreate()
            blogcreate.blogtitle = request.POST['blogtitle']
            blogcreate.blogdescription = request.POST['blogdescription']
            blogcreate.blogimage = request.FILES['blogimage'] #request.FILES.get('blogimage', False)
            blogcreate.bloguser = request.user.username
            blogcreate.save()
            if blogcreate.blogid != None:
                return redirect('/blog/detail/' + str(blogcreate.blogid))
        else:
            return render(request, 'blog/blogcreate.html',{'created':context})
    else:
        return redirect('/accounts/login')

def detail(request, blog_id):
    blogcreate = get_object_or_404(BlogCreate,pk=blog_id)
    return render(request, 'blog/blogdetail.html', {'blogcreate':blogcreate,'currentuser':request.user.username})

def delete(request, blog_id):
    BlogCreate.objects.filter(blogid=blog_id).delete()
    return redirect('/blog/')