# Copyright 2024 The Aibrix Team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import hashlib
from abc import ABC, abstractmethod

from farmhash import FarmHash128


class Hasher(ABC):
    @abstractmethod
    def hash(self, data: bytes) -> int:
        """Compute a 128-bit hash from the given data.

        Args:
            data (bytes): Input data to hash.

        Returns:
            int: 128-bit unsigned integer hash value.
        """
        raise NotImplementedError


class MD5Hasher(Hasher):
    def hash(self, data: bytes) -> int:
        return int(hashlib.md5(data).hexdigest(), 16)


class FarmHasher(Hasher):
    def hash(self, data: bytes) -> int:
        return int(FarmHash128(data))
