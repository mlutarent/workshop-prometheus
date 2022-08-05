Vagrant.require_version ">= 1.8.0"

Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/bionic64"

  config.vm.synced_folder "playgrounds/", "/home/vagrant/playgrounds"
  config.vm.network "forwarded_port", guest: 55055, host: 55055

  # https://www.vagrantup.com/docs/provisioning/ansible_local
  config.vm.provision "ansible_local" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "provision/playbook.yml"
    ansible.galaxy_role_file = "provision/requirements.yml"
    ansible.galaxy_roles_path = "/home/vagrant/roles"
    ansible.become = true
  end
end
