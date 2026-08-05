from django.db import models


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
