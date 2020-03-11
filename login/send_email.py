import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
if __name__ == '__main__':
    send_mail(
        '测试邮件',
        'context',
        'monitor-etl@lhcis.com',
        ['wangj_xx@lhcis.com']
    )
