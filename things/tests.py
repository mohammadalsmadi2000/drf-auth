from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Thing
# Create your tests here.

class ThingTests(TestCase):
  
    @classmethod
    def setUpTestData(cls):
        tetsUser1=get_user_model().objects.create_user(username='testuser1',password='pass')
        tetsUser1.save()
        test_thing=Thing.objects.create(name='flower',owner=tetsUser1,desc="test desc ...")
        test_thing.save()

    def test_thing_model(self):
        thing=Thing.objects.get(id=1)
        actual_owner=str(thing.owner)
        actual_name=str(thing.name)
        actual_desc=str(thing.desc)
        self.assertEqual(actual_owner,"testuser1")
        self.assertEqual(actual_name,"flower") 
        self.assertEqual(actual_desc,"test desc ...")  
    
    def test_thing_update(self):
        thing = Thing.objects.get(id=1)
        thing.name = 'updated flower'
        thing.desc = 'updated desc...'
        thing.save()

        updated_thing = Thing.objects.get(id=1)
        self.assertEqual(updated_thing.name, 'updated flower')
        self.assertEqual(updated_thing.desc, 'updated desc...')
    
    def test_thing_delete(self):
        thing = Thing.objects.get(id=1)
        thing.delete()

        with self.assertRaises(Thing.DoesNotExist):
            Thing.objects.get(id=1)