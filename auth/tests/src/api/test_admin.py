# TODO: Не могу придумать как выполнить команду по созданию админа (пытался сделать через db.session.add() итд,
#  но алхимия ругается на дублирование определения моделей
#  raise exc.InvalidRequestError(
#  sqlalchemy.exc.InvalidRequestError: Table 'auth_history' is already defined for this MetaData instance.
#  Specify 'extend_existing=True' to redefine options and columns on an existing Table object.
#  но как понял 'extend_existing=True' очень не рекомендуется использовать!

# import json
# import pytest
#
#
# @pytest.mark.parametrize(
#     'user, query, expected_response',
#     [
#         ({'email': 'admin@admin.com', 'password': 'admin_admin'}, {'name': 'new_role'}, {'status_code': 200})
#     ]
# )
# def test_create_role(client, user, query, expected_response):
#
#     response = client.post('/auth/sign-up', data=json.dumps(user), content_type='application/json')
#     access_token = response.get_json().get('access_token')
#
#     headers = {'Authorization': f'Bearer {access_token}'}
#
#     response = client.post(
#     '/admin/roles/create', data=json.dumps(query), content_type='application/json', headers=headers
#     )
#
#     assert response.status_code == expected_response.get('status_code')
