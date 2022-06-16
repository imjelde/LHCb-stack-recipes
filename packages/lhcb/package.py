# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------


from spack import *


class Lhcb(CMakePackage):
    """The LHCb project contains general purpose classes used throughout the LHCb software.
    It is built on top of the Gaudi framework.
    Documentation is available at http://cern.ch/lhcbdoc/lhcb"""

    homepage = "https://gitlab.cern.ch/lhcb/LHCb/"
    git      = "https://gitlab.cern.ch/lhcb/LHCb.git"
    url      = "https://gitlab.cern.ch/lhcb/LHCb/-/archive/v53r6/LHCb-v53r6.tar.gz"

    maintainers = ['imjelde']

    version('commit1204', commit='294e780ad2c122b74999e34dd78baab30081b44d')
    version('master', branch='master')
    version('53.6',    sha256='5c846c5f5f162d169718522db891b5cdd1e68171e3a69688c6afd9fb7397cb4e')

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
