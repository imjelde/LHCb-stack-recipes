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
    url      = "https://gitlab.cern.ch/lhcb/Detector/-/archive/master/Detector-master.tar.gz"

    maintainers = ['imjelde']

    version('master', branch='master')

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
