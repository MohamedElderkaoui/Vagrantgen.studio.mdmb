# Vagrantfile generator
# Adrian Ramos
# https://github.com/aramcap/vagrantgen

Vagrant.configure("2") do |config|
    config.vm.synced_folder ".", "/vagrant", disabled: true

    config.vm.define "cluster1vm01" do |node|
        node.vm.hostname = "cluster1vm01"
        node.vm.box = "centos/7"
        node.vm.provider "virtualbox" do |provider|
            provider.memory = "1024"
            provider.cpus = "2"
            unless File.exist?("disk1.vdi")
                provider.customize ["storagectl", :id,  "--name", "SATA", "--add", "sata"]
            end
            unless File.exist?("disk1.vdi")
                provider.customize ["createhd", "--filename", "disk1.vdi", "--size", 20 * 1024]
            end
            provider.customize ["storageattach", :id,  "--storagectl", "SATA", "--port", 1, "--type", "hdd", "--medium", "disk1.vdi"]
        end
        node.vm.network "private_network", ip: "192.168.122.100"
        node.vm.network "public_network", type: "bridge", dev: "br01",  mode: "bridge"
        node.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
    end
end