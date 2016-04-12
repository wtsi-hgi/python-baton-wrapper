from hgicommon.enums import ComparisonOperator

from baton.models import AccessControl

BATON_DATA_OBJECT_PROPERTY = "data_object"
BATON_COLLECTION_PROPERTY = "collection"

BATON_COLLECTION_CONTENTS = "contents"

BATON_REPLICA_PROPERTY = "replicates"
BATON_REPLICA_NUMBER_PROPERTY = "number"
BATON_REPLICA_VALID_PROPERTY = "valid"
BATON_REPLICA_CHECKSUM_PROPERTY = "checksum"
BATON_REPLICA_LOCATION_PROPERTY = "location"
BATON_REPLICA_RESOURCE_PROPERTY = "resource"

BATON_ACL_PROPERTY = "access"
BATON_ACL_OWNER_PROPERTY = "owner"
BATON_ACL_LEVEL_PROPERTY = "level"
BATON_ACL_LEVELS = {
    AccessControl.Level.NONE: "null",
    AccessControl.Level.OWN: "own",
    AccessControl.Level.READ: "read",
    AccessControl.Level.WRITE: "write"
}

BATON_AVU_PROPERTY = "avus"
BATON_AVU_ATTRIBUTE_PROPERTY = "attribute"
BATON_AVU_VALUE_PROPERTY = "value"

BATON_SEARCH_CRITERIA_PROPERTY = "avus"
BATON_SEARCH_CRITERION_ATTRIBUTE_PROPERTY = "attribute"
BATON_SEARCH_CRITERION_VALUE_PROPERTY = "value"
BATON_SEARCH_CRITERION_COMPARISON_OPERATOR_PROPERTY = "o"
BATON_SEARCH_CRITERION_COMPARISON_OPERATORS = {
    ComparisonOperator.EQUALS: "=",
    ComparisonOperator.GREATER_THAN: ">",
    ComparisonOperator.LESS_THAN: "<"
}

BATON_SPECIFIC_QUERY_PROPERTY = "specific"
BATON_SPECIFIC_QUERY_ALIAS_PROPERTY = "alias"
BATON_SPECIFIC_QUERY_ARGUMENTS_PROPERTY = "args"
BATON_SPECIFIC_QUERY_SQL_PROPERTY = "sqlStr"

BATON_ERROR_PROPERTY = "error"
BATON_ERROR_MESSAGE_KEY = "message"
BATON_ERROR_CODE_KEY = "code"
BATON_ERROR_ENTITY_DOES_NOT_EXIST_ERROR_CODE = -310000
BATON_ERROR_CATALOG_ALREADY_HAS_ITEM_BY_THAT_NAME = -809000
BATON_ERROR_CAT_SUCCESS_BUT_WITH_NO_INFO = -819000
BATON_ERROR_CAT_INVALID_ARGUMENT = -816000

IRODS_SPECIFIC_QUERY_LS = "ls"
IRODS_SPECIFIC_QUERY_FIND_QUERY_BY_ALIAS = "findQueryByAlias"

BATON_METAMOD_ADD_OPERATION = "add"
BATON_METAMOD_REMOVE_OPERATION = "rem"
