from auth_system import User, Administrator, RegularUser, Guest, AccessControl

# =====================================================================
# МЕТОД 1: User.verify_username
# =====================================================================

def test_verify_username_successful():
    """Тест 1.1: Метод возвращает True, если имя совпадает."""
    user = User("Alexey", "1234567890")
    result = user.verify_username("Alexey")
    assert result is True


def test_verify_username_incorrect():
    """Тест 1.2: Метод возвращает False, если имя указано неверно."""
    user = User("Alexey", "1234567890")
    result = user.verify_username("WrongName")
    assert result is False


# =====================================================================
# МЕТОД 2: User.verify_password
# =====================================================================

def test_verify_password_successful():
    """Тест 2.1: Проверка с правильным паролем."""
    user = User("Sonya", "qwertyuiop[]")
    result = user.verify_password("qwertyuiop[]")
    assert result is True


def test_verify_password_wrong():
    """Тест 2.2: Проверка с неверным паролем."""
    user = User("Sonya", "qwertyuiop[]")
    result = user.verify_password("incorrect_pass")
    assert result is False


# =====================================================================
# МЕТОД 3: AccessControl.authenticate_user
# =====================================================================

def test_authenticate_user_successful():
    """Тест 3.1: Успешная аутентификация добавленного пользователя."""
    system = AccessControl()
    admin = Administrator("Admin_Boss", "admin_hash_123", ["delete_users"])
    system.add_user(admin)

    authenticated = system.authenticate_user("Admin_Boss", "admin_hash_123")
    assert authenticated is not None
    assert authenticated.username == "Admin_Boss"


def test_authenticate_user_wrong_password():
    """Тест 3.2: Ошибка аутентификации при неверном пароле (возвращает None)."""
    system = AccessControl()
    user = User("Alexey", "1234567890")
    system.add_user(user)

    authenticated = system.authenticate_user("Alexey", "bad_pass")
    assert authenticated is None


def test_authenticate_user_not_found():
    """Тест 3.3 (дополнительный): Попытка войти под несуществующим пользователем."""
    system = AccessControl()
    authenticated = system.authenticate_user("UnknownUser", "any_password")
    assert authenticated is None

def test_user_show_details(capsys):
    user = User("Sonya", "qwertyuiop[]")
    user.show_details()
    captured = capsys.readouterr()
    assert "Username: Sonya" in captured.out
    assert "Is Active: True" in captured.out


def test_admin_permissions():
    admin = Administrator("Admin_Boss", "admin_hash_123", ["edit_roles"])
    assert admin.permissions == ["edit_roles"]
    assert admin.is_active is True

def test_regular_user_default_and_custom_date():
    reg_default = RegularUser("Ivan_default", "hash1")
    reg_custom = RegularUser("Ivan_user", "hash2", "2026-11-09")
    assert reg_default.last_login_date == ""
    assert reg_custom.last_login_date == "2026-11-09"

def test_guest_user_attributes():
    guest = Guest()
    assert guest.username == "Guest"
    assert guest.access_level == "limited"
    assert guest.password_hash == ""