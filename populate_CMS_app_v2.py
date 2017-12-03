import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Contract_Management_System_v2.settings')

import django
django.setup()

 # FAKE POP SCRIPT
import random
from CMS_app_v2.models import Document
from faker import Faker

fakengen = Faker()

def populate_contracts(N=5):
    for entry in range (N):

        # Create fake data for that entry
        fake_title = fakengen.company()

        #Create the new document entry
        doc = Document.objects.get_or_create(title=fake_title)[0]

if __name__ == '__main__':
    print("populating contracts!")
    populate_contracts(20)
    print("populating contracts complete!")
