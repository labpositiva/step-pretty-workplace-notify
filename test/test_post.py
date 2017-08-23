# -*- coding: utf-8 -*-
import unittest

from src.post import Post


class TestPost(unittest.TestCase):

    def test_create_post(self):
        'post() create in workplace facebook'
        data = {
            'token': 'token',
            'group': 'group',
            'user': 'user',
            'message': 'message',
        }
        response = Post().create(**data)
        not self.assertEqual(response, None)
