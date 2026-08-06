import json

from django.test import TestCase
from django.urls import reverse


class ContentApiTests(TestCase):
    def test_news_create_and_list(self):
        response = self.client.post(
            reverse('news_api'),
            data=json.dumps({
                'title': '国羽新德里世锦赛前瞻',
                'category': '赛事',
                'date': '2026-08-17',
                'excerpt': '石宇奇领衔国羽出战。',
                'image': '/home/media/imges/hero-main.webp',
            }),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['ok'], True)

        list_response = self.client.get(reverse('news_api'))
        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(list_response.json()['count'], 1)

    def test_news_requires_title(self):
        response = self.client.post(
            reverse('news_api'),
            data=json.dumps({'category': '赛事'}),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 400)

    def test_player_create_and_update(self):
        response = self.client.post(
            reverse('players_api'),
            data=json.dumps({'name': '石宇奇', 'country': '中国'}),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 201)
        item_id = response.json()['id']

        update_response = self.client.patch(
            reverse('players_api_detail', args=[item_id]),
            data=json.dumps({'status': '男单世界第一'}),
            content_type='application/json',
        )
        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(update_response.json()['ok'], True)

    def test_match_and_product_create(self):
        match_response = self.client.post(
            reverse('matches_api'),
            data=json.dumps({'event': '韩国大师赛', 'date': '08.04-08.09'}),
            content_type='application/json',
        )
        self.assertEqual(match_response.status_code, 201)

        product_response = self.client.post(
            reverse('products_api'),
            data=json.dumps({'name': '旗舰进攻型球拍', 'tag': '球拍'}),
            content_type='application/json',
        )
        self.assertEqual(product_response.status_code, 201)
