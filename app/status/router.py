"""Status API router"""

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from .. import api_responses
from .. import base_api_models
from .. import constants
from .. import helpers
from ..database import main
from .constants import (
    TAGS,
    ADD_STATUS_OPERATION_ID,
    DELETE_STATUS_BY_ID_OPERATION_ID,
    GET_STATUSES_OPERATION_ID,
    GET_STATUS_BY_ID_OPERATION_ID,
    PATCH_STATUS_OPERATION_ID,
    UPDATE_STATUS_OPERATION_ID,
)
from . import handlers
from . import models as status_api_models


router = APIRouter()


@router.get(
    "/",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_STATUSES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_STATUSES_OPERATION_ID,
    response_model=status_api_models.StatusesListResponse,
    responses=api_responses.responses_descriptions,
)
def get_statuses(
    active: bool = True,
    offset: int = Query(default=constants.DEFAULT_PAGE_OFFSET, ge=0),
    limit: int = Query(default=constants.DEFAULT_PAGE_LIMIT, ge=1),
    session: Session = Depends(main.get_session),
) -> status_api_models.StatusesListResponse:
    """
    Gets a list of statuses
    """
    return handlers.get_statuses(session, active, offset, limit)


@router.get(
    "/{status_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_STATUSES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_STATUS_BY_ID_OPERATION_ID,
    response_model=base_api_models.Status,
    responses=api_responses.responses_descriptions,
)
def get_status_by_id(
    status_id: int, session: Session = Depends(main.get_session)
) -> base_api_models.Status:
    """
    Get info of an existing status by Id
    """
    return handlers.get_status_by_id(session, status_id)


@router.post(
    "/",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_STATUSES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=ADD_STATUS_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    status_code=status.HTTP_201_CREATED,
    responses=api_responses.responses_descriptions,
)
def add_status(
    payload: status_api_models.CreateStatusPayload,
    session: Session = Depends(main.get_session),
) -> base_api_models.APIResponse:
    """
    Add a new status
    """
    return handlers.add_status(session, payload)


@router.put(
    "/{status_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_STATUSES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=UPDATE_STATUS_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    responses=api_responses.responses_descriptions,
)
def update_status(
    status_id: int,
    payload: status_api_models.UpdateStatusPayload,
    session: Session = Depends(main.get_session),
) -> base_api_models.APIResponse:
    """
    Update an existing status by Id
    """
    return handlers.update_status(session, status_id, payload)


@router.patch(
    "/{status_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_STATUSES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=PATCH_STATUS_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    responses=api_responses.responses_descriptions,
)
def patch_status(
    status_id: int,
    payload: status_api_models.PatchStatusPayload,
    session: Session = Depends(main.get_session),
) -> base_api_models.APIResponse:
    """
    Update partially an existing status by Id
    """
    return handlers.partially_update_status(session, status_id, payload)


@router.delete(
    "/{status_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_STATUSES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=DELETE_STATUS_BY_ID_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    responses=api_responses.responses_descriptions,
)
def delete_status_by_id(
    status_id: int, session: Session = Depends(main.get_session)
) -> base_api_models.APIResponse:
    """
    Delete an existing status by Id
    """
    return handlers.delete_status_by_id(session, status_id)
