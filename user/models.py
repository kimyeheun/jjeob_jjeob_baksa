from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, user_email, user_name, user_id, password=None):
        if not user_email:
            raise ValueError("이메일은 필수 입력 사항 입니다.")
        if not user_name:
            raise ValueError("이름은 필수 입력 사항 입니다.")
        if not user_id:
            raise ValueError("아이디는 필수 입력 사항 입니다.")

        user = self.model(
            user_email=self.normalize_email(user_email),
            user_name=user_name,
            user_id=user_id,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_email, user_name, user_id, password=None):
        user = self.create_user(
            user_email=self.normalize_email(user_email),
            password=password,
            user_name=user_name,
            user_id=user_id,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    user_id = models.IntegerField(null=False, primary_key=True)
    user_name = models.CharField(max_length=50, null=False, verbose_name="유저 이름")
    password = models.CharField(max_length=1000, null=False)
    user_nick = models.CharField(max_length=50, null=True, blank=True, verbose_name="유저 닉네임")
    user_category = models.BooleanField(default=True, verbose_name="유저 카테고리")
    user_email = models.CharField(verbose_name="이메일", max_length=50, null=False, unique=True,)
    food_reco = models.IntegerField(null=True, blank=True, verbose_name="음식 추천수")
    user_pic = models.ImageField(null=True, blank=True, verbose_name="유저 프로필 사진")

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS = ['user_id', 'user_name', ]

    objects = MyAccountManager()

    def __str__(self):
        return self.user_email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True