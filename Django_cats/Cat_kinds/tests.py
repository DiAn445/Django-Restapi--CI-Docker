from django.test import TestCase
from django.conf import settings
from .utils import CatKinds

class UnitTest(TestCase):
    fixtures = ['myfixture.json']
    
    def test_amount_of_obj_in_db(self):
        db = CatKinds.objects.count()
        self.assertEqual(db, 6)

    def test_likes_are_positive(self):
        db = CatKinds.objects.all()
        result = [i.likes for i in db]
        match result:
            case result if min(result) < 0:
                raise ValueError("Error: the result should be >= 0")
        self.assertEqual(True, True)    


