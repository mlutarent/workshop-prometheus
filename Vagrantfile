Vagrant.require_version ">= 2.2.0"

Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/bionic64"

  config.vm.synced_folder "playgrounds/", "/home/vagrant/playgrounds"

  # Forwards ports opened by the playgrounds to the host (the machine that runs vagrant)
  config.vm.network "forwarded_port", guest: 9090, host: 9090
  config.vm.network "forwarded_port", guest: 9093, host: 9093
  config.vm.network "forwarded_port", guest: 3000, host: 3000
  config.vm.network "forwarded_port", guest: 5000, host: 5000
  config.vm.network "forwarded_port", guest: 5001, host: 5001
  config.vm.network "forwarded_port", guest: 8025, host: 8025

  # Use ansible as for provisioning
  # https://www.vagrantup.com/docs/provisioning/ansible_local
  config.vm.provision "ansible_local" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "provision/playbook.yml"
    ansible.galaxy_role_file = "provision/requirements.yml"
    ansible.galaxy_roles_path = "/home/vagrant/roles"
    ansible.become = true
  end
end
