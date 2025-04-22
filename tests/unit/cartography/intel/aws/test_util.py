import pytest

from cartography.intel.aws.util.common import parse_and_validate_aws_regions
from cartography.intel.aws.util.common import parse_and_validate_aws_requested_syncs


def test_parse_and_validate_requested_syncs():
    no_spaces = "ec2:instance,s3,rds,iam"
    assert parse_and_validate_aws_requested_syncs(no_spaces) == ['ec2:instance', 's3', 'rds', 'iam']

    mismatch_spaces = 'ec2:subnet, eks,kms'
    assert parse_and_validate_aws_requested_syncs(mismatch_spaces) == ['ec2:subnet', 'eks', 'kms']

    sync_that_does_not_exist = 'lambda_function, thisfuncdoesnotexist, route53'
    with pytest.raises(ValueError):
        parse_and_validate_aws_requested_syncs(sync_that_does_not_exist)

    absolute_garbage = '#@$@#RDFFHKjsdfkjsd,KDFJHW#@,'
    with pytest.raises(ValueError):
        parse_and_validate_aws_requested_syncs(absolute_garbage)


def test_parse_and_validate_aws_regions():
    no_spaces = "us-west-1,us-west-2,us-east-1"
    assert parse_and_validate_aws_regions(no_spaces) == ['us-west-1', 'us-west-2', 'us-east-1']

    mismatch_spaces = 'us-west-1, us-west-2,us-east-1'
    assert parse_and_validate_aws_regions(mismatch_spaces) == ['us-west-1', 'us-west-2', 'us-east-1']

    region_that_does_not_exist = 'us-west-1, us-west-2, us-east-3'
    with pytest.raises(ValueError):
        parse_and_validate_aws_regions(region_that_does_not_exist)

    absolute_garbage = '#@$@#RDFFHKjsdfkjsd,KDFJHW#@,'
    with pytest.raises(ValueError):
        parse_and_validate_aws_regions(absolute_garbage)
