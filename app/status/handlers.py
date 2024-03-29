"""Status API handlers"""

from .. import base_api_models
from .. import api_responses
from ..database import models as db_models
from .. import mappers
from . import models as status_api_models


def get_statuses(
    active: bool, offset: int, limit: int
) -> status_api_models.StatusesListResponse:
    """Get list of statuses

    Args:
        active (bool): Flag to return only active records.
        offset (int): The items to skip before collecting the result set.
        limit (int): The items to return.

    Returns:
        StatusesListResponse: List of statuses
    """
    items = db_models.Status.find_paginated(
        limit, offset, lambda x: x.where(db_models.Status.is_active == active)
    )
    return list(map(mappers.map_status, items))


def get_status_by_id(status_id: int) -> base_api_models.Status:
    """Get info of an existing status by Id

    Args:
        status_id (int): id of the status

    Returns:
        Status: Status for id
    """
    item = db_models.Status.find_by_id(status_id)
    return mappers.map_status(item)


def delete_status_by_id(status_id: int) -> base_api_models.APIResponse:
    """Delete an existing status by Id

    Args:
        status_id (int): id of the status

    Returns:
        APIResponse: The result of the deletion
    """
    db_models.Status.delete_by_id(status_id)
    return api_responses.ITEM_DELETED_RESPONSE


def add_status(
    payload: status_api_models.CreateStatusPayload,
) -> base_api_models.APIResponse:
    """Add a new status

    Args:
        payload (CreateStatusPayload): payload to create status

    Returns:
        APIResponse: The result of the addition
    """
    db_models.Status.create_from_data(payload.dict())
    return api_responses.ITEM_ADDED_RESPONSE


def update_status(
    status_id: int, payload: status_api_models.UpdateStatusPayload
) -> base_api_models.APIResponse:
    """Update an existing status by Id

    Args:
        status_id (int): id of the status to update
        payload (UpdateStatusPayload): payload to update status

    Returns:
        APIResponse: The result of the update
    """
    db_models.Status.update_by_id(status_id, payload.dict())
    return api_responses.ITEM_UPDATED_RESPONSE


def partially_update_status(
    status_id: int, payload: status_api_models.PatchStatusPayload
) -> base_api_models.APIResponse:
    """Partially updates an existing status by Id

    Args:
        status_id (int): id of the status to partially update
        payload (PatchStatusPayload): payload to update status

    Returns:
        APIResponse: The result of the update
    """
    db_models.Status.update_by_id(status_id, payload.dict())
    return api_responses.ITEM_UPDATED_RESPONSE
