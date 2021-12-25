from django.core.management.base import BaseCommand

from faker import Faker

from polls.models import User


class Command(BaseCommand):
    help = 'Creates random user and saves to database. ' \
           'Amount of users can be specified via "-amt" or "--amount" option'

    def add_arguments(self, parser):
        parser.add_argument('-amt', '--amount', type=int, choices=range(1, 11),
                            default=1, help='Accepts values from 1 to 10')

    def handle(self, *args, **options):
        amount = options['amount']
        fake = Faker()

        for i in range(amount):
            new_user = User(
                username=fake.user_name(),
                email=fake.email(),
                password=fake.password()
            )
            new_user.save()
        self.stdout.write(self.style.SUCCESS('CREATED AND SAVED!'))
