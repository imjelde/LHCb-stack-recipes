# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------

from spack import *


class Detector(CMakePackage):
    """Description of the LHCb Upgrade detector using the DD4hep framework"""

    homepage = "https://gitlab.cern.ch/lhcb/Detector"
    git      = "https://gitlab.cern.ch/lhcb/Detector"
    url      = "https://gitlab.cern.ch/lhcb/Detector/-/archive/v1r2/Detector-v1r2.tar.gz"

    maintainers = ['imjelde']

    version('master', branch='master')
    version('1.2', sha256='388192b573d9d8e10431730df7dabead3591432b64784d210b67ea0963039bd3')
    version('1.1', sha256='b96b25f0289fc0a8bf3f7d3c9da6a5aebc62aa51890662717f6a710fec38ca83')

    depends_on('gitconddb@0.2.0:')
    depends_on('nlohmann-json')
    depends_on('libgit2')
    depends_on('root +root7')
    depends_on('fmt@6.1.2:')
    depends_on('yaml-cpp@0.6.2:')
    depends_on('boost')
    depends_on('vc')
    depends_on('dd4hep')
    depends_on('openssl')

    def url_for_version(self, version):
            major = str(version[0])
            minor = str(version[1])
            url = "https://gitlab.cern.ch/lhcb/Detector/-/archive/v{0}r{1}/Detector-v{0}r{1}.tar.gz".format(major, minor)
            return url
