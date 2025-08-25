import json
from pathlib import Path

from protodocs._proto_specification import generate_proto_specification

import testpb_pb2  # noqa: F401


def test_all_parameter_types_match_armeria():
    serialized_descriptors = (Path(__file__).parent / "descriptorset.pb").read_bytes()
    spec = generate_proto_specification(
        ["armeria.grpc.testing.TestService"], serialized_descriptors
    )

    with open(Path(__file__).parent / "armeria-spec.json", "r") as f:
        armeria_spec = json.load(f)

    assert spec.to_json() == armeria_spec
