"""Service API service"""

from datetime import datetime
from sqlalchemy import select, func
from sqlalchemy.orm import Session
from .. import constants
from ..database import models as db_models
from ..enums import StatusType
from . import models as api_models

# pylint: disable=W0613
# pylint: disable=E1102


def get_service_by_id(session: Session, service_id: int) -> db_models.Service:
    """Gets a service by id

    Args:
        session (Session):  Database session
        service_id (int): ID of service

    Returns:
        db_models.Service: The matched service
    """
    statement = (
        select(db_models.Service).where(db_models.Service.id == service_id).limit(1)
    )
    return session.scalars(statement).one()


def get_status_by_code_and_type(
    session: Session, code: str, status_type: StatusType
) -> db_models.Status:
    """Gets a status by code and type

    Args:
        session (Session):  Database session
        code (str): Code of the status item
        status_type (StatusType): type of the status

    Returns:
        db_models.Status: The matched status
    """
    statement = (
        select(db_models.Status)
        .where(db_models.Status.code == code)
        .where(db_models.Status.type == status_type)
        .limit(1)
    )
    return session.scalars(statement).one()


def get_priority_by_code(session: Session, code: str) -> db_models.Priority:
    """Gets a priority item by code

    Args:
        session (Session):  Database session
        code (str): Code of the priority item

    Returns:
        db_models.Priority: The matched priority item
    """
    statement = (
        select(db_models.Priority).where(db_models.Priority.code == code).limit(1)
    )
    return session.scalars(statement).one()


def get_total_turns_for_service_id(session: Session, service_id: int) -> int:
    """Gets the total of turns for the given service

    Args:
        session (Session):  Database session
        service_id (int): ID of service

    Returns:
        int: The total of turns
    """
    return session.scalar(
        select(func.count(db_models.ServiceTurn.id)).filter(
            db_models.ServiceTurn.service_id == service_id
        )
    )


def create_service_turn(
    session: Session,
    application: str,
    service_id: int,
    item: api_models.CreateServiceTurnPayload,
) -> db_models.ServiceTurn:
    """Creates a service turn for the given service

    Args:
        session (Session):  Database session
        application (str, optional): The application in context.
        service_id (int): ID of service to create a turn from
        item (api_models.CreateServiceTurnPayload): The required payload

    Returns:
        db_models.ServiceTurn: Created service turn
    """
    service = get_service_by_id(session, service_id)
    turns_count = get_total_turns_for_service_id(session, service_id)
    status = get_status_by_code_and_type(
        session, constants.DEFAULT_TURN_STATUS, StatusType.TURN
    )
    priority = get_priority_by_code(session, constants.DEFAULT_TURN_PRIORITY)
    current_datetime = datetime.now()
    turn = db_models.ServiceTurn(
        customer_name=item.customerName,
        service_id=service.id,
        ticket_number=f"{service.prefix}-{turns_count + 1}",
        created_by=constants.SYSTEM_CREATOR,
        last_modified=current_datetime,
        created=current_datetime,
        status_id=status.id,
        priority_id=priority.id,
    )
    session.add_all([turn])
    session.commit()
    return turn
