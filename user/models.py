from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from itsdangerous import TimedJSONWebSignatureSerializer as TJWSSerializer, BadData


# Create your models here.

class User(AbstractUser):
    """用户表"""

    class Meta:
        db_table = "dgk_user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def generate_set_password_token(self):
        """
        生成修改密码的token
        """
        serializer = TJWSSerializer(settings.SECRET_KEY, expires_in=60 * 60)
        data = {'user_id': self.id}
        token = serializer.dumps(data)
        return token.decode()

    @staticmethod
    def check_set_password_token(token, user_id):
        """
        检验设置密码的token
        """
        serializer = TJWSSerializer(settings.SECRET_KEY, expires_in=60 * 60)
        try:
            data = serializer.loads(token)
        except BadData:
            return False
        else:
            if int(user_id) != data.get('user_id'):
                return False
            else:
                return True
