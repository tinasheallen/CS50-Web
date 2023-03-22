from django.shortcuts import render
import random
import markdown
from . import util

def changer(title):
    stuff = util.get_entry(title)
    markdowner = markdown.Markdown()
    if stuff == None:
        return None
    else:
        return markdowner.convert(stuff)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entries(request, title):
    contents = changer(title)
    if contents == None:
        return render(request, "encyclopedia/errorpage.html", {
            "message": "!Entry does not exist!"
        })
    else:
        return render(request, "encyclopedia/entrypage.html", {
            "title": title,
            "content": contents
        })
    


def search(request):
    if request.method == "POST":
        searching = request.POST['q']
        contents = changer(searching)
        if contents is not None:
            return render(request, "encyclopedia/entrypage.html", {
                "tite": searching,
                "content": contents
            })
        else:
            allEntries = util.list_entries()
            recommendations = []
            for entry in allEntries:
                if searching.lower() in entry.lower():
                    recommendations.append(entry)
            return render(request, "encyclopedia/searchpage.html", {
                "recommendations": recommendations
            })


def createPage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newpage.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        duplicate = util.get_entry(title)
        if duplicate is not None:
            return render(request, "encyclopedia/errorpage.html", {
                "message": "! This page already exists"
            } )
        else:
            util.save_entry(title, content)
            contents = changer(title)
            return render(request, "encyclopedia/entrypage.html", {
                "title": title,
                "content": contents
            })
        

def edit(request):
    if request.method == 'POST':
        title = request.POST['entryName']
        content = util.get_entry(title)
        return render(request, "encyclopedia/editpage.html",{
            "title": title,
            "content": content
        })
    

def editPage(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        contents = changer(title)
        return render(request, "encyclopedia/entrypage.html", {
            "title": title,
            "content": contents
        })

def randomPage(request):
    entryName = util.list_entries()
    randInput = random.choice(entryName)
    contents = changer(randInput)
    return render(request, "encyclopedia/entrypage.html", {
        "title": randInput,
        "content": contents
    })



        

