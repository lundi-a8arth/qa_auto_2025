import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_find_address_by_name():
    db = Database()
    user = db.get_user_adress_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_by_id():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_insert_product_to_db():
    db = Database()
    db.insert_new_product(4, "печиво", "солодке", 30)
    cookie_qnt = db.select_product_qnt_by_id(4)

    assert cookie_qnt[0][0] == 30


@pytest.mark.database
def test_delete_product_from_db():
    db = Database()
    db.insert_new_product(99, "test name", "test description", 999)
    db.delete_product(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_insert_customer_to_db():
    db = Database()
    db.insert_new_customer(3, "Dmytro", "Ivasiuka 16D", "Kyiv", "04210", "Ukraine")
    user = db.get_user_adress_by_name("Dmytro")

    assert user[0][0] == "Ivasiuka 16D"


@pytest.mark.database
def test_change_customer_address():
    db = Database()
    db.change_customer_address_by_id(3, "Khreschatyk 1", "Kyiv", "00001", "Ukraine")
    user = db.get_user_adress_by_name("Dmytro")

    assert user[0][0] == "Khreschatyk 1"


@pytest.mark.database
def test_customer_delete():
    db = Database()
    db.insert_new_customer(
        666, "Eugene", "Test Address", "Test City", "11111", "Test Country"
    )
    user_before_delete = db.get_user_adress_by_name("Eugene")
    assert user_before_delete[0][0] == "Test Address"
    db.delete_customer(666)
    user_after_delete = db.get_user_adress_by_name("Eugene")
    assert len(user_after_delete) == 0


@pytest.mark.database
def test_customers_qnt_by_name():
    db = Database()
    result = db.select_customers_quantity_by_name("Alex")

    assert len(result) == 2


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"
