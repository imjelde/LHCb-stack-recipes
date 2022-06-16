# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install gaudida
#
# You can edit this file again by typing:
#
#     spack edit gaudida
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Gaudida(CMakePackage):
    """The Gaudi project is an open project for providing the necessary interfaces
    and services for building HEP experiment frameworks in the domain of event data
    processing applications. The Gaudi framework is experiment independent."""

    homepage = "https://gaudi.web.cern.ch/gaudi/"
    git      = "https://gitlab.cern.ch/gaudi/Gaudi.git"
    url      = "https://gitlab.cern.ch/gaudi/Gaudi/-/archive/master/Gaudi-master.tar.gz"

    maintainers = ['imjelde']

    version('36.4',     sha256='1a5c27cdc21ec136b47f5805406c92268163393c821107a24dbb47bd88e4b97d')
    version('add-backwardscomp', branch='add-v21-v22-api-options')

    # Mandatory minimum build
    depends_on('boost@1.70: +python')
    depends_on('python@3:')
    depends_on('root@6.18: cxxstd=17 +root7')
    depends_on('uuid')
    depends_on('tbb@2019.0.11007.2:')
    depends_on('zlib@1.2.11:')
    depends_on('range-v3')
    depends_on('cppgsl')
    depends_on('fmt')
    depends_on('nlohmann-json')

    # Optional
    depends_on('aida', when='+optional')
    depends_on('xerces-c', when='+optional')
    depends_on('clhep@2.4.0.1:', when='+optional')
    depends_on('heppdt', when='+optional')
    depends_on('cppunit', when='+optional')
    depends_on('unwind', when='+optional')
    depends_on('gperftools@2.7.0:', when='+optional')
    depends_on('doxygen@1.8.15:', when='+docs')
    depends_on('jemalloc', when='+optional')

    depends_on('py-six')

    variant('optional', default=False,
            description='Full build including optional depencencies')
    variant('docs', default=False,
            description='Include documentation')
    variant('test', default=False,
            description='Include tests')

    # Options of full build and testing
    def cmake_args(self):
        args = [
            self.define_from_variant('BUILD_TESTING', 'test'),
            self.define_from_variant('GAUDI_USE_AIDA', 'optional'),
            self.define_from_variant('GAUDI_USE_XERCESC', 'optional'),
            self.define_from_variant('GAUDI_USE_CLHEP', 'optional'),
            self.define_from_variant('GAUDI_USE_HEPPDT', 'optional'),
            self.define_from_variant('GAUDI_USE_CPPUNIT', 'optional'),
            self.define_from_variant('GAUDI_USE_UNWIND', 'optional'),
            self.define_from_variant('GAUDI_USE_GPERFTOOLS', 'optional'),
            self.define_from_variant('GAUDI_USE_DOXYGEN', 'docs'),
            self.define_from_variant('GAUDI_USE_JEMALLOC', 'optional')
        ]
        return args
