"""Appointment API router"""

from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from .. import api_responses
from .. import base_api_models
from .. import constants
from .. import helpers
from ..database import main
from .constants import (
    TAGS,
    ADD_APPOINTMENT_OPERATION_ID,
    DELETE_APPOINTMENT_BY_ID_OPERATION_ID,
    GET_APPOINTMENTS_OPERATION_ID,
    GET_APPOINTMENT_BY_ID_OPERATION_ID,
    PATCH_APPOINTMENT_OPERATION_ID,
    UPDATE_APPOINTMENT_OPERATION_ID,
)
from . import handlers
from . import models as appointment_api_models


router = APIRouter()


@router.get(
    "/",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_PRIORITIES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_APPOINTMENTS_OPERATION_ID,
    response_model=appointment_api_models.AppointmentsListResponse,
    responses=api_responses.responses_descriptions,
)
def get_appointments(
    offset: int = Query(default=constants.DEFAULT_PAGE_OFFSET, ge=0),
    limit: int = Query(default=constants.DEFAULT_PAGE_LIMIT, ge=1),
    session: Session = Depends(main.get_session),
) -> appointment_api_models.AppointmentsListResponse:
    """
    Gets a list of appointments
    """
    return handlers.get_appointments(session, offset, limit)


@router.get(
    "/{appointment_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_PRIORITIES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_APPOINTMENT_BY_ID_OPERATION_ID,
    response_model=base_api_models.Appointment,
    responses=api_responses.responses_descriptions,
)
def get_appointment_by_id(
    appointment_id: int, session: Session = Depends(main.get_session)
) -> base_api_models.Appointment:
    """
    Get info of an existing appointment by Id
    """
    return handlers.get_appointment_by_id(session, appointment_id)


@router.post(
    "/",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_PRIORITIES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=ADD_APPOINTMENT_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    status_code=status.HTTP_201_CREATED,
    responses=api_responses.responses_descriptions,
)
def add_appointment(
    payload: appointment_api_models.CreateAppointmentPayload,
    session: Session = Depends(main.get_session),
) -> base_api_models.APIResponse:
    """
    Add a new appointment
    """
    return handlers.add_appointment(session, payload)


@router.put(
    "/{appointment_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_PRIORITIES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=UPDATE_APPOINTMENT_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    responses=api_responses.responses_descriptions,
)
def update_appointment(
    appointment_id: int,
    payload: appointment_api_models.UpdateAppointmentPayload,
    session: Session = Depends(main.get_session),
) -> base_api_models.APIResponse:
    """
    Update an existing appointment by Id
    """
    return handlers.update_appointment(session, appointment_id, payload)


@router.patch(
    "/{appointment_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_PRIORITIES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=PATCH_APPOINTMENT_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    responses=api_responses.responses_descriptions,
)
def patch_appointment(
    appointment_id: int,
    payload: appointment_api_models.PatchAppointmentPayload,
    session: Session = Depends(main.get_session),
) -> base_api_models.APIResponse:
    """
    Update partially an existing appointment by Id
    """
    return handlers.partially_update_appointment(session, appointment_id, payload)


@router.delete(
    "/{appointment_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_PRIORITIES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=DELETE_APPOINTMENT_BY_ID_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    responses=api_responses.responses_descriptions,
)
def delete_appointment_by_id(
    appointment_id: int, session: Session = Depends(main.get_session)
) -> base_api_models.APIResponse:
    """
    Delete an existing appointment by Id
    """
    return handlers.get_appointment_by_id(session, appointment_id)
