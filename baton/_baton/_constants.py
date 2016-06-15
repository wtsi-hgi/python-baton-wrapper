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

BATON_TIMESTAMP_PROPERTY = "timestamps"
BATON_TIMESTAMP_CREATED_PROPERTY = "created"
BATON_TIMESTAMP_LAST_MODIFIED_PROPERTY = "modified"
BATON_TIMESTAMP_REPLICA_NUMBER_LINK_PROPERTY = "replicates"

BATON_ACL_PROPERTY = "access"
BATON_ACL_OWNER_PROPERTY = "owner"
BATON_ACL_ZONE_PROPERTY = "zone"
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
IRODS_ERROR_USER_FILE_DOES_NOT_EXIST = -310000
IRODS_ERROR_CATALOG_ALREADY_HAS_ITEM_BY_THAT_NAME = -809000
IRODS_ERROR_CAT_SUCCESS_BUT_WITH_NO_INFO = -819000
IRODS_ERROR_CAT_INVALID_ARGUMENT = -816000

IRODS_SPECIFIC_QUERY_LS = "ls"
IRODS_SPECIFIC_QUERY_FIND_QUERY_BY_ALIAS = "findQueryByAlias"

BATON_METAMOD_OPERATION_FLAG = "--operation"
BATON_METAMOD_OPERATION_ADD = "add"
BATON_METAMOD_OPERATION_REMOVE = "rem"
BATON_LIST_AVU_FLAG = "--avu"
BATON_LIST_ACCESS_CONTROLS_FLAG = "--acl"
BATON_CHMOD_RECURSIVE_FLAG = "--recurse"
