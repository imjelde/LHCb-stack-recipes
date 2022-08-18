# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------


from spack import *


class Lhcb(CMakePackage):
    """The LHCb project contains general purpose classes used throughout the LHCb software.
    It is built on top of the Gaudi framework."""

    homepage = "http://cern.ch/lhcbdoc/lhcb"
    git      = "https://gitlab.cern.ch/lhcb/LHCb.git"
    url      = "https://gitlab.cern.ch/lhcb/LHCb/-/archive/v53r8p1/LHCb-v53r8p1.tar.gz"

    maintainers = ['imjelde']

    version('master', branch='master')
    version('commit1204', commit='294e780ad2c122b74999e34dd78baab30081b44d')
    version('53r9',   sha256='997c14636e604570135408807165209ede635a170b2107f8fe7053754619a9fa')
    version('53r8p1', sha256='9e21c75fbeaa7470f40b1933ae74ec7df569a31160ee6bd843089d9964c7c6ec')
    version('53r6',   sha256='5c846c5f5f162d169718522db891b5cdd1e68171e3a69688c6afd9fb7397cb4e')

    variant('test', default=True,
        description='Include tests')

    depends_on('gaudida +optional')
    depends_on('detector')
    depends_on('aida')
    depends_on('boost@1.77: +container')
    depends_on('clhep')
    depends_on('cppgsl')
    depends_on('eigen@3')
    depends_on('fmt')
    depends_on('gsl')
    depends_on('hepmc')
    depends_on('openssl')
    depends_on('python')
    depends_on('range-v3')
    depends_on('root@6.20: +root7')
    depends_on('tbb')
    depends_on('vc@1.4.1')
    depends_on('vdt')
    depends_on('xerces-c')
    depends_on('yaml-cpp')

    depends_on('relax')

    depends_on('libgit2')
    depends_on('libzmq')
    depends_on('libsodium')

    depends_on('py-six')

    # options of full testing
    def cmake_args(self):
        args = [
            self.define_from_variant('BUILD_TESTING', 'test')
        ]
        return args
