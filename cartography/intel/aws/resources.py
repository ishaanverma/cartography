from typing import Callable
from typing import Dict

from . import apigateway
from . import config
from . import dynamodb
from . import ecr
from . import ecs
from . import eks
from . import elasticache
from . import elasticsearch
from . import emr
from . import iam
from . import identitycenter
from . import inspector
from . import kms
from . import lambda_function
from . import permission_relationships
from . import rds
from . import redshift
from . import resourcegroupstaggingapi
from . import route53
from . import s3
from . import secretsmanager
from . import securityhub
from . import sqs
from . import ssm
from .ec2.auto_scaling_groups import sync_ec2_auto_scaling_groups
from .ec2.elastic_ip_addresses import sync_elastic_ip_addresses
from .ec2.images import sync_ec2_images
from .ec2.instances import sync_ec2_instances
from .ec2.internet_gateways import sync_internet_gateways
from .ec2.key_pairs import sync_ec2_key_pairs
from .ec2.launch_templates import sync_ec2_launch_templates
from .ec2.load_balancer_v2s import sync_load_balancer_v2s
from .ec2.load_balancers import sync_load_balancers
from .ec2.network_acls import sync_network_acls
from .ec2.network_interfaces import sync_network_interfaces
from .ec2.reserved_instances import sync_ec2_reserved_instances
from .ec2.security_groups import sync_ec2_security_groupinfo
from .ec2.snapshots import sync_ebs_snapshots
from .ec2.subnets import sync_subnets
from .ec2.tgw import sync_transit_gateways
from .ec2.volumes import sync_ebs_volumes
from .ec2.vpc import sync_vpc
from .ec2.vpc_peerings import sync_vpc_peerings
from .iam_instance_profiles import sync_iam_instance_profiles

RESOURCE_FUNCTIONS: Dict[str, Callable[..., None]] = {
    'iam': iam.sync,
    'iaminstanceprofiles': sync_iam_instance_profiles,
    's3': s3.sync,
    'dynamodb': dynamodb.sync,
    'ec2:launch_templates': sync_ec2_launch_templates,
    'ec2:autoscalinggroup': sync_ec2_auto_scaling_groups,
    # `ec2:instance` must be included before `ssm` and `ec2:images`,
    # they rely on EC2Instance data provided by this module.
    'ec2:instance': sync_ec2_instances,
    'ec2:images': sync_ec2_images,
    'ec2:keypair': sync_ec2_key_pairs,
    'ec2:load_balancer': sync_load_balancers,
    'ec2:load_balancer_v2': sync_load_balancer_v2s,
    'ec2:network_acls': sync_network_acls,
    'ec2:network_interface': sync_network_interfaces,
    'ec2:security_group': sync_ec2_security_groupinfo,
    'ec2:subnet': sync_subnets,
    'ec2:tgw': sync_transit_gateways,
    'ec2:vpc': sync_vpc,
    'ec2:vpc_peering': sync_vpc_peerings,
    'ec2:internet_gateway': sync_internet_gateways,
    'ec2:reserved_instances': sync_ec2_reserved_instances,
    'ec2:volumes': sync_ebs_volumes,
    'ec2:snapshots': sync_ebs_snapshots,
    'ecr': ecr.sync,
    'ecs': ecs.sync,
    'eks': eks.sync,
    'elasticache': elasticache.sync,
    'elastic_ip_addresses': sync_elastic_ip_addresses,
    'emr': emr.sync,
    'lambda_function': lambda_function.sync,
    'kms': kms.sync,
    'rds': rds.sync,
    'redshift': redshift.sync,
    'route53': route53.sync,
    'elasticsearch': elasticsearch.sync,
    'permission_relationships': permission_relationships.sync,
    'resourcegroupstaggingapi': resourcegroupstaggingapi.sync,
    'apigateway': apigateway.sync,
    'secretsmanager': secretsmanager.sync,
    'securityhub': securityhub.sync,
    'sqs': sqs.sync,
    'ssm': ssm.sync,
    'inspector': inspector.sync,
    'config': config.sync,
    'identitycenter': identitycenter.sync_identity_center_instances,
}

AWS_REGIONS = {
    'us-east-1',
    'us-east-2',
    'us-west-1',
    'us-west-2',
    'af-south-1',
    'ap-east-1',
    'ap-south-1',
    'ap-south-2',
    'ap-southeast-1',
    'ap-southeast-2',
    'ap-southeast-3',
    'ap-southeast-4',
    'ap-southeast-5',
    'ap-southeast-7',
    'ap-northeast-1',
    'ap-northeast-2',
    'ap-northeast-3',
    'ca-west-1',
    'eu-central-1',
    'eu-west-1',
    'eu-west-2',
    'eu-west-3',
    'eu-south-1',
    'eu-south-2',
    'eu-north-1',
    'eu-central-2',
    'il-central-1',
    'mx-central-1',
    'me-south-1',
    'me-central-1',
    'sa-east-1',
    'us-gov-east-1',
    'us-gov-west-1',
}
