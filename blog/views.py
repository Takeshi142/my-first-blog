from django.shortcuts import render
from django.utils import timezone
from .models import Post
import datetime
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
    timetesut = timezone.make_aware(datetime.datetime(year=2021, month=12, day=24, hour=0))
    posts = Post.objects.filter(published_date__lte=timetesut).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


