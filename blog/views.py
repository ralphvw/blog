from django.shortcuts import render


posts = [
    {
        "author": "CoreyMS",
        "title": "Blog Post 1",
        "content": "Content",
        "date_posted": "08-27-2018",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Content 2",
        "date_posted": "08-29-2018",
    },
]


# Create your views here.
def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html")
