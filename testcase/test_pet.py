
import pytest
import allure
from utile.path_utils import get_pet_data
from utile.path_utils import get_pet_data,get_query_data
from utile.path_utils import get_delete_data
@pytest.mark.parametrize('case_data',get_pet_data())
def test_update_pet(client,created_pet,case_data):
    pet_id = created_pet["id"]
    payload = case_data['update_payload']
    response = client.put("/pet", json=payload)
    assert response.status_code == case_data['expected_status']
@pytest.mark.parametrize('case_data',get_query_data())
def test_get_pet(client,created_pet,case_data):
    pet_id = case_data['query_id']
    if pet_id == "dynamic":
        pet_id = created_pet["id"]
    response = client.get(f"/pet/{pet_id}")
    assert response.status_code == case_data['expected_status']
    @allure.epic("Swagger Petstore 接口自动化测试")
@allure.feature("宠物管理模块")
@allure.story("删除宠物接口")
@allure.title("测试动态删除宠物并断言成功")
@pytest.mark.parametrize('case_data',get_delete_data())
def test_delete_pet(client,created_pet,case_data):
    pet_id = case_data['delete_id']
    if pet_id == "dynamic":
        pet_id = created_pet["id"]
    response = client.delete(f"/pet/{pet_id}")
    assert response.status_code == case_data['expected_code']
    if case_data['expected_code'] == 200:
        res_body = response.json()
        assert res_body['message'] == str(pet_id)

