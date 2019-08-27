""" Tests the role """
import os
import pytest

import testinfra.utils.ansible_runner

# pylint: disable=invalid-name
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture
def has_apt(host):
    """ Fixture to check for aptitude """
    return host.run('command -v apt').rc == 0


def test_hosts_file(host):
    """ Verify the hosts file (therefore instance) works """
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize('pkg', [
    {'pacman': 'openssh', 'apt': 'openssh-server'},
    {'pacman': 'openssl', 'apt': 'openssl'},
    {'pacman': 'keychain', 'apt': 'keychain'},
    {'pacman': 'wget', 'apt': 'wget'},
    {'pacman': 'curl', 'apt': 'curl'},
    {'pacman': 'unzip', 'apt': 'unzip'},
    {'pacman': 'git', 'apt': 'git'},
    {'pacman': 'tig', 'apt': 'tig'},
    {'pacman': 'vim', 'apt': 'vim'},
    {'pacman': 'tmux', 'apt': 'tmux'},
    {'pacman': 'fzf', 'apt': 'fzf'},
    {'pacman': 'fd', 'apt': 'fd-find'},
    {'pacman': 'ripgrep', 'apt': 'ripgrep'},
    {'pacman': 'tree', 'apt': 'tree'},
    {'pacman': 'ranger', 'apt': 'ranger'},
    {'pacman': 'ncdu', 'apt': 'ncdu'},
    {'pacman': 'htop', 'apt': 'htop'},
    {'pacman': 'iotop', 'apt': 'iotop'},
    {'pacman': 'tldr', 'apt': 'tldr'},
])
def test_that_common_packages_installed(host, pkg, has_apt):
    """ Test whether role installed packages are present by package mgr."""
    # in debian-based systems fd is called fd-find
    pkg_mgr = 'pacman'
    if has_apt:
        pkg_mgr = 'apt'
    #  if has_apt and pkg == 'fd':
    #      pkg = 'fd-find'
    assert host.package(pkg[pkg_mgr]).is_installed
