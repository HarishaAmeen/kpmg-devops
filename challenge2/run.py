import requests
import json

class EC2Metadata:

    def __init__(self):

        self._session = requests.Session()
        self.metadata_url = "http://169.254.169.254/latest/meta-data"

    def _get_url(self, url):
        return self._session.get(url, timeout=1.0)

    @property
    def ami_id(self):
        return self._get_url(f"{self.metadata_url}/ami-id").text

    @property
    def ami_launch_index(self):
        return int(self._get_url(f"{self.metadata_url}/ami-launch-index").text)

    @property
    def ami_manifest_launch(self):
        return self._get_url(f"{self.metadata_url}/ami-manifest-launch").text

    @property
    def iam_info(self):
        resp = self._get_url(f"{self.metadata_url}iam/info")
        if resp.status_code == 404:
            return None
        return resp.json()

    @property
    def hostname(self):
        return self._get_url(f"{self.metadata_url}/hostname").text

    @property
    def block_device_mapping_ami(self):
        return self._get_url(f"{self.metadata_url}/block-device-mapping/ami").text

    @property
    def hibernation_configured(self):
        return self._get_url(f"{self.metadata_url}/hibernation/configured").text

    @property
    def hibernation_configured(self):
        return self._get_url(f"{self.metadata_url}/hibernation/configured").text

    @property
    def instance_action(self):
        return self._get_url(f"{self.metadata_url}/instance-action").text

    @property
    def instance_id(self):
        return self._get_url(f"{self.metadata_url}/instance-id").text

    @property
    def instance_life_cycle(self):
        return self._get_url(f"{self.metadata_url}/instance-life-cycle").text

    @property
    def instance_type(self):
        return self._get_url(f"{self.metadata_url}/instance-type").text

    @property
    def local_hostname(self):
        return self._get_url(f"{self.metadata_url}/local-hostname").text

    @property
    def local_ipv4(self):
        return self._get_url(f"{self.metadata_url}/local-ipv4").text

    @property
    def mac(self):
        return self._get_url(f"{self.metadata_url}/mac").text

    @property
    def network_interfaces(self):
        r = self._get_url(f"{self.metadata_url}/network/interfaces/macs/").text
        macs = [line.rstrip("/") for line in r.splitlines()]

        result = {}
        for mac in macs:
            result[mac] = {}
            result[mac]["device-number"] = self._get_url(f"{self.metadata_url}/network/interfaces/macs/{mac}/device-number").text
            result[mac]["interace-id"] = self._get_url(f"{self.metadata_url}/network/interfaces/macs/{mac}/interface-id").text
            result[mac]["local-hostname"] = self._get_url(f"{self.metadata_url}/network/interfaces/macs/{mac}/local-hostname").text
            result[mac]["local-ipv4s"] = self._get_url(f"{self.metadata_url}/network/interfaces/macs/{mac}/local-ipv4s").text
            result[mac]["mac"] = self._get_url(f"{self.metadata_url}/network/interfaces/macs/{mac}/mac").text
            result[mac]["owner-id"] = self._get_url(f"{self.metadata_url}/network/interfaces/macs/{mac}/owner-id").text
            result[mac]["security-group-ids"] = self._get_url(f"{self.metadata_url}/network/interfaces/macs/{mac}/security-group-ids").text.split("\n")
            result[mac]["security-groups"] = self._get_url(f"{self.metadata_url}/network/interfaces/macs/{mac}/security-groups").text.split("\n")
            result[mac]["subnet-id"] = self._get_url(f"{self.metadata_url}/network/interfaces/macs/{mac}/subnet-id").text
            result[mac]["subnet-ipv4-cidr-block"] = self._get_url(f"{self.metadata_url}/network/interfaces/macs/{mac}/subnet-ipv4-cidr-block").text
            result[mac]["vpc-id"] = self._get_url(f"{self.metadata_url}/network/interfaces/macs/{mac}/vpc-id").text
            result[mac]["vpc-ipv4-cidr-block"] = self._get_url(f"{self.metadata_url}/network/interfaces/macs/{mac}/vpc-ipv4-cidr-block").text
            result[mac]["vpc-ipv4-cidr-blocks"] = self._get_url(f"{self.metadata_url}/network/interfaces/macs/{mac}/vpc-ipv4-cidr-blocks").text.split("\n")
        return result

    @property
    def availability_zone(self):
        return self._get_url(f"{self.metadata_url}/placement/availability-zone").text

    @property
    def availability_zones(self):
        return self._get_url(f"{self.metadata_url}/placement/availability-zones").text

    @property
    def product_codes(self):
        return self._get_url(f"{self.metadata_url}/product-codes").text

    @property
    def profile(self):
        return self._get_url(f"{self.metadata_url}/profile").text

    @property
    def public_keys(self):
        r = self._get_url(f"{self.metadata_url}/public-keys").text
        return ",".join([line.split("=")[1] for line in r.splitlines()])

    @property
    def reservation_id(self):
        return self._get_url(f"{self.metadata_url}/reservation-id").text

    @property
    def security_groups(self):
        return self._get_url(f"{self.metadata_url}/security-groups").text.splitlines()

    @property
    def domain(self):
        return self._get_url(f"{self.metadata_url}/services/domain").text

    @property
    def system(self):
        return self._get_url(f"{self.metadata_url}/system").text

# Define ec2 metadata object
ec2_metadata = EC2Metadata()

res = {}
for attrib in dir(ec2_metadata):
    if not attrib.startswith("_"):
        res.update({attrib : getattr(ec2_metadata, attrib, "")})

# Display result
print(json.dumps(res, indent=4))

