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


# A global flag to indicate whether current platform has RDMA transport support.
HAS_RDMA_TRANSPORT_SUPPORT = True

__all__ = ["HAS_RDMA_TRANSPORT_SUPPORT"]

try:
    from .rdma import (  # noqa: F401
        AddrFamily,
        DeviceRequest,
        GIDType,
        RDMATransport,
    )

    __all__.extend(["AddrFamily", "DeviceRequest", "GIDType", "RDMATransport"])
except ImportError:
    HAS_RDMA_TRANSPORT_SUPPORT = False
