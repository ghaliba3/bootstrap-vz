from manifest import Manifest


def tasks(tasklist, manifest):
	from tasks import packages
	from tasks import connection
	from tasks import host
	from tasks import ebs
	tasklist.add(packages.HostPackages(), packages.ImagePackages(), host.CheckPackages(),
	             connection.GetCredentials(), host.GetInfo(), connection.Connect())
	if manifest.volume['backing'].lower() == 'ebs':
		tasklist.add(ebs.CreateVolume(), ebs.AttachVolume())

	from common.tasks import TriggerRollback
	tasklist.add(TriggerRollback())
