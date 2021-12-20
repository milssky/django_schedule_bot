from django.core.management.base import BaseCommand, CommandError
from bot.handlers import start


class Command(BaseCommand):
    help = "Start bot command"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("START BOT"))
        start()
