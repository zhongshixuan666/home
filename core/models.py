from django.db import models
from django.contrib.auth.models import User


class Contract(models.Model):
    name = models.CharField('联系人', max_length=50)
    phone = models.CharField('联系电话', max_length=30)
    project_type = models.CharField('项目类型', max_length=50)
    message = models.TextField('需求说明')
    created_at = models.DateTimeField('提交时间', auto_now_add=True)

    class Meta:
        verbose_name = '联系留言'
        verbose_name_plural = '联系留言'
        ordering = ['-created_at']
        db_table = 'contract'

    def __str__(self):
        return f'{self.name} · {self.project_type}'


class NewsArticle(models.Model):
    title = models.CharField('标题', max_length=200)
    category = models.CharField('分类', max_length=50, blank=True, default='资讯')
    date = models.CharField('日期', max_length=50, blank=True)
    excerpt = models.TextField('摘要', blank=True)
    image = models.CharField('图片', max_length=500, blank=True)
    is_published = models.BooleanField('是否发布', default=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '新闻资讯'
        verbose_name_plural = '新闻资讯'
        ordering = ['-created_at']
        db_table = 'news_article'

    def __str__(self):
        return self.title


class PlayerProfile(models.Model):
    name = models.CharField('姓名', max_length=100)
    en_name = models.CharField('英文名', max_length=100, blank=True)
    country = models.CharField('协会', max_length=100, blank=True)
    birth = models.CharField('出生日期', max_length=50, blank=True)
    height = models.CharField('身高', max_length=50, blank=True)
    status = models.CharField('当前状态', max_length=100, blank=True)
    style = models.CharField('技术特点', max_length=300, blank=True)
    bio = models.TextField('档案介绍', blank=True)
    image = models.CharField('图片', max_length=500, blank=True)
    video = models.CharField('视频', max_length=500, blank=True)
    is_published = models.BooleanField('是否发布', default=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '球员档案'
        verbose_name_plural = '球员档案'
        ordering = ['-created_at']
        db_table = 'player_profile'

    def __str__(self):
        return self.name


class MatchSchedule(models.Model):
    MATCH_TYPES = (
        ('upcoming', '赛程预告'),
        ('result', '近期赛果'),
        ('champion', '冠军榜'),
    )
    match_type = models.CharField('数据类型', max_length=20, choices=MATCH_TYPES, default='upcoming')
    date = models.CharField('日期', max_length=50, blank=True)
    time = models.CharField('时间', max_length=50, blank=True)
    event = models.CharField('赛事', max_length=200)
    stage = models.CharField('阶段', max_length=200, blank=True)
    venue = models.CharField('地点', max_length=200, blank=True)
    watch = models.CharField('看点', max_length=300, blank=True)
    player_a = models.CharField('对阵 A', max_length=100, blank=True)
    player_b = models.CharField('对阵 B', max_length=100, blank=True)
    score = models.CharField('比分', max_length=100, blank=True)
    result = models.CharField('结果', max_length=200, blank=True)
    champion = models.CharField('冠军', max_length=200, blank=True)
    is_published = models.BooleanField('是否发布', default=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '比赛赛程'
        verbose_name_plural = '比赛赛程'
        ordering = ['-created_at']
        db_table = 'match_schedule'

    def __str__(self):
        return self.event


class Product(models.Model):
    name = models.CharField('名称', max_length=200)
    desc = models.TextField('说明', blank=True)
    image = models.CharField('图片', max_length=500, blank=True)
    tag = models.CharField('分类', max_length=50, blank=True)
    rank = models.CharField('排名', max_length=50, blank=True)
    score = models.CharField('评分', max_length=50, blank=True)
    is_published = models.BooleanField('是否发布', default=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '装备产品'
        verbose_name_plural = '装备产品'
        ordering = ['-created_at']
        db_table = 'product'

    def __str__(self):
        return self.name


class MemberProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField('手机号', max_length=20, unique=True)
    phone_verified = models.BooleanField('手机已验证', default=False)
    email_verified = models.BooleanField('邮箱已验证', default=False)
    created_at = models.DateTimeField('注册时间', auto_now_add=True)

    class Meta:
        verbose_name = '会员档案'
        verbose_name_plural = '会员档案'
        ordering = ['-created_at']
        db_table = 'member_profile'

    def __str__(self):
        return f'{self.user.username} · {self.phone}'


class VerificationCode(models.Model):
    CHANNELS = (
        ('phone', '手机'),
        ('email', '邮箱'),
    )
    channel = models.CharField('发送渠道', max_length=10, choices=CHANNELS)
    account = models.CharField('手机号或邮箱', max_length=120)
    code = models.CharField('验证码', max_length=10)
    purpose = models.CharField('用途', max_length=20, default='register')
    expires_at = models.DateTimeField('过期时间')
    verified = models.BooleanField('已验证', default=False)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '验证码'
        verbose_name_plural = '验证码'
        ordering = ['-created_at']
        db_table = 'verification_code'

    def __str__(self):
        return f'{self.channel} · {self.account}'


class CommunityPost(models.Model):
    CATEGORIES = (
        ('球迷投稿', '球迷投稿'),
        ('赛事讨论', '赛事讨论'),
        ('装备交流', '装备交流'),
        ('训练心得', '训练心得'),
        ('其他', '其他'),
    )
    title = models.CharField('标题', max_length=120)
    content = models.TextField('内容')
    author = models.CharField('作者', max_length=50)
    category = models.CharField('分类', max_length=50, choices=CATEGORIES, default='球迷投稿')
    views = models.PositiveIntegerField('浏览数', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    hot_score = models.PositiveIntegerField('热度值', default=0)
    is_published = models.BooleanField('是否发布', default=True)
    created_at = models.DateTimeField('发布时间', auto_now_add=True)

    class Meta:
        verbose_name = '社区投稿'
        verbose_name_plural = '社区投稿'
        ordering = ['-created_at']
        db_table = 'community_post'

    def __str__(self):
        return self.title