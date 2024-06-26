"""Entry point"""

from fastapi import FastAPI, Request, status as status_codes, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import IntegrityError
from . import constants
from . import api_responses
from .appointment import router as appointment
from .category import router as category
from .customer import router as customer
from .priority import router as priority
from .queue import router as queue
from .service import router as service
from .service_turn import router as service_turn
from .status import router as status
from .location import router as location


app = FastAPI(
    title=constants.API_TITLE,
    description=constants.API_DESCRIPTION,
    summary=constants.API_SUMMARY,
    version=constants.API_VERSION,
)

# pylint: disable=W0613



@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    """Handles HTTP exceptions

    Args:
        request (Request): HTTP Request
        exc (HTTPException): HTTP Exception

    Returns:
        JSONResponse: Error response
    """
    print(exc)
    return JSONResponse(
        status_code=exc.status_code,
        content=api_responses.get_response_from_exception(exc).__dict__,
    )

@app.exception_handler(IntegrityError)
def integrity_error_handler(request: Request, exc: IntegrityError):
    """Database integrity error handler

    Args:
        request (Request): HTTP Request
        exc (IntegrityError): Database integrity error

    Returns:
        JSONResponse: Error response
    """
    print(exc)
    return JSONResponse(
        status_code=status_codes.HTTP_400_BAD_REQUEST,
        content=api_responses.get_validation_error_response(
            constants.REVIEW_REQUEST_ERROR_MESSAGE
        ).__dict__,
    )

@app.exception_handler(RequestValidationError)
def request_validation_error_handler(request: Request, exc: RequestValidationError):
    """Request validation error handler

    Args:
        request (Request): HTTP Request
        exc (RequestValidationError): Request validation error

    Returns:
        JSONResponse: Error response
    """
    errors = [f"{err['msg']} ({'.'.join(err['loc'])})" for err in exc.errors()]
    message = ". ".join(errors)
    print(exc)
    return JSONResponse(
        status_code=status_codes.HTTP_400_BAD_REQUEST,
        content=api_responses.get_validation_error_response(message).__dict__,
    )


app.include_router(appointment.router, prefix=constants.APPOINTMENTS_ROUTE_PREFIX)
app.include_router(category.router, prefix=constants.CATEGORIES_ROUTE_PREFIX)
app.include_router(customer.router, prefix=constants.CUSTOMERS_ROUTE_PREFIX)
app.include_router(priority.router, prefix=constants.PRIORITIES_ROUTE_PREFIX)
app.include_router(queue.router, prefix=constants.QUEUES_ROUTE_PREFIX)
app.include_router(service.router, prefix=constants.SERVICES_ROUTE_PREFIX)
app.include_router(status.router, prefix=constants.STATUSES_ROUTE_PREFIX)
app.include_router(service_turn.router, prefix=constants.SERVICE_TURNS_ROUTE_PREFIX)
app.include_router(location.router, prefix=constants.LOCATIONS_ROUTE_PREFIX)
