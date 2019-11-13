# Javascript with Django

```javascript
const likeBtns = document.querySelectorAll('.fa-heart')

    likeBtns.forEach((btn) => {
      btn.addEventListener('click', (e) => {
        const postId = e.target.dataset.id
        
        axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'
        axios.defaults.xsrfCookieName = 'csrftoken'
        axios.defaults.xsrfHeaderName = 'X-CSRFToken'

        axios.post(`/posts/${postId}/like/`)
            .then((response) => {
              console.log(response)
            })
            .catch((error) => {
              console.log(error)
            })
```

```python
from django.http import JsonResponse


def like(request, id):

    return JsonResponse({'message': 'is it right?'})
```