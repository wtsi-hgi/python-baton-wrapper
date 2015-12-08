from hgicommon.enums import ComparisonOperator

from baton.models import AccessControl

BATON_DATA_OBJECT_PROPERTY = "data_object"
BATON_COLLECTION_PROPERTY = "collection"

BATON_METADATA_PROPERTY = "avus"
BATON_CHECKSUM_PROPERTY = "checksum"

BATON_FILE_REPLICATE_PROPERTY = "replicates"
BATON_FILE_REPLICATE_ID_PROPERTY = "number"

BATON_ACL_PROPERTY = "access"
BATON_ACL_OWNER_PROPERTY = "owner"
BATON_ACL_ZONE_PROPERTY = "zone"
BATON_ACL_LEVEL_PROPERTY = "level"
BATON_ACL_LEVELS = {
    AccessControl.Level.OWN: "own",
    AccessControl.Level.READ: "read",
}

BATON_AVU_SEARCH_PROPERTY = "avus"
BATON_ATTRIBUTE_PROPERTY = "attribute"
BATON_VALUE_PROPERTY = "value"
BATON_COMPARISON_OPERATOR_PROPERTY = "o"
BATON_COMPARISON_OPERATORS = {
    ComparisonOperator.EQUALS: "=",
    ComparisonOperator.GREATER_THAN: ">",
    ComparisonOperator.LESS_THAN: "<"
}

BATON_ERROR_PROPERTY = "error"
BATON_ERROR_MESSAGE_KEY = "message"
BATON_ERROR_CODE_KEY = "code"
BATON_FILE_DOES_NOT_EXIST_ERROR_CODE = -310000
