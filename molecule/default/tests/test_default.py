import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

@pytest.fixture
def has_apt(host):
   return host.run('command -v apt').rc == 0


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

@pytest.mark.parametrize('pkg',[
    'openssh',
    'openssl',
    'wget',
    'curl',
    'git',
    'tig',
    'vim',
    'tmux',
    'fzf',
    'fd',
    'ripgrep',
    'tree',
    'ranger',
    'ncdu',
    'htop',
    'iotop',
    'tldr',
])
def test_that_common_packages_installed(host, pkg, has_apt):
    # in debian-based systems fd is called fd-find
    if has_apt and pkg == 'fd':
        pkg = 'fd-find'
    assert host.package(pkg).is_installed
