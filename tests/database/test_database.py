import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection(db):
    version = db.test_connection()

    sqlite_version = version[0][0]
    assert (
        sqlite_version == "3.50.4"
    ), f"Expected SQLite Version is 3.50.4, got {sqlite_version}"
    print(f"Connected successfully. SQLite Database Version is: {sqlite_version}")


@pytest.mark.database
def test_check_all_users(db):
    users = db.get_all_users()
    assert len(users) >= 1, "Expected at least one user in the database"
    print(users)


@pytest.mark.database
def test_find_address_by_name(db):
    user = db.get_user_adress_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_by_id(db):
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_insert_product_to_db(db):
    db.insert_new_product(4, "cookies", "with chocolate", 30)
    cookie_qnt = db.select_product_qnt_by_id(4)

    assert cookie_qnt[0][0] == 30


@pytest.mark.database
def test_delete_product_from_db(db):
    db.insert_new_product(99, "test name", "test description", 999)
    db.delete_product(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_insert_customer_to_db(db):
    db.insert_new_customer(3, "Dmytro", "Yaroslaviv Val 1", "Kyiv", "04210", "Ukraine")
    user = db.get_user_adress_by_name("Dmytro")

    assert user[0][0] == "Yaroslaviv Val 1"


@pytest.mark.database
def test_change_customer_address(db):
    db.change_customer_address_by_id(3, "Khreschatyk 1", "Kyiv", "00001", "Ukraine")
    user = db.get_user_adress_by_name("Dmytro")

    assert user[0][0] == "Khreschatyk 1"


@pytest.mark.database
def test_customer_delete(db):
    db.insert_new_customer(
        666, "Eugene", "Test Address", "Test City", "11111", "Test Country"
    )
    user_before_delete = db.get_user_adress_by_name("Eugene")
    assert user_before_delete[0][0] == "Test Address"
    db.delete_customer(666)
    user_after_delete = db.get_user_adress_by_name("Eugene")
    assert len(user_after_delete) == 0


@pytest.mark.database
def test_customers_qnt_by_name(db):
    result = db.select_customers_quantity_by_name("Alex")

    assert len(result) == 2


@pytest.mark.database
def test_create_order(db):
    db.insert_new_order(3, 2, 4, "2025-12-30")
    result = db.get_order(3)
    assert result[0] == 3


@pytest.mark.database
def test_update_order(db):
    db.insert_new_order(100, 99, 99, "2025-12-31")
    order_before_update = db.get_order(100)
    assert order_before_update[0] == 100
    assert order_before_update[1] == 99
    assert order_before_update[2] == 99
    db.update_order(100, 7, 7)
    order_after_update = db.get_order(100)
    assert order_after_update[0] == 100
    assert order_after_update[1] == 7
    assert order_after_update[2] == 7


@pytest.mark.database
def test_delete_order(db):
    db.insert_new_order(99, 99, 99, "2025-12-31")
    result = db.get_order(99)
    assert result[0] == 99
    db.delete_order(99)
    result = db.get_order(99)
    assert result is None


@pytest.mark.database
def test_detailed_orders(db):
    orders = db.get_detailed_orders()
    print("Orders: ", orders)
    # Check quantity of orders equal to 4
    assert len(orders) == 4

    # Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "soda"
    assert orders[0][3] == "with sugar"
