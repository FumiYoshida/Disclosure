from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        # ここに更新の内容を書く
        print('updated')