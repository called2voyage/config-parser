# Copyright 2022 called2voyage
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os

TRUE_VALUES = ['true', 'on', 'yes']
FALSE_VALUES = ['false', 'off', 'no']

class Config():
    def __init__(self, name):
        '''Config constructor
        Stores the filename and initializes the parameters dictionary
        '''
        self.name = name
        self.parameters = {}

    def add_parameter(self, name, value):
        '''Adds a parameter to the Config with the given name and value'''
        self.parameters[name] = value

    def get(self, name):
        '''Gets the value for the given parameter name
        Assumes the given name exists, raises KeyError if not
        '''
        return self.parameters[name]

    def exists(self, name):
        '''Checks to see if the given name exists'''
        return name in self.parameters

def parse_config(filepath):
    '''Parses a config file at the given filepath and returns a Config object'''
    config = None
    with open(filepath, 'r') as f:
        config = Config(os.path.basename(f.name))
        while line := f.readline():
            if '=' in line:
                if not line.lstrip().startswith('#'):
                    if line.count('=') == 1:
                        try:
                            config.add_parameter(line.split('=')[0].strip(),
                                                 int(line.split('=')[1].strip()))
                        except ValueError:
                            try:
                                config.add_parameter(line.split('=')[0].strip(),
                                                     float(line.split('=')[1].strip()))
                            except ValueError:
                                if line.split('=')[1].strip().lower() in TRUE_VALUES:
                                    config.add_parameter(line.split('=')[0].strip(),
                                                         True)
                                elif line.split('=')[1].strip().lower() in FALSE_VALUES:
                                    config.add_parameter(line.split('=')[0].strip(),
                                                         False)
                                else:
                                    config.add_parameter(line.split('=')[0].strip(),
                                                         line.split('=')[1].strip())
    return config
