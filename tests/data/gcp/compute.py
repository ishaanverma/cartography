# flake8: noqa
VPC_RESPONSE = {
    "id": "projects/project-abc/global/networks",
    "items": [
        {
            "autoCreateSubnetworks": True,
            "creationTimestamp": "2018-05-10T17:33:18.968-07:00",
            "description": "Default network for the project",
            "id": "123456",
            "kind": "compute#network",
            "name": "default",
            "routingConfig": {
                "routingMode": "REGIONAL",
            },
            "selfLink": "https://www.googleapis.com/compute/v1/projects/project-abc/global/networks/default",
            "subnetworks": [
                "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west2/subnetworks/default",
                "https://www.googleapis.com/compute/v1/projects/project-abc/regions/asia-east2/subnetworks/default",
                "https://www.googleapis.com/compute/v1/projects/project-abc/regions/asia-east1/subnetworks/default",
                "https://www.googleapis.com/compute/v1/projects/project-abc/regions/us-east1/subnetworks/default",
                "https://www.googleapis.com/compute/v1/projects/project-abc/regions/northamerica-northeast1/subnetworks/default",
                "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west1/subnetworks/default",
                "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west3/subnetworks/default",
                "https://www.googleapis.com/compute/v1/projects/project-abc/regions/asia-south1/subnetworks/default",
                "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west4/subnetworks/default",
                "https://www.googleapis.com/compute/v1/projects/project-abc/regions/asia-southeast1/subnetworks/default",
                "https://www.googleapis.com/compute/v1/projects/project-abc/regions/us-west2/subnetworks/default",
                "https://www.googleapis.com/compute/v1/projects/project-abc/regions/us-central1/subnetworks/default",
                "https://www.googleapis.com/compute/v1/projects/project-abc/regions/asia-northeast2/subnetworks/default",
                "https://www.googleapis.com/compute/v1/projects/project-abc/regions/us-east4/subnetworks/default",
                "https://www.googleapis.com/compute/v1/projects/project-abc/regions/us-west1/subnetworks/default",
                "https://www.googleapis.com/compute/v1/projects/project-abc/regions/southamerica-east1/subnetworks/default",
                "https://www.googleapis.com/compute/v1/projects/project-abc/regions/asia-northeast1/subnetworks/default",
                "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west6/subnetworks/default",
                "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-north1/subnetworks/default",
                "https://www.googleapis.com/compute/v1/projects/project-abc/regions/australia-southeast1/subnetworks/default",
            ],
        },
    ],
    "kind": "compute#networkList",
    "selfLink": "https://www.googleapis.com/compute/v1/projects/project-abc/global/networks",
}

VPC_SUBNET_RESPONSE = {
    "id": "projects/project-abc/regions/europe-west2/subnetworks",
    "items": [
        {
            "creationTimestamp": "2018-05-10T17:33:24.446-07:00",
            "fingerprint": "!@#$%ASDF",
            "gatewayAddress": "10.0.0.1",
            "id": "98765",
            "ipCidrRange": "10.0.0.0/20",
            "kind": "compute#subnetwork",
            "name": "default",
            "network": "https://www.googleapis.com/compute/v1/projects/project-abc/global/networks/default",
            "privateIpGoogleAccess": False,
            "region": "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west2",
            "selfLink": "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west2/subnetworks/default",
        },
    ],
    "kind": "compute#subnetworkList",
    "selfLink": "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west2/subnetworks",
}

GCP_LIST_INSTANCES_RESPONSE = {
    "id": "projects/project-abc/zones/europe-west2-b/instances",
    "items": [
        {
            "canIpForward": False,
            "cpuPlatform": "Intel Haswell",
            "creationTimestamp": "2018-02-16T10:42:04.362-08:00",
            "deletionProtection": True,
            "description": "",
            "disks": [
                {
                    "autoDelete": True,
                    "boot": True,
                    "deviceName": "instance-1",
                    "guestOsFeatures": [
                        {
                            "type": "VIRTIO_SCSI_MULTIQUEUE",
                        },
                    ],
                    "index": 0,
                    "interface": "SCSI",
                    "kind": "compute#attachedDisk",
                    "licenses": [
                        "https://www.googleapis.com/compute/v1/projects/project-that-has-license/global/licenses/ubuntu-1404-trusty",
                    ],
                    "mode": "READ_WRITE",
                    "source": "https://www.googleapis.com/compute/v1/projects/project-abc/zones/europe-west2-b/disks/instance-1",
                    "type": "PERSISTENT",
                },
            ],
            "id": "1234",
            "kind": "compute#instance",
            "labelFingerprint": "fingerprint1234=",
            "machineType": "https://www.googleapis.com/compute/v1/projects/project-abc/zones/europe-west2-b/machineTypes/n1-standard-1",
            "metadata": {
                "fingerprint": "fingerprint2345",
                "kind": "compute#metadata",
            },
            "name": "instance-1",
            "networkInterfaces": [
                {
                    "accessConfigs": [
                        {
                            "kind": "compute#accessConfig",
                            "name": "External NAT",
                            "natIP": "1.2.3.4",
                            "networkTier": "PREMIUM",
                            "type": "ONE_TO_ONE_NAT",
                        },
                    ],
                    "fingerprint": "fingerprint-3456",
                    "kind": "compute#networkInterface",
                    "name": "nic0",
                    "network": "https://www.googleapis.com/compute/v1/projects/project-abc/global/networks/default",
                    "networkIP": "10.0.0.2",
                    "subnetwork": "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west2/subnetworks/default",
                },
            ],
            "scheduling": {
                "automaticRestart": True,
                "onHostMaintenance": "MIGRATE",
                "preemptible": False,
            },
            "selfLink": "https://www.googleapis.com/compute/v1/projects/project-abc/zones/europe-west2-b/instances/instance-1",
            "serviceAccounts": [
                {
                    "email": "my-svc-account@developer.gserviceaccount.com",
                    "scopes": [
                        "https://www.googleapis.com/auth/devstorage.read_only",
                        "https://www.googleapis.com/auth/logging.write",
                        "https://www.googleapis.com/auth/monitoring.write",
                        "https://www.googleapis.com/auth/servicecontrol",
                        "https://www.googleapis.com/auth/service.management.readonly",
                        "https://www.googleapis.com/auth/trace.append",
                    ],
                },
            ],
            "startRestricted": False,
            "status": "RUNNING",
            "tags": {
                "fingerprint": "fingerprint3456",
                "items": ["test"],
            },
            "zone": "https://www.googleapis.com/compute/v1/projects/project-abc/zones/europe-west2-b",
        },
        {
            "canIpForward": True,
            "cpuPlatform": "Intel Haswell",
            "creationTimestamp": "2018-04-19T05:24:54.903-07:00",
            "deletionProtection": False,
            "description": "",
            "disks": [
                {
                    "autoDelete": True,
                    "boot": True,
                    "deviceName": "instance-1-test",
                    "guestOsFeatures": [
                        {
                            "type": "VIRTIO_SCSI_MULTIQUEUE",
                        },
                    ],
                    "index": 0,
                    "interface": "SCSI",
                    "kind": "compute#attachedDisk",
                    "licenses": [
                        "https://www.googleapis.com/compute/v1/projects/project-that-has-license/global/licenses/ubuntu-1404-trusty",
                    ],
                    "mode": "READ_WRITE",
                    "source": "https://www.googleapis.com/compute/v1/projects/project-abc/zones/europe-west2-b/disks/instance-1-test",
                    "type": "PERSISTENT",
                },
            ],
            "id": "2345",
            "kind": "compute#instance",
            "labelFingerprint": "fingerprint1234=",
            "machineType": "https://www.googleapis.com/compute/v1/projects/project-abc/zones/europe-west2-b/machineTypes/n1-standard-1",
            "metadata": {
                "fingerprint": "fingerprint2345",
                "kind": "compute#metadata",
            },
            "name": "instance-1-test",
            "networkInterfaces": [
                {
                    "accessConfigs": [
                        {
                            "kind": "compute#accessConfig",
                            "name": "External NAT",
                            "natIP": "1.3.4.5",
                            "networkTier": "PREMIUM",
                            "type": "ONE_TO_ONE_NAT",
                        },
                    ],
                    "fingerprint": "fingerprint4567",
                    "kind": "compute#networkInterface",
                    "name": "nic0",
                    "network": "https://www.googleapis.com/compute/v1/projects/project-abc/global/networks/default",
                    "networkIP": "10.0.0.3",
                    "subnetwork": "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west2/subnetworks/default",
                },
            ],
            "scheduling": {
                "automaticRestart": True,
                "onHostMaintenance": "MIGRATE",
                "preemptible": False,
            },
            "selfLink": "https://www.googleapis.com/compute/v1/projects/project-abc/zones/europe-west2-b/instances/instance-1-test",
            "serviceAccounts": [
                {
                    "email": "my-svc-account@developer.gserviceaccount.com",
                    "scopes": [
                        "https://www.googleapis.com/auth/devstorage.read_only",
                        "https://www.googleapis.com/auth/logging.write",
                        "https://www.googleapis.com/auth/monitoring.write",
                        "https://www.googleapis.com/auth/servicecontrol",
                        "https://www.googleapis.com/auth/service.management.readonly",
                        "https://www.googleapis.com/auth/trace.append",
                    ],
                },
            ],
            "startRestricted": False,
            "status": "RUNNING",
            "tags": {
                "fingerprint": "fingerprint1234=",
            },
            "zone": "https://www.googleapis.com/compute/v1/projects/project-abc/zones/europe-west2-b",
        },
    ],
    "kind": "compute#instanceList",
    "selfLink": "https://www.googleapis.com/compute/v1/projects/project-abc/zones/europe-west2-b/instances",
}

TRANSFORMED_GCP_VPCS = [
    {
        "partial_uri": "projects/project-abc/global/networks/default",
        "name": "default",
        "self_link": "https://www.googleapis.com/compute/v1/projects/project-abc/global/networks/default",
        "project_id": "project-abc",
        "auto_create_subnetworks": True,
        "description": "Default network for the project",
        "routing_config_routing_mode": "REGIONAL",
    },
]

TRANSFORMED_GCP_SUBNETS = [
    {
        "id": "projects/project-abc/regions/europe-west2/subnetworks/default",
        "partial_uri": "projects/project-abc/regions/europe-west2/subnetworks/default",
        "name": "default",
        "vpc_self_link": "https://www.googleapis.com/compute/v1/projects/project-abc/global/networks/default",
        "vpc_partial_uri": "projects/project-abc/global/networks/default",
        "project_id": "project-abc",
        "region": "europe-west2",
        "gateway_address": "10.0.0.1",
        "ip_cidr_range": "10.0.0.0/20",
        "self_link": "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west2/subnetworks/default",
        "private_ip_google_access": False,
    },
]

TRANSFORMED_GCP_INSTANCES = [
    {
        "canIpForward": False,
        "cpuPlatform": "Intel Haswell",
        "creationTimestamp": "2018-02-16T10:42:04.362-08:00",
        "deletionProtection": True,
        "description": "",
        "disks": [
            {
                "autoDelete": True,
                "boot": True,
                "deviceName": "instance-1",
                "guestOsFeatures": [
                    {
                        "type": "VIRTIO_SCSI_MULTIQUEUE",
                    },
                ],
                "index": 0,
                "interface": "SCSI",
                "kind": "compute#attachedDisk",
                "licenses": [
                    "https://www.googleapis.com/compute/v1/projects/project-that-has-license/global/licenses/ubuntu-1404-trusty",
                ],
                "mode": "READ_WRITE",
                "source": "https://www.googleapis.com/compute/v1/projects/project-abc/zones/europe-west2-b/disks/instance-1",
                "type": "PERSISTENT",
            },
        ],
        "id": "1234",
        "kind": "compute#instance",
        "labelFingerprint": "fingerprint1234=",
        "machineType": "https://www.googleapis.com/compute/v1/projects/project-abc/zones/europe-west2-b/machineTypes/n1-standard-1",
        "metadata": {
            "fingerprint": "fingerprint2345",
            "kind": "compute#metadata",
        },
        "name": "instance-1",
        "networkInterfaces": [
            {
                "accessConfigs": [
                    {
                        "kind": "compute#accessConfig",
                        "name": "External NAT",
                        "natIP": "1.2.3.4",
                        "networkTier": "PREMIUM",
                        "type": "ONE_TO_ONE_NAT",
                    },
                ],
                "fingerprint": "fingerprint-3456",
                "kind": "compute#networkInterface",
                "name": "nic0",
                "network": "https://www.googleapis.com/compute/v1/projects/project-abc/global/networks/default",
                "vpc_partial_uri": "projects/project-abc/global/networks/default",
                "networkIP": "10.0.0.2",
                "subnetwork": "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west2/subnetworks/default",
                "subnet_partial_uri": "projects/project-abc/regions/europe-west2/subnetworks/default",
            },
        ],
        "scheduling": {
            "automaticRestart": True,
            "onHostMaintenance": "MIGRATE",
            "preemptible": False,
        },
        "selfLink": "https://www.googleapis.com/compute/v1/projects/project-abc/zones/europe-west2-b/instances/instance-1",
        "serviceAccounts": [
            {
                "email": "my-svc-account@developer.gserviceaccount.com",
                "scopes": [
                    "https://www.googleapis.com/auth/devstorage.read_only",
                    "https://www.googleapis.com/auth/logging.write",
                    "https://www.googleapis.com/auth/monitoring.write",
                    "https://www.googleapis.com/auth/servicecontrol",
                    "https://www.googleapis.com/auth/service.management.readonly",
                    "https://www.googleapis.com/auth/trace.append",
                ],
            },
        ],
        "startRestricted": False,
        "status": "RUNNING",
        "tags": {
            "fingerprint": "fingerprint3456",
            "items": ["test"],
        },
        "zone": "https://www.googleapis.com/compute/v1/projects/project-abc/zones/europe-west2-b",
        "partial_uri": "projects/project-abc/zones/europe-west2-b/instances/instance-1",
        "project_id": "project-abc",
        "zone_name": "europe-west2-b",
    },
    {
        "canIpForward": True,
        "cpuPlatform": "Intel Haswell",
        "creationTimestamp": "2018-04-19T05:24:54.903-07:00",
        "deletionProtection": False,
        "description": "",
        "disks": [
            {
                "autoDelete": True,
                "boot": True,
                "deviceName": "instance-1-test",
                "guestOsFeatures": [
                    {
                        "type": "VIRTIO_SCSI_MULTIQUEUE",
                    },
                ],
                "index": 0,
                "interface": "SCSI",
                "kind": "compute#attachedDisk",
                "licenses": [
                    "https://www.googleapis.com/compute/v1/projects/project-that-has-license/global/licenses/ubuntu-1404-trusty",
                ],
                "mode": "READ_WRITE",
                "source": "https://www.googleapis.com/compute/v1/projects/project-abc/zones/europe-west2-b/disks/instance-1-test",
                "type": "PERSISTENT",
            },
        ],
        "id": "2345",
        "kind": "compute#instance",
        "labelFingerprint": "fingerprint1234=",
        "machineType": "https://www.googleapis.com/compute/v1/projects/project-abc/zones/europe-west2-b/machineTypes/n1-standard-1",
        "metadata": {
            "fingerprint": "fingerprint2345",
            "kind": "compute#metadata",
        },
        "name": "instance-1-test",
        "networkInterfaces": [
            {
                "accessConfigs": [
                    {
                        "kind": "compute#accessConfig",
                        "name": "External NAT",
                        "natIP": "1.3.4.5",
                        "networkTier": "PREMIUM",
                        "type": "ONE_TO_ONE_NAT",
                    },
                ],
                "fingerprint": "fingerprint4567",
                "kind": "compute#networkInterface",
                "name": "nic0",
                "network": "https://www.googleapis.com/compute/v1/projects/project-abc/global/networks/default",
                "vpc_partial_uri": "projects/project-abc/global/networks/default",
                "networkIP": "10.0.0.3",
                "subnetwork": "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west2/subnetworks/default",
                "subnet_partial_uri": "projects/project-abc/regions/europe-west2/subnetworks/default",
            },
        ],
        "scheduling": {
            "automaticRestart": True,
            "onHostMaintenance": "MIGRATE",
            "preemptible": False,
        },
        "selfLink": "https://www.googleapis.com/compute/v1/projects/project-abc/zones/europe-west2-b/instances/instance-1-test",
        "serviceAccounts": [
            {
                "email": "my-svc-account@developer.gserviceaccount.com",
                "scopes": [
                    "https://www.googleapis.com/auth/devstorage.read_only",
                    "https://www.googleapis.com/auth/logging.write",
                    "https://www.googleapis.com/auth/monitoring.write",
                    "https://www.googleapis.com/auth/servicecontrol",
                    "https://www.googleapis.com/auth/service.management.readonly",
                    "https://www.googleapis.com/auth/trace.append",
                ],
            },
        ],
        "startRestricted": False,
        "status": "RUNNING",
        "tags": {
            "fingerprint": "fingerprint1234=",
        },
        "zone": "https://www.googleapis.com/compute/v1/projects/project-abc/zones/europe-west2-b",
        "partial_uri": "projects/project-abc/zones/europe-west2-b/instances/instance-1-test",
        "project_id": "project-abc",
        "zone_name": "europe-west2-b",
    },
]

LIST_FIREWALLS_RESPONSE = {
    "id": "projects/project-abc/global/firewalls",
    "items": [
        {
            "allowed": [
                {
                    "IPProtocol": "icmp",
                },
            ],
            "creationTimestamp": "2018-05-10T17:33:45.769-07:00",
            "description": "Allow ICMP from anywhere",
            "direction": "INGRESS",
            "disabled": False,
            "id": "121212",
            "kind": "compute#firewall",
            "logConfig": {
                "enable": False,
            },
            "name": "default-allow-icmp",
            "network": "https://www.googleapis.com/compute/v1/projects/project-abc/global/networks/default",
            "priority": 65534,
            "selfLink": "https://www.googleapis.com/compute/v1/projects/project-abc/global/firewalls/default-allow-icmp",
            "sourceRanges": ["0.0.0.0/0"],
        },
        {
            "allowed": [
                {
                    "IPProtocol": "tcp",
                    "ports": ["0-65535"],
                },
                {
                    "IPProtocol": "udp",
                    "ports": ["0-65535"],
                },
                {
                    "IPProtocol": "icmp",
                },
            ],
            "creationTimestamp": "2018-05-10T17:33:45.754-07:00",
            "description": "Allow internal traffic on the default network",
            "direction": "INGRESS",
            "disabled": False,
            "id": "131313",
            "kind": "compute#firewall",
            "logConfig": {
                "enable": False,
            },
            "name": "default-allow-internal",
            "network": "https://www.googleapis.com/compute/v1/projects/project-abc/global/networks/default",
            "priority": 65534,
            "selfLink": "https://www.googleapis.com/compute/v1/projects/project-abc/global/firewalls/default-allow-internal",
            "sourceRanges": ["10.128.0.0/9"],
        },
        {
            "allowed": [
                {
                    "IPProtocol": "tcp",
                    "ports": ["3389"],
                },
            ],
            "creationTimestamp": "2018-05-10T17:33:45.764-07:00",
            "description": "Allow RDP from anywhere",
            "direction": "INGRESS",
            "disabled": False,
            "id": "141414",
            "kind": "compute#firewall",
            "logConfig": {
                "enable": False,
            },
            "name": "default-allow-rdp",
            "network": "https://www.googleapis.com/compute/v1/projects/project-abc/global/networks/default",
            "priority": 65534,
            "selfLink": "https://www.googleapis.com/compute/v1/projects/project-abc/global/firewalls/default-allow-rdp",
            "sourceRanges": ["0.0.0.0/0"],
        },
        {
            "allowed": [
                {
                    "IPProtocol": "tcp",
                    "ports": ["22"],
                },
            ],
            "creationTimestamp": "2018-05-10T17:33:45.759-07:00",
            "description": "Allow SSH from anywhere",
            "direction": "INGRESS",
            "disabled": False,
            "id": "151515",
            "kind": "compute#firewall",
            "logConfig": {
                "enable": False,
            },
            "name": "default-allow-ssh",
            "network": "https://www.googleapis.com/compute/v1/projects/project-abc/global/networks/default",
            "priority": 65534,
            "selfLink": "https://www.googleapis.com/compute/v1/projects/project-abc/global/firewalls/default-allow-ssh",
            "sourceRanges": ["0.0.0.0/0"],
        },
        {
            "allowed": [
                {
                    "IPProtocol": "tcp",
                    "ports": ["9000-9001"],
                },
            ],
            "creationTimestamp": "2019-02-08T10:03:14.422-08:00",
            "description": "",
            "direction": "INGRESS",
            "disabled": False,
            "id": "161616",
            "kind": "compute#firewall",
            "logConfig": {
                "enable": True,
            },
            "name": "custom-port-incoming",
            "network": "https://www.googleapis.com/compute/v1/projects/project-abc/global/networks/default",
            "priority": 1000,
            "selfLink": "https://www.googleapis.com/compute/v1/projects/project-abc/global/firewalls/custom-port-incoming",
            "sourceRanges": ["0.0.0.0/0"],
            "targetTags": ["test"],
        },
    ],
    "kind": "compute#firewallList",
    "selfLink": "https://www.googleapis.com/compute/v1/projects/project-abc/global/firewalls",
}

TRANSFORMED_FW_LIST = [
    {
        "allowed": [
            {
                "IPProtocol": "icmp",
            },
        ],
        "creationTimestamp": "2018-05-10T17:33:45.769-07:00",
        "description": "Allow ICMP from anywhere",
        "direction": "INGRESS",
        "disabled": False,
        "id": "projects/project-abc/global/firewalls/default-allow-icmp",
        "kind": "compute#firewall",
        "logConfig": {
            "enable": False,
        },
        "name": "default-allow-icmp",
        "network": "https://www.googleapis.com/compute/v1/projects/project-abc/global/networks/default",
        "priority": 65534,
        "selfLink": "https://www.googleapis.com/compute/v1/projects/project-abc/global/firewalls/default-allow-icmp",
        "sourceRanges": ["0.0.0.0/0"],
        "transformed_allow_list": [
            {
                "fromport": None,
                "protocol": "icmp",
                "ruleid": "projects/project-abc/global/firewalls/default-allow-icmp/allow/icmp",
                "toport": None,
            },
        ],
        "transformed_deny_list": [],
        "vpc_partial_uri": "projects/project-abc/global/networks/default",
        "has_target_service_accounts": False,
    },
    {
        "allowed": [
            {
                "IPProtocol": "tcp",
                "ports": ["0-65535"],
            },
            {
                "IPProtocol": "udp",
                "ports": ["0-65535"],
            },
            {
                "IPProtocol": "icmp",
            },
        ],
        "creationTimestamp": "2018-05-10T17:33:45.754-07:00",
        "description": "Allow internal traffic on the default network",
        "direction": "INGRESS",
        "disabled": False,
        "id": "projects/project-abc/global/firewalls/default-allow-internal",
        "kind": "compute#firewall",
        "logConfig": {
            "enable": False,
        },
        "name": "default-allow-internal",
        "network": "https://www.googleapis.com/compute/v1/projects/project-abc/global/networks/default",
        "priority": 65534,
        "selfLink": "https://www.googleapis.com/compute/v1/projects/project-abc/global/firewalls/default-allow-internal",
        "sourceRanges": ["10.128.0.0/9"],
        "transformed_allow_list": [
            {
                "fromport": 0,
                "protocol": "tcp",
                "ruleid": "projects/project-abc/global/firewalls/default-allow-internal/allow/0to65535tcp",
                "toport": 65535,
            },
            {
                "fromport": 0,
                "protocol": "udp",
                "ruleid": "projects/project-abc/global/firewalls/default-allow-internal/allow/0to65535udp",
                "toport": 65535,
            },
            {
                "fromport": None,
                "protocol": "icmp",
                "ruleid": "projects/project-abc/global/firewalls/default-allow-internal/allow/icmp",
                "toport": None,
            },
        ],
        "transformed_deny_list": [],
        "vpc_partial_uri": "projects/project-abc/global/networks/default",
        "has_target_service_accounts": False,
    },
    {
        "allowed": [
            {
                "IPProtocol": "tcp",
                "ports": ["3389"],
            },
        ],
        "creationTimestamp": "2018-05-10T17:33:45.764-07:00",
        "description": "Allow RDP from anywhere",
        "direction": "INGRESS",
        "disabled": False,
        "id": "projects/project-abc/global/firewalls/default-allow-rdp",
        "kind": "compute#firewall",
        "logConfig": {
            "enable": False,
        },
        "name": "default-allow-rdp",
        "network": "https://www.googleapis.com/compute/v1/projects/project-abc/global/networks/default",
        "priority": 65534,
        "selfLink": "https://www.googleapis.com/compute/v1/projects/project-abc/global/firewalls/default-allow-rdp",
        "sourceRanges": ["0.0.0.0/0"],
        "transformed_allow_list": [
            {
                "fromport": 3389,
                "protocol": "tcp",
                "ruleid": "projects/project-abc/global/firewalls/default-allow-rdp/allow/3389tcp",
                "toport": 3389,
            },
        ],
        "transformed_deny_list": [],
        "vpc_partial_uri": "projects/project-abc/global/networks/default",
        "has_target_service_accounts": False,
    },
    {
        "allowed": [
            {
                "IPProtocol": "tcp",
                "ports": ["22"],
            },
        ],
        "creationTimestamp": "2018-05-10T17:33:45.759-07:00",
        "description": "Allow SSH from anywhere",
        "direction": "INGRESS",
        "disabled": False,
        "id": "projects/project-abc/global/firewalls/default-allow-ssh",
        "kind": "compute#firewall",
        "logConfig": {
            "enable": False,
        },
        "name": "default-allow-ssh",
        "network": "https://www.googleapis.com/compute/v1/projects/project-abc/global/networks/default",
        "priority": 65534,
        "selfLink": "https://www.googleapis.com/compute/v1/projects/project-abc/global/firewalls/default-allow-ssh",
        "sourceRanges": ["0.0.0.0/0"],
        "transformed_allow_list": [
            {
                "fromport": 22,
                "protocol": "tcp",
                "ruleid": "projects/project-abc/global/firewalls/default-allow-ssh/allow/22tcp",
                "toport": 22,
            },
        ],
        "transformed_deny_list": [],
        "vpc_partial_uri": "projects/project-abc/global/networks/default",
        "has_target_service_accounts": False,
    },
    {
        "allowed": [
            {
                "IPProtocol": "tcp",
                "ports": ["9000-9001"],
            },
        ],
        "creationTimestamp": "2019-02-08T10:03:14.422-08:00",
        "description": "",
        "direction": "INGRESS",
        "disabled": False,
        "id": "projects/project-abc/global/firewalls/custom-port-incoming",
        "kind": "compute#firewall",
        "logConfig": {
            "enable": True,
        },
        "name": "custom-port-incoming",
        "network": "https://www.googleapis.com/compute/v1/projects/project-abc/global/networks/default",
        "priority": 1000,
        "selfLink": "https://www.googleapis.com/compute/v1/projects/project-abc/global/firewalls/custom-port-incoming",
        "sourceRanges": ["0.0.0.0/0"],
        "targetTags": ["test"],
        "transformed_allow_list": [
            {
                "fromport": 9000,
                "protocol": "tcp",
                "ruleid": "projects/project-abc/global/firewalls/custom-port-incoming/allow/9000to9001tcp",
                "toport": 9001,
            },
        ],
        "transformed_deny_list": [],
        "vpc_partial_uri": "projects/project-abc/global/networks/default",
        "has_target_service_accounts": False,
    },
]

LIST_FORWARDING_RULES_RESPONSE = {
    "id": "projects/project-abc/regions/europe-west2/forwardingRules",
    "items": [
        {
            "id": "11111111",
            "creationTimestamp": "2019-11-22T06:05:37.254-08:00",
            "name": "internal-service-1111",
            "description": "my-k8s-internal-service",
            "region": "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west2",
            "IPAddress": "10.0.0.10",
            "IPProtocol": "TCP",
            "ports": [
                "80",
            ],
            "selfLink": "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west2/forwardingRules/internal-service-1111",
            "loadBalancingScheme": "INTERNAL",
            "subnetwork": "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west2/subnetworks/default",
            "network": "https://www.googleapis.com/compute/v1/projects/project-abc/global/networks/default",
            "backendService": "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west2/backendServices/backend-service-1111",
            "networkTier": "PREMIUM",
            "target": "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west2/targetPools/node-pool-12345",
            "fingerprint": "12345678",
            "kind": "compute#forwardingRule",
        },
        {
            "id": "12121212",
            "creationTimestamp": "2019-03-30T14:02:47.050-07:00",
            "name": "public-ingress-controller-1234567",
            "description": "ingress-controller",
            "region": "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west2",
            "IPAddress": "1.2.3.11",
            "IPProtocol": "TCP",
            "portRange": "80-443",
            "target": "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west2/targetPools/node-pool-12345",
            "selfLink": "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west2/forwardingRules/public-ingress-controller-1234567",
            "loadBalancingScheme": "EXTERNAL",
            "networkTier": "PREMIUM",
            "target": "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west2/targetVpnGateways/vpn-12345",
            "fingerprint": "123456789",
            "kind": "compute#forwardingRule",
        },
        {
            "id": "13131313",
            "creationTimestamp": "2020-08-12T03:18:41.743-07:00",
            "name": "shard-server-22222",
            "description": "shard-server",
            "region": "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west2",
            "IPAddress": "10.0.0.20",
            "IPProtocol": "TCP",
            "ports": [
                "10203",
            ],
            "selfLink": "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west2/forwardingRules/shard-server-22222",
            "loadBalancingScheme": "INTERNAL",
            "subnetwork": "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west2/subnetworks/default",
            "network": "https://www.googleapis.com/compute/v1/projects/project-abc/global/networks/default",
            "backendService": "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west1/backendServices/backend-service-111234",
            "networkTier": "PREMIUM",
            "target": "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west2/targetPools/node-pool-234567",
            "fingerprint": "1234567",
            "kind": "compute#forwardingRule",
        },
    ],
    "selfLink": "https://www.googleapis.com/compute/v1/projects/project-abc/regions/europe-west4/forwardingRules",
    "kind": "compute#forwardingRuleList",
}
