from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser,
                                        PermissionsMixin)

from company.models import Company


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class DefaultUser(AbstractBaseUser, PermissionsMixin):

    name = models.CharField('Nome', max_length=100, blank=True, null=True)
    image = models.ImageField(
        upload_to='account/images',
        verbose_name='Imagem',
        null=True,
        blank=True
    )
    email = models.EmailField('E-mail', unique=True)
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    objects = UserManager()

    REQUIRED_FIELDS = ['name']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.name

    def get_full_name(self):
        # The user is identified by their email address
        return self.name

    def get_short_name(self):
        # The user is identified by their email address
        return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __unicode__(self):
        return u"name: %s " % (self.name or u'')

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


class TechRecruiter(DefaultUser):

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="tech_recruiter_company",
        verbose_name="Company"
    )

    def __str__(self):
        return str(self.name or "[Not set]") + " -> " + self.email

    def get_short_name(self):
        return self.name

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Tech Recruiter'
        verbose_name_plural = 'Tech Recruiteis'


class Candidate(DefaultUser):

    def __str__(self):
        return str(self.name or "[Not set]") + " -> " + self.email

    def get_short_name(self):
        return self.name

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Candidate'
        verbose_name_plural = 'Candidates'
