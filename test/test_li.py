#import unittest
from django.utils import unittest
import li

class LinkedInTests(unittest.TestCase):
    
    def test_handle(self):
        api = li.mgc_handle()
        self.assertIsNotNone(api)
        self.assertEqual(api.get_profile().last_name, "Champion")
    
    def test_get_group(self):
        api = li.mgc_handle()
        profile_id = api.get_profile().id
        
        groups = api.get_groups(profile_id)
        self.assertNotEqual(len(groups), 0)
        self.assertIsNotNone(groups[0].name)