import pytest
from unittest.mock import Mock
from sqlalchemy.orm import Session
from app.services.exchange_service import process_exchange
from app.models.user_model import User
from app.models.transaction import Transaction

@pytest.fixture
def mock_db_session():
    session = Mock(spec=Session)
    return session

# Caso 1
def test_process_exchange_success(mock_db_session): 
    # Crear un usuario simulado

    user = User(id=1, name="Test User", email="test@tester.com", daily_limit=1000.0)
    mock_db_session.query.return_value.filter.return_value.first.return_value = user

    # Mock de `add` y `commit` para evitar escritura en base de datos
    mock_db_session.add = Mock()
    mock_db_session.commit = Mock()

    # Llamar a la función
    result = process_exchange(
        db=mock_db_session,
        user_id=1,
        currency_from="USD",
        currency_to="EUR",
        amount=50,
    )

    # Validar resultados
    assert result["success"] == True
    assert "result" in result
    mock_db_session.add.assert_called_once()
    mock_db_session.commit.assert_called_once()

# Caso 2: Usuario no encontrado
def test_process_exchange_user_not_found(mock_db_session):
    # No se encuentra el usuario
    mock_db_session.query.return_value.filter.return_value.first.return_value = None

    with pytest.raises(ValueError, match="User not found"):
        process_exchange(
            db=mock_db_session,
            user_id=1,
            currency_from="USD",
            currency_to="EUR",
            amount=50,
        )


# Caso 3: Monto excede el límite diario
def test_process_exchange_exceeds_daily_limit(mock_db_session):
    # Crear un usuario con límite diario bajo
    user = User(id=1, name="Test User", email="test@example.com", daily_limit=10.0)
    mock_db_session.query.return_value.filter.return_value.first.return_value = user

    with pytest.raises(ValueError, match="Amount exceeds daily limit"):
        process_exchange(
            db=mock_db_session,
            user_id=1,
            currency_from="USD",
            currency_to="EUR",
            amount=50,
        )