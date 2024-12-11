from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

def home(request):
    posts_list = Post.objects.all().order_by("date_posted") # Ordenamos por fecha de publicacion
    paginator = Paginator(posts_list, 5) # 5 posts por pagina
    page_number = request.GET.get("page") # Obtenemos el numero de pagina desde la URL
    page_obj = paginator.get_page(page_number) # Obtener los posts de la pagina actual
    return render(request, "blog/home.html", {"page_obj": page_obj})