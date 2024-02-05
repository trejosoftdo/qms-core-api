"""Priority API router"""

from fastapi import APIRouter, Depends
from .. import base_api_models
from .. import constants
from .. import helpers
from .constants import (
    TAGS,
    ADD_PRIORITY_OPERATION_ID,
    DELETE_PRIORITY_BY_ID_OPERATION_ID,
    GET_PRIORITIES_OPERATION_ID,
    GET_PRIORITY_BY_ID_OPERATION_ID,
    PATCH_PRIORITY_OPERATION_ID,
    UPDATE_PRIORITY_OPERATION_ID,
)
from . import handlers
from . import models as priority_api_models


router = APIRouter()


@router.get(
    "/",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_PRIORITIES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_PRIORITIES_OPERATION_ID,
    response_model=priority_api_models.PrioritiesListResponse,
)
def get_priorities(
    active: bool = True,
    offset: int = 0,
    limit: int = 10,
) -> priority_api_models.PrioritiesListResponse:
    """
    Gets a list of priorities
    """
    return handlers.get_priorities(active, offset, limit)


@router.get(
    "/{priority_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_PRIORITIES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_PRIORITY_BY_ID_OPERATION_ID,
    response_model=base_api_models.Priority,
)
def get_priority_by_id(priority_id: int) -> base_api_models.Priority:
    """
    Get info of an existing priority by Id
    """
    return handlers.get_priority_by_id(priority_id)


@router.post(
    "/",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_PRIORITIES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=ADD_PRIORITY_OPERATION_ID,
    response_model=base_api_models.APIResponse,
)
def add_priority(
    payload: priority_api_models.CreatePriorityPayload,
) -> base_api_models.APIResponse:
    """
    Add a new priority
    """
    return handlers.add_priority(payload)


@router.put(
    "/{priority_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_PRIORITIES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=UPDATE_PRIORITY_OPERATION_ID,
    response_model=base_api_models.APIResponse,
)
def update_priority(
    priority_id: int, payload: priority_api_models.UpdatePriorityPayload
) -> base_api_models.APIResponse:
    """
    Update an existing priority by Id
    """
    return handlers.update_priority(priority_id, payload)


@router.patch(
    "/{priority_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_PRIORITIES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=PATCH_PRIORITY_OPERATION_ID,
    response_model=base_api_models.APIResponse,
)
def patch_priority(
    priority_id: int, payload: priority_api_models.PatchPriorityPayload
) -> base_api_models.APIResponse:
    """
    Update partially an existing priority by Id
    """
    return handlers.partially_update_priority(priority_id, payload)


@router.delete(
    "/{priority_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_PRIORITIES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=DELETE_PRIORITY_BY_ID_OPERATION_ID,
    response_model=base_api_models.APIResponse,
)
def delete_priority_by_id(priority_id: int) -> base_api_models.APIResponse:
    """
    Delete an existing priority by Id
    """
    return handlers.get_priority_by_id(priority_id)