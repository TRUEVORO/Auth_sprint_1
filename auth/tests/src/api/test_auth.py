import json
from http import HTTPStatus

import pytest


@pytest.mark.parametrize(
    'user, expected_response',
    [
        ({'email': 'testuser@test.com', 'password': 'password123'}, {'status_code': HTTPStatus.OK}),
        ({'email': 'new_testuser@test.com', 'password': 'short'}, {'status_code': HTTPStatus.NOT_FOUND}),
        ({'email': 'not_email', 'password': 'password123'}, {'status_code': HTTPStatus.NOT_FOUND}),
    ],
)
def test_sign_up(client, user, expected_response):
    response = client.post('/auth/sign-up', data=json.dumps(user), content_type='application/json')
    assert response.status_code == expected_response['status_code']


@pytest.mark.parametrize(
    'user, expected_response',
    [
        ({'email': 'testuser@test.com', 'password': 'password123'}, {'status_code': HTTPStatus.OK}),
        ({'email': 'new_testuser@test.com', 'password': 'short'}, {'status_code': HTTPStatus.NOT_FOUND}),
        ({'email': 'not_email', 'password': 'password123'}, {'status_code': HTTPStatus.NOT_FOUND}),
    ],
)
def test_sign_in(client, user, expected_response):
    response = client.post('/auth/sign-in', data=json.dumps(user), content_type='application/json')
    assert response.status_code == expected_response['status_code']


@pytest.mark.parametrize(
    'user, expected_response',
    [({'email': 'testuser@test.com', 'password': 'password123'}, {'status_code': HTTPStatus.OK})],
)
def test_refresh(client, user, expected_response):
    response = client.post('/auth/sign-in', data=json.dumps(user), content_type='application/json')
    refresh_token = response.get_json().get('refresh_token')

    headers = {'Authorization': f'Bearer {refresh_token}'}

    response = client.post('/auth/refresh', headers=headers)
    assert response.status_code == expected_response['status_code']


@pytest.mark.parametrize(
    'user, expected_response',
    [({'email': 'testuser@test.com', 'password': 'password123'}, {'status_code': HTTPStatus.OK})],
)
def test_sign_out(client, user, expected_response):
    response = client.post('/auth/sign-in', data=json.dumps(user), content_type='application/json')
    refresh_token = response.get_json().get('refresh_token')

    headers = {'Authorization': f'Bearer {refresh_token}'}

    response = client.post('/auth/sign-out', headers=headers)
    assert response.status_code == expected_response['status_code']


# @pytest.mark.parametrize(
#     'user, expected_response',
#     [
#         ({'email': 'newuser@test.com', 'password': 'password123'}, {'status_code': HTTPStatus.OK})
#     ]
# )
# def test_auth_history(client, user, expected_response):
#     response = client.post('/auth/sign-up', data=json.dumps(user), content_type='application/json')
#     access_token = response.get_json().get('access_token')
#
#     headers = {'Authorization': f'Bearer {access_token}'}
#
#     response = client.post('/auth/auth-history', headers=headers)
#     assert response.status_code == expected_response['status_code']
