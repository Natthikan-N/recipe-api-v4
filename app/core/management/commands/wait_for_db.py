import time

from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **option):
        self.stdout.write("waiting for db")

        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except(Psycopg2OpError, OperationalError):
                self.stdout.write("Database unavaliable , waiting second...")
                time.sleep(1)
        self.stdout.write("DB is ready!!")
