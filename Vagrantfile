Vagrant.require_version ">= 1.8.0"

Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/bionic64"

  config.vm.synced_folder "playgrounds/", "/home/vagrant/playgrounds"
  config.vm.network "forwarded_port", guest: 55055, host: 55055

  # For third party playground "blndev"
#   config.vm.network "forwarded_port", guest: 3000, host: 3000
#   config.vm.network "forwarded_port", guest: 9080, host: 9080
#   config.vm.network "forwarded_port", guest: 9090, host: 9090
#   config.vm.network "forwarded_port", guest: 9091, host: 9091
#   config.vm.network "forwarded_port", guest: 9092, host: 9092
#   config.vm.network "forwarded_port", guest: 9100, host: 9100
#   config.vm.network "forwarded_port", guest: 9101, host: 9101
#   config.vm.network "forwarded_port", guest: 9102, host: 9102
#   config.vm.network "forwarded_port", guest: 9103, host: 9103

  # For third party playground "prometheus community"
  config.vm.network "forwarded_port", guest: 9090, host: 9090
  config.vm.network "forwarded_port", guest: 9093, host: 9093

  # https://www.vagrantup.com/docs/provisioning/ansible_local
  config.vm.provision "ansible_local" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "provision/playbook.yml"
    ansible.galaxy_role_file = "provision/requirements.yml"
    ansible.galaxy_roles_path = "/home/vagrant/roles"
    ansible.become = true
  end
end
