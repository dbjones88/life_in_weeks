# Displays a lifetime as weeks.
Inspired by [this blog](https://waitbutwhy.com/2014/05/life-weeks.html) By Tim Urban

### In the top level urls.py add:
```python
    urlpatterns = [
        ...
    path('', include('lifeweeks.urls')),
        ...
]
```
### In settings.py add to INSTALLED_APPS:
```python
INSTALLED_APPS = [
    ...
    'lifeweeks',
]
```