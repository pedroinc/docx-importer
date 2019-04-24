import pytest
from doc_processor import DocProcessor


def test_file_name_valid_if_match_license():
    is_valid = DocProcessor.file_name_valid(' KMV 3966 ANYCAR.doc')
    assert is_valid


def test_file_name_fails_if_cant_match_license():
    assert DocProcessor.file_name_valid('MARIA.doc') is None

