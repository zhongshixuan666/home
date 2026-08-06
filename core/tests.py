import json

from django.test import TestCase
from django.urls import reverse

from .models import VerificationCode


class ContentApiTests(TestCase):
    def test_news_create_and_list(self):
        response = self.client.post(
            reverse('news_api'),
            data=json.dumps({
                'title': '国羽新德里世锦赛前瞻',
                'category': '赛事',
                'date': '2026-08-17',
                'excerpt': '石宇奇领衔国羽出战。',
                'image': '/home/images/hero-main.webp',
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


class AuthApiTests(TestCase):
    def send_code(self, channel, account):
        return self.client.post(
            reverse('auth_send_code'),
            data=json.dumps({'channel': channel, 'account': account, 'purpose': 'register'}),
            content_type='application/json',
        )

    def register(self, username, phone, email, channel, code):
        return self.client.post(
            reverse('auth_register'),
            data=json.dumps({
                'username': username,
                'password': 'test123456',
                'phone': phone,
                'email': email,
                'channel': channel,
                'code': code,
            }),
            content_type='application/json',
        )

    def test_register_and_login_with_phone(self):
        send = self.send_code('phone', '13800138000')
        self.assertEqual(send.status_code, 200)
        code = VerificationCode.objects.get(account='13800138000').code

        register = self.register('shiyuqi', '13800138000', 'shi@yujie.com', 'phone', code)
        self.assertEqual(register.status_code, 201)

        self.client.post(reverse('auth_logout'))
        login = self.client.post(
            reverse('auth_login'),
            data=json.dumps({'account': '13800138000', 'password': 'test123456'}),
            content_type='application/json',
        )
        self.assertEqual(login.status_code, 200)
        self.assertEqual(login.json()['user']['phone_verified'], True)

    def test_register_and_login_with_email(self):
        send = self.send_code('email', 'player@yujie.com')
        code = VerificationCode.objects.get(account='player@yujie.com').code

        register = self.register('chenyufei', '13900139000', 'player@yujie.com', 'email', code)
        self.assertEqual(register.status_code, 201)

        self.client.post(reverse('auth_logout'))
        login = self.client.post(
            reverse('auth_login'),
            data=json.dumps({'account': 'player@yujie.com', 'password': 'test123456'}),
            content_type='application/json',
        )
        self.assertEqual(login.status_code, 200)
        self.assertEqual(login.json()['user']['email_verified'], True)

    def test_duplicate_phone_is_rejected(self):
        send = self.send_code('phone', '13700137000')
        code = VerificationCode.objects.get(account='13700137000').code
        self.register('firstuser', '13700137000', 'first@yujie.com', 'phone', code)

        send_again = self.send_code('phone', '13700137000')
        code_again = VerificationCode.objects.filter(account='13700137000').order_by('-created_at').first().code
        duplicate = self.register('seconduser', '13700137000', 'second@yujie.com', 'phone', code_again)
        self.assertEqual(duplicate.status_code, 400)
        self.assertIn('手机号已被注册', duplicate.json()['error'])
