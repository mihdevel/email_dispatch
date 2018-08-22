from django.test import TestCase
import requests
from email_dispatch.models import Group

urls = {
  'group': 'http://127.0.0.1:8000/groups',
  'email': 'http://127.0.0.1:8000/emails',
  'dispatch': 'http://127.0.0.1:8000/dispatchs',
}

class GroupTests(TestCase):
  
  # def test_create_groups(self, url=urls['group']):
  #   self.assertEqual(requests.put(url, data={"name": "name1"}), {"id": 1, "name": "name1" })
  
  def test_get_all_groups(self, url=urls['group']):
    Group.objects.create(name='name1')
    Group.objects.create(name='name2')
    self.assertEqual(requests.get(url).text, '[{"id": 1, "name": "name1"}, {"id": 1, "name": "name2" }]')

  def test_get_one_groups(self, url=urls['group']):
    Group(name='name1')
    self.assertEqual(requests.get(url+'/1').text, '{"id":1,"name":"name1"}')
    
  # def test_put_group(self, url=urls['group']):
  #   Group(name='name1')
  #   requests.put(url, data={"id": 1, "name": "name2"})
  #   self.assertEqual(requests.get(url+'/1'), 'name2')
  #
  def test_deleted_group(self, url=urls['group']):
    Group(name='name1')
    self.assertEqual(requests.delete(url+'/1').status_code, 204)