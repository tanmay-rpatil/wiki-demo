from django.shortcuts import render, redirect
from django.http import Http404, QueryDict
from encyclopedia.models import Entry
import random


def index(request):
    entries=[]
    for entry in Entry.objects.all():
        entries.append(entry.title)
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

def article(request, title):
    # md = markdown.Markdown()
    try:
        entry = Entry.objects.get(title__exact=title)
    except:
        raise Http404("Article does not exist")     
    
    # content = md.convert(content)
    return render(request,"encyclopedia/article.html",{
        "title": title,
        "content": entry.content
    } )

def search(request):
    name = request.GET.get('q')
    options = []
    valid = Entry.objects.filter(title__contains=name)
    for entry in valid:
        options.append(entry.title)
    print(options)
    return render(request, "encyclopedia/results.html", {
        "content": options
    })

def randompage(request):
    lst=[]
    for entry in Entry.objects.all():
        lst.append(entry.title)
    # lst = util.list_entries()
    size = len(lst)
    entry = lst[random.randint(0,size-1)]
    return redirect('/wiki/'+entry)

def new(request):
    if (request.method=='GET'):
        return render(request,'encyclopedia/new.html')
    elif (request.method=='POST'):
        title = request.POST['title']
        content = request.POST['content']
        method = request.POST.get('_method','')
        title = title.strip()
    
        if (title and content):
            if(method=='PUT'):#check if title is matching
                original = request.POST['original'].strip()
                if( (title!=original) or ( not(content.strip()) ) ) :
                    return render(request,'encyclopedia/new.html', {
                        "error": 1,
                    })
                try:
                    # print(request.POST['original'])
                    e = Entry.objects.get(title__exact=original)
                    e.content = content
                    e.full_clean()
                    e.save()
                except:
                    return render(request,'encyclopedia/new.html', {
                        "error": 1,
                    })
                
                #else valid edit
                return render(request, 'encyclopedia/article.html', {
                    "title": title,
                    "new": 1,
                    "content": content
                })
            #else here when a new page is being created
            try:
                e = Entry.objects.create(title=title, content=content)
                e.full_clean()
                e.save()
            except:
                return render(request,'encyclopedia/new.html', {
                    "title": title,
                    "error": 1,
                    "content": content
                })
            return render(request, 'encyclopedia/article.html', {
                "title": title,
                "new": 1,
                "content": content
            })
        # here if there is blank title or blank content
        return render(request, 'encyclopedia/new.html', {
            "error": 1,
        })
    

def edit(request):
    title = request.GET.get('title')
    try:
        entry = Entry.objects.get(title__exact=title)
    except:
        raise Http404("Article does not exist") 
    
    return render(request, 'encyclopedia/new.html', {
        "title": entry.title,
        "original": entry.content,
        "edit": True
    })