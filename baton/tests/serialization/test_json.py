import json
import unittest

from frozendict import frozendict

from baton.serialization.json import DataObjectReplicaJSONEncoder, AccessControlJSONEncoder, DataObjectJSONEncoder, \
    IrodsMetadataJSONEncoder, AccessControlJSONDecoder, DataObjectReplicaJSONDecoder, IrodsMetadataJSONDecoder, \
    DataObjectJSONDecoder, DataObjectReplicaCollectionJSONEncoder, DataObjectReplicaCollectionJSONDecoder
from baton.tests.serialization._helpers import create_data_object_with_baton_json_representation


class TestAccessControlJSONEncoder(unittest.TestCase):
    """
    Tests for `AccessControlJSONEncoder`.
    """
    def setUp(self):
        self.data_object, self.data_object_as_json = create_data_object_with_baton_json_representation()
        self.access_control = self.data_object.acl[0]
        self.access_control_as_json = self.data_object_as_json["access"][0]

    def test_default(self):
        encoded = AccessControlJSONEncoder().default(self.access_control)
        self.assertEqual(encoded, self.access_control_as_json)

    def test_with_json_dumps(self):
        encoded = json.dumps(self.access_control, cls=AccessControlJSONEncoder)
        self.assertEqual(json.loads(encoded), self.access_control_as_json)


class TestAccessControlJSONDecoder(unittest.TestCase):
    """
    Tests for `AccessControlJSONDecoder`.
    """
    def setUp(self):
        self.data_object, self.data_object_as_json = create_data_object_with_baton_json_representation()
        self.access_control = self.data_object.acl[0]
        self.access_control_as_json_string = json.dumps(self.data_object_as_json["access"][0])

    def test_decode(self):
        decoded = AccessControlJSONDecoder().decode(self.access_control_as_json_string)
        self.assertEqual(decoded, self.access_control)

    def test_with_json_loads(self):
        decoded = json.loads(self.access_control_as_json_string, cls=AccessControlJSONDecoder)
        self.assertEqual(decoded, self.access_control)


class TestDataObjectReplicaJSONEncoder(unittest.TestCase):
    """
    Tests for `DataObjectReplicaJSONEncoder`.
    """
    def setUp(self):
        self.data_object, self.data_object_as_json = create_data_object_with_baton_json_representation()
        self.replica = self.data_object.replicas.get_by_number(1)
        self.replica_as_json = self.data_object_as_json["replicates"][0]
        assert self.replica_as_json["number"] == 1

    def test_default(self):
        encoded = DataObjectReplicaJSONEncoder().default(self.replica)
        self.assertEqual(encoded, self.replica_as_json)

    def test_with_json_dumps(self):
        encoded = json.dumps(self.replica, cls=DataObjectReplicaJSONEncoder)
        self.assertEqual(json.loads(encoded), self.replica_as_json)


class TestDataObjectReplicaJSONDecoder(unittest.TestCase):
    """
    Tests for `DataObjectReplicaJSONDecoder`.
    """
    def setUp(self):
        self.data_object, self.data_object_as_json = create_data_object_with_baton_json_representation()
        self.replica = self.data_object.replicas.get_by_number(1)
        self.replica_as_json_string = json.dumps(self.data_object_as_json["replicates"][0])

    def test_decode(self):
        decoded = DataObjectReplicaJSONDecoder().decode(self.replica_as_json_string)
        self.assertEqual(decoded, self.replica)

    def test_with_json_loads(self):
        decoded = json.loads(self.replica_as_json_string, cls=DataObjectReplicaJSONDecoder)
        self.assertEqual(decoded, self.replica)


class TestDataObjectReplicaCollectionJSONEncoder(unittest.TestCase):
    """
    Tests for `DataObjectReplicaCollectionJSONDecoder`.
    """
    def setUp(self):
        self.data_object, self.data_object_as_json = create_data_object_with_baton_json_representation()
        self.replicas = self.data_object.replicas
        self.replicas_as_json = self.data_object_as_json["replicates"]

    def test_default(self):
        encoded = DataObjectReplicaCollectionJSONEncoder().default(self.replicas)
        self.assertEqual(encoded, self.replicas_as_json)

    def test_with_json_dumps(self):
        encoded = json.dumps(self.replicas, cls=DataObjectReplicaCollectionJSONEncoder)
        self.assertEqual(json.loads(encoded), self.replicas_as_json)


class TestDataObjectReplicaCollectionJSONDecoder(unittest.TestCase):
    """
    Tests for `DataObjectReplicaCollectionJSONDecoder`.
    """
    def setUp(self):
        self.data_object, self.data_object_as_json = create_data_object_with_baton_json_representation()
        self.replicas = self.data_object.replicas
        self.replicas_as_json_as_string = json.dumps(self.data_object_as_json["replicates"])

    def test_decode(self):
        decoded = DataObjectReplicaCollectionJSONDecoder().decode(self.replicas_as_json_as_string)
        self.assertEqual(decoded, self.replicas)

    def test_with_json_loads(self):
        decoded = json.loads(self.replicas_as_json_as_string, cls=DataObjectReplicaCollectionJSONDecoder)
        self.assertEqual(decoded, self.replicas)


class TestIrodsMetadataJSONEncoder(unittest.TestCase):
    """
    Tests for `IrodsMetadataJSONEncoder`.
    """
    def setUp(self):
        self.data_object, self.data_object_as_json = create_data_object_with_baton_json_representation()
        self.metadata = self.data_object.metadata
        self.metadata_as_json= self.data_object_as_json["avus"]

    def test_default(self):
        encoded = IrodsMetadataJSONEncoder().default(self.metadata)
        self.assertCountEqual(encoded, self.metadata_as_json)

    def test_with_json_dumps(self):
        encoded = json.dumps(self.metadata_as_json, cls=IrodsMetadataJSONEncoder)
        self.assertCountEqual(json.loads(encoded), self.metadata_as_json)


class TestIrodsMetadataJSONDecoder(unittest.TestCase):
    """
    Tests for `IrodsMetadataJSONDecoder`.
    """
    def setUp(self):
        self.data_object, self.data_object_as_json = create_data_object_with_baton_json_representation()
        self.metadata = self.data_object.metadata
        self.metadata_as_json_string = json.dumps(self.data_object_as_json["avus"])

    def test_decode(self):
        decoded = IrodsMetadataJSONDecoder().decode(self.metadata_as_json_string)
        self.assertEqual(decoded, self.metadata)

    def test_with_json_loads(self):
        decoded = json.loads(self.metadata_as_json_string, cls=IrodsMetadataJSONDecoder)
        self.assertEqual(decoded, self.metadata)


class TestDataObjectJSONEncoder(unittest.TestCase):
    """
    Tests for `DataObjectJSONEncoder`.
    """
    def setUp(self):
        self.data_object, self.data_object_as_json = create_data_object_with_baton_json_representation()
        self.maxDiff = None

    def test_default(self):
        encoded = DataObjectJSONEncoder().default(self.data_object)
        self._assert_data_object_as_json_equal(encoded, self.data_object_as_json)

    def test_with_json_dumps(self):
        encoded = json.dumps(self.data_object, cls=DataObjectJSONEncoder)
        self._assert_data_object_as_json_equal(json.loads(encoded), self.data_object_as_json)

    def _assert_data_object_as_json_equal(self, target: dict, actual: dict):
        """
        Assert that two JSON representations of `DataObject` instances are equal.
        :param target: the data object to check
        :param actual: the data object to check against
        """
        TestDataObjectJSONEncoder._fix_set_as_list_in_json_issue(target)
        TestDataObjectJSONEncoder._fix_set_as_list_in_json_issue(actual)
        self.assertEqual(target, actual)

    @staticmethod
    def _fix_set_as_list_in_json_issue(data_object_as_json: dict):
        """
        Work around issue that (unordered) set is represented as (ordered) list in JSON
        :param data_object_as_json: a JSON representation of a `DataObject` instance
        """
        avus = set()
        for avu in data_object_as_json["avus"]:
            # Using `frozendict` as a hashable dict
            avus.add(frozendict(avu))

        data_object_as_json["avus"] = avus


class TestDataObjectJSONDecoder(unittest.TestCase):
    """
    Tests for `DataObjectJSONDecoder`.
    """
    def setUp(self):
        self.data_object, self.data_object_as_json = create_data_object_with_baton_json_representation()
        self.data_object_as_json_string = json.dumps(self.data_object_as_json)

    def test_decode(self):
        decoded = DataObjectJSONDecoder().decode(self.data_object_as_json_string)
        self.assertEqual(decoded, self.data_object)

    def test_with_json_loads(self):
        decoded = json.loads(self.data_object_as_json_string, cls=DataObjectJSONDecoder)
        self.assertEqual(decoded, self.data_object)


if __name__ == "__main__":
    unittest.main()
