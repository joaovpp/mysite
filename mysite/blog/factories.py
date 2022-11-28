import factory
from faker import Factory as FakerFactory

from django.contrib.auth.models import User
from django.utils.timezone import now

from .models import Post

faker = FakerFactory.create()

class UserFactory(factory.django.DjangoModelFactory):
    """Cria um modelo fake de User pré-definido do Django
    O factory é um espelho do nosso modelo"""
    class Meta:
        model = User

    email = factory.Faker("safe_email") #email fake
    username = factory.LazyAttribute(lambda x: faker.name()) #username fake

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop("password", None)
        user = super(UserFactory, cls), prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user

class PostFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda x: faker.sentence())
    created_on = factory.LazyAttribute(lambda x: now())
    author = factory.SubFactory(UserFactory)
    status = 0

    class Meta:
        model = Post
