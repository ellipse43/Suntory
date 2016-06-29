# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from django.core.mail import send_mail
from django.core import validators
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import six, timezone
from django.conf import settings


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
        help_text=_(
            'Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(
                r'^[\w.@+-]+$',
                _('Enter a valid username. This value may contain only '
                  'letters, numbers ' 'and @/./+/-/_ characters.')
            ),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(
        _('email address'),
        unique=True,
        validators=[validators.EmailValidator(), ],
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    #
    introduction = models.CharField(
        _('introduction'), max_length=255, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Followee(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='followees',
        on_delete=models.SET_NULL, blank=True, null=True)
    followee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'followee', )

    def __unicode__(self):
        return '%s-%s' % (self.user, self.followee,)


class Follower(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='followers',
        on_delete=models.SET_NULL, blank=True, null=True)
    follower = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'follower', )

    def __unicode__(self):
        return '%s-%s' % (self.user, self.follower,)


class Blocker(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='blockers',
        on_delete=models.SET_NULL, blank=True, null=True)
    blocker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'blocker', )

    def __unicode__(self):
        return '%s-%s' % (self.user, self.blocker,)
