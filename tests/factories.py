from django.contrib.auth import get_user_model

import factory


class UserFactory(factory.Factory):
    """
    Generates unique user so other factories don't generate
    integrity error when they need a user.
    """
    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user

    FACTORY_FOR = get_user_model()

    username = factory.Sequence(lambda n: 'user%s' % n)
    first_name = factory.Sequence(lambda n: 'Test%s' % n)
    last_name = factory.Sequence(lambda n: 'User%s' % n)
    email = factory.Sequence(lambda n: 'user%s@test.com' % n)
    is_staff = True
    is_active = True
    is_superuser = False