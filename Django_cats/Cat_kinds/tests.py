from django.test import TestCase

from Django_cats.Cat_kinds.models import CatKinds

class UnitTest(TestCase):
    def amount_of_obj_in_db(self):
        db = CatKinds.objects.all()
        return self.assertEqual(len(db), 6)
        