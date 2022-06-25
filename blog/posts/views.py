from django.http import JsonResponse
import os
import markdown
from posts.utils import tags, fixUnicode




def post(request, slug):
    fPath = os.path.join(os.getcwd(), f"assets/posts/{slug}.md")
    f = fixUnicode(open(fPath, "r").read())
    
    md = f.split("===")[-1]
    html = markdown.markdown(md)

    result = {
        "post": {
            "content": html,
            "tags": tags(html)
        }
    }
    return JsonResponse(result, safe=True)


def posts(request):
    dir = os.path.join(os.getcwd(), "assets/posts")
    ls = os.listdir(dir)

    result = []
    for f in ls:
        result.append({
            "slug": f[:-3],
            "title": fixUnicode(open(os.path.join(dir, f), "r").readlines()[1][7:-1])
        })
    return JsonResponse(result, safe=False)