# Copyright 2020 Nokia
# Copyright 2020 Cachengo
# Copyright 2020 ENEA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from hw_detector.hw_type import HWType

class HWFALCON(HWType):
    def __init__(self):
        super(HWFALCON, self).__init__()
        self.matches = {'Board Product' : 'FALCON'}
        self.hwtype = 'FALCON'
        self.vendor_name = 'AMPERE'
        self.productfamily = 'FALCON'
        self.disk_map = {'os': '/dev/sda',
                         'osd' : ['/dev/sdb',
                                  '/dev/sdc',
                                  '/dev/sdd'
                                 ]
                        }

class HWHAWK(HWType):
    def __init__(self):
        super(HWHAWK, self).__init__()
        self.matches = {'Board Product' : 'HAWK'}
        self.hwtype = 'HAWK'
        self.vendor_name = 'AMPERE'
        self.productfamily = 'FALCON' # Hawk uses same BMC
        self.disk_map = {'os': '/dev/sda',
                         'osd' : ['/dev/sdb',
                                  '/dev/sdc',
                                  '/dev/sdd'
                                 ]
                        }
