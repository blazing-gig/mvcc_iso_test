import itertools
import os, django, json
# sys.path.append("") #here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iso_test.settings")
django.setup()

from sample.models import Employee

def get_obj(obj):
    return {key.replace(" ", "_"): obj[key] for key in obj }


with open("/Users/I0847/Desktop/sample_data/7mm_companies.json", "r") as f:
    data = []
    for index, line in enumerate(f):
        doc = json.loads(line)
        if index > 0 and index % 50000 == 0:
            Employee.objects.bulk_create([ Employee(**get_obj(obj)) for obj in data ])
            print("Created from {} to {}".format(index - 50000, index))
            data = []
        else:
            data.append(doc)

    if len(data) > 0:
        print("final creation length ", len(data))
        Employee.objects.bulk_create([Employee(**get_obj(obj)) for obj in data])

