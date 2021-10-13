import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from profiles.models import Profile


@pytest.mark.django_db
def test_letting_index_view(client):
    url = reverse('profiles_index')
    response = client.get(url)
    assert b"Profiles" in response.content
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_view(client):
    user = User.objects.create(
        username='Voldemort',
        first_name='Tom',
        last_name="Riddle",
        email='Tom_unicorn@onestpasvraimentmechant.com'
    )
    Profile.objects.create(
        favorite_city='Lyon',
        user_id=user.id
    )
    url = reverse('profile', args=(user.username,))
    response = client.get(url)
    assert b'Voldemort' in response.content
    assert response.status_code == 200