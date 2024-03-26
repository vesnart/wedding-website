# from django.core.management.base import BaseCommand
# from django.conf import settings
# import os
# from images.models import Image

# class Command(BaseCommand):
#     help = 'Bulk uploads images from a specified directory'

#     def add_arguments(self, parser):
#         parser.add_argument('directory', type=str, help='Directory of images to upload')

#     def handle(self, *args, **options):
#         directory = options['directory']
#         for filename in os.listdir(directory):
#             if filename.endswith((".jpg", ".jpeg", ".png")):
#                 path = os.path.join(directory, filename)
#                 title = os.path.splitext(filename)[0]
#                 image_description = os.path.splitext(filename)[0]  # without extension
#                 category = 'medium'
#                 image = Image(image=path, title=title, image_description=image_description, category=category)
#                 image.save()
#                 self.stdout.write(self.style.SUCCESS(f'Successfully uploaded "{filename}"'))
#                 print(f"file {filename} Uploaded Successfully!")
