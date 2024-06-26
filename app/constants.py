"""General constants"""

# pylint: disable=C0301

BEARER_PORTION = "Bearer "
IS_AUTHORIZED_PROPERTY = "isAuthorized"
IS_VALID_PROPERTY = "isValid"
SCOPE_PROPERTY = "scope"
SCOPES_SEPARATOR = " "
API_KEYS_SEPARATOR = ","
IP_ADDRESSES_SEPARATOR = ","
EMPTY_VALUE = ""
TIMEOUT = 10
SYSTEM_CREATOR = "SYSTEM"
DEFAULT_TURN_STATUS = "PENDING"
DEFAULT_APPOINTMENT_STATUS = "PENDING"
DEFAULT_TURN_PRIORITY = "NORMAL_PRIORITY"
NOT_AVAILABLE = "N/A"

DEFAULT_PAGE_OFFSET = 0
DEFAULT_PAGE_LIMIT = 10

# Scopes START

# Read status information
READ_STATUSES_SCOPE = "read_statuses"
# Create, modify and delete status information
WRITE_STATUSES_SCOPE = "write_statuses"
# Administrate status information
ADMIN_STATUSES_SCOPE = "admin_statuses"

# Read priority information
READ_PRIORITIES_SCOPE = "read_priorities"
# Create, modify and delete priority information
WRITE_PRIORITIES_SCOPE = "write_priorities"
# Administrate priority information
ADMIN_PRIORITIES_SCOPE = "admin_priorities"

# Read category information
READ_CATEGORIES_SCOPE = "read_categories"
# Create, modify and delete category information
WRITE_CATEGORIES_SCOPE = "write_categories"
# Administrate category information
ADMIN_CATEGORIES_SCOPE = "admin_categories"

# Read service information
READ_SERVICES_SCOPE = "read_services"
# Create, modify and delete service information
WRITE_SERVICES_SCOPE = "write_services"
# Administrate service information
ADMIN_SERVICES_SCOPE = "admin_services"

# Read services turns information
READ_SERVICE_TURNS_SCOPE = "read_serviceturns"
# Create, modify and delete services turns information
WRITE_SERVICE_TURNS_SCOPE = "write_serviceturns"
# Administrate services turns information
ADMIN_SERVICE_TURNS_SCOPE = "admin_serviceturns"

# Read customer information
READ_CUSTOMERS_SCOPE = "read_customers"
# Create, modify and delete customer information
WRITE_CUSTOMERS_SCOPE = "write_customers"
# Administrate customer information
ADMIN_CUSTOMERS_SCOPE = "admin_customers"
# Read own customer information
READ_OWN_CUSTOMER_SCOPE = "read_own_profile"

# Read customers' appointments information
READ_APPOINTMENTS_SCOPE = "read_appointments"
# Read own appointments information
READ_OWN_APPOINTMENTS_SCOPE = "read_own_appointments"
# Create own appointments information
CREATE_OWN_APPOINTMENTS_SCOPE = "create_own_appointments"
# Create, modify and delete customers' appointments information
WRITE_APPOINTMENTS_SCOPE = "write_appointments"
# Administrate customers' appointments information
ADMIN_APPOINTMENTS_SCOPE = "admin_appointments"

# Read queue information
READ_QUEUES_SCOPE = "read_queues"
# Create, modify and delete queue information
WRITE_QUEUES_SCOPE = "write_queues"
# Administrate queue
ADMIN_QUEUES_SCOPE = "admin_queues"

# Read location information
READ_LOCATIONS_SCOPE = "read_locations"
# Create, modify and delete location information
WRITE_LOCATIONS_SCOPE = "write_locations"
# Administrate location
ADMIN_LOCATIONS_SCOPE = "admin_locations"

# Scopes END

# API Metadata
API_TITLE = "QMS Core API"
API_SUMMARY = "API for QMS Core functionality."
API_DESCRIPTION = "The API for the QMS Core functionality."
API_VERSION = "1.0.0"

# API routes prefixes
APPOINTMENTS_ROUTE_PREFIX = "/api/v1/appointments"
CATEGORIES_ROUTE_PREFIX = "/api/v1/categories"
CUSTOMERS_ROUTE_PREFIX = "/api/v1/customers"
PRIORITIES_ROUTE_PREFIX = "/api/v1/priorities"
QUEUES_ROUTE_PREFIX = "/api/v1/queues"
SERVICES_ROUTE_PREFIX = "/api/v1/services"
SERVICE_TURNS_ROUTE_PREFIX = "/api/v1/serviceturns"
STATUSES_ROUTE_PREFIX = "/api/v1/statuses"
LOCATIONS_ROUTE_PREFIX = "/api/v1/locations"

# Environment names
AUTH_API_BASE_URL_ENV_NAME = "AUTH_API_BASE_URL"
APP_CLIENT_ID_ENV_NAME = "APP_CLIENT_ID"
APP_CLIENT_SECRET_ENV_NAME = "APP_CLIENT_SECRET"
IAM_API_KEY_ENV_NAME = "IAM_API_KEY"
AUTH_ALLOWED_IP_ADDRESSES_ENV_NAME = "AUTH_ALLOWED_IP_ADDRESSES"
AUTH_ALLOWED_API_KEYS_ENV_NAME = "AUTH_ALLOWED_API_KEYS"
DB_CONNECTION_STRING_ENV_NAME = "DB_CONNECTION_STRING"

# Error messages
INTERNAL_SERVER_ERROR_MESSAGE = "Internal Server Error"
REVIEW_REQUEST_ERROR_MESSAGE = "Please, review your request and try later."
INVALID_TOKEN_ERROR_MESSAGE = "Invalid token. Please review your request."
FORBIDDEN_ERROR_MESSAGE = "Client doen't have permission to request this resource"
UNAUTHORIZED_ERROR_MESSAGE = "Client is not authenticated against the API"
NOT_FOUND_ERROR_MESSAGE = "Item not found. Please review your request."
INVALID_STATUS_ERROR_MESSAGE = "Invalid status type provided."
CONFLICT_ERROR_MESSAGE = "Request could not be processed because of conflict in the current state of the resource."
INVALID_REQUEST = "INVALID_REQUEST"

UNEXPECTED_ERROR_TYPE = "UNEXPECTED_ERROR"
INVALID_TOKEN_ERROR_TYPE = "INVALID_TOKEN"
UNAUTHORIZED_ERROR_TYPE = "UNAUTHORIZED"
NOT_FOUND_ERROR_TYPE = "NOT_FOUND"
FORBIDDEN_ERROR_TYPE = "FORBIDDEN"
NOT_FOUND_ERROR_TYPE = "NOT_FOUND"
INVALID_STATUS_ERROR_TYPE = "INVALID_STATUS_TYPE"
CONFLICT_ERROR_TYPE = "CONFLICT"
DUPLICATE_KEYWORD = "Duplicate"

# Operations
OPERATION_DELETE = "DELETE"
OPERATION_ADD = "ADD"
OPERATION_UPDATE = "UPDATE"

# Success messages
ITEM_DELETED_SUCCESSFULLY_MESSAGE = "Item deleted successfully"
ITEM_ADDED_SUCCESSFULLY_MESSAGE = "Item added successfully"
ITEM_UPDATED_SUCCESSFULLY_MESSAGE = "Item updated successfully"

# Statuses API description
HTTP_400_DESCRIPTION = "Client is sending an incorrect format of API request"
HTTP_422_DESCRIPTION = (
    "The server was unable to process the request because it contains invalid data"
)
HTTP_401_DESCRIPTION = "Client is not authenticated against the API"
HTTP_403_DESCRIPTION = "Client doesn't have permission to request this resource"
HTTP_404_DESCRIPTION = "Resource could not be found"
HTTP_409_DESCRIPTION = "Request could not be processed because of conflict in the current state of the resource"
HTTP_500_DESCRIPTION = "Unexpected internal error"
