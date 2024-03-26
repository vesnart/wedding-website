from .models import TrackingScript

def tracking_scripts(request):
    return {
        'tracking_scripts': TrackingScript.objects.filter(active=True)
    }