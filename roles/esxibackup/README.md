# Backup ESXi hosts
#
# As ESXi stand-alone has no option to automaticaly create a backup of a machine, an Ansible playbook was created. 
# Make sure that you have an NFS share named NFSSHARE available at the ESXi host or change the playbook to another folder.
# You can find the folder directions in /tasks/exportvmdk.yml
# Sorry, I'm to lazy to convert it to a variable now
# Make sure to set tag(note) "BACKUP: YES" at the VM in ESXi
# Only hosts with the tag will be backed up.
#
# Because it's not possible to export a vmdk while the machine is running, a backup is created and after export of the
# vmdk file removed. Machines that already have a snapthos will not be snapthotted again.
# Snapshots will not backed up. You will miss the data after the snapthot was created. 
