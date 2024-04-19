# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0-only
# SPDX-FileCopyrightText: 2024 Red Hat, Project Atmosphere
#
# Copyright 2024 Red Hat, Project Atmosphere
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU
# General Public License as published by the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <https://www.gnu.org/licenses/>.

from __future__ import absolute_import, division, print_function

import traceback
import json


class Entity:
    def __init__(self, **kwargs):
        """Entity class is for all objects.

        Args:
        **kwargs: any keyword arguments will be saved as object attributes.
        """
        self.__dict__.update(kwargs)

    def __iter__(self):
        """Iterates over the object's attributes and yields key-value pairs.

        This is useful for converting the object to a dict.
        """
        for key in self.__dict__:
            yield key, self.__dict__[key]


class BTPAPIError(Entity):
    """BTP API error object."""

    pass


from ansible.module_utils.basic import missing_required_lib


def get_headers(token: str) -> dict:
    return {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Accept": "application/json",
        "DataServiceVersion": "2.0",
    }


try:
    import requests
except ImportError:
    HAS_REQUESTS_LIBRARY = False
    REQUESTS_LIBRARY_IMPORT_ERROR = traceback.format_exc()
else:
    HAS_REQUESTS_LIBRARY = True
    REQUESTS_LIBRARY_IMPORT_ERROR = None


class BTPGlobalAccount(Entity):
    """BTP global account object."""

    pass


class BTPAccountsServiceClient:
    def __init__(
        self,
        url: str,
    ):
        """A client for the SAP BTP Accounts service.

        Args:
            url (str): The URL of the SAP BTP Accounts service.
        """
        self.url = url

    def get_global_account(
        self, token: str, timeout: int = 60, **kwargs
    ) -> (BTPGlobalAccount, BTPAPIError):
        url_params = ""
        if not HAS_REQUESTS_LIBRARY:
            return None, BTPAPIError(
                msg=missing_required_lib("requests"),
                exception=REQUESTS_LIBRARY_IMPORT_ERROR,
            )
        if kwargs.get("expand"):
            url_params = "?expand=true"
        try:
            response = requests.get(
                f"{self.url}/accounts/v1/globalAccount" + url_params,
                headers=get_headers(token),
                timeout=timeout,
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            return None, BTPAPIError(
                response=response.text,
                status_code=response.status_code,
            )
        return BTPGlobalAccount(**json.loads(response.text)), None

    def get_global_account_assignments(
        self,
        token: str,
        **kwargs,
    ):
        url_params = ""
        if not HAS_REQUESTS_LIBRARY:
            return None, BTPAPIError(
                msg=missing_required_lib("requests"),
                exception=REQUESTS_LIBRARY_IMPORT_ERROR,
            )
        if kwargs.get("include_auto_managed_plans"):
            url_params += "&includeAutoManagedPlans=true"
        if kwargs.get("entitled_services_only"):
            url_params += "&entitledServicesOnly=true"
        try:
            response = requests.get(
                f"{self.url}/entitlements/v1/assignments?directoryGUID=7abf6926-f5da-467e-975a-cf2473680127" + url_params,
                headers=get_headers(token),
                timeout=60,
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            return None, BTPAPIError(
                response=response.text,
                status_code=response.status_code,
            )
        return BTPGlobalAccount(**json.loads(response.text)), None

    def get_subaccounts(
        self,
        token: str,
    ):

        url_params = ""
        if not HAS_REQUESTS_LIBRARY:
            return None, BTPAPIError(
                msg=missing_required_lib("requests"),
                exception=REQUESTS_LIBRARY_IMPORT_ERROR,
            )
        try:
            response = requests.get(
                f"{self.url}/accounts/v1/subaccounts?derivedAuthorizations=any" + url_params,
                headers=get_headers(token),
                timeout=60,
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            return None, BTPAPIError(
                response=response.text,
                status_code=response.status_code,
            )
        subaccounts = json.loads(response.text)["value"]
        return subaccounts, None

    def create_subaccount(self, token: str, **kwargs):
        body = {}
        if kwargs.get("beta_enabled") is not None:
            body["betaEnabled"] = kwargs["beta_enabled"]

        if kwargs.get("description") is not None:
            body["description"] = kwargs["description"]

        if kwargs.get("display_name") is not None:
            body["displayName"] = kwargs["display_name"]

        if kwargs.get("region") is not None:
            body["region"] = kwargs["region"]

        if kwargs.get("subdomain") is not None:
            body["subdomain"] = kwargs["subdomain"]

        if kwargs.get("subaccount_admins") is not None:
            body["subaccountAdmins"] = kwargs["subaccount_admins"]

        body["usedForProduction"] = "USED_FOR_PRODUCTION"

        if not HAS_REQUESTS_LIBRARY:
            return None, BTPAPIError(
                msg=missing_required_lib("requests"),
                exception=REQUESTS_LIBRARY_IMPORT_ERROR,
            )
        try:
            response = requests.post(
                f"{self.url}/accounts/v1/subaccounts",
                headers=get_headers(token),
                json=body,
                timeout=60,
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            return None, BTPAPIError(
                response=response.text,
                status_code=response.status_code,
            )
        return BTPGlobalAccount(**json.loads(response.text)), None


import traceback
from abc import ABC, abstractmethod

try:
    from oauth2_client.credentials_manager import CredentialManager, ServiceInformation
except ImportError:
    HAS_OAUTH2_CLIENT_LIBRARY = False
    OAUTH2_CLIENT_LIBRARY_IMPORT_ERROR = traceback.format_exc()
else:
    HAS_OAUTH2_CLIENT_LIBRARY = True
    OAUTH2_CLIENT_LIBRARY_IMPORT_ERROR = None


import signal
from functools import wraps


class BTPTimeoutError(Exception):
    pass


def timeout(seconds=60):
    def decorator(func):
        def _handle_timeout():
            raise BTPTimeoutError("Function call timed out")

        @wraps(func)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wrapper

    return decorator


class OAuthClientABC(ABC):
    """Abstract base class for OAuth clients."""

    @abstractmethod
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        authorize_service_url: str,
        token_service_url: str,
        login: str = None,
        password: str = None,
    ) -> None:
        """Initializes the OAuthClient object.

        This object is used to authenticate against the OAuth service and get authorization token.

        Args:
            login (str): The login username.
            password (str): The login password.
            client_id (str): The client ID.
            client_secret (str): The client secret.
            authorize_service_url (str): The URL of the authorization service.
            token_service_url (str): The URL of the token service.
        """
        pass

    @property
    def token(self) -> str:
        """Gets the OAuth token.

        Returns:
            str: The OAuth token.
        """
        return self.get_token()

    @abstractmethod
    def get_token(self) -> str:
        """Abstract method to get an OAuth token."""
        pass


class OAuthClient(OAuthClientABC):
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        authorize_service_url: str,
        token_service_url: str,
        login: str = None,
        password: str = None,
    ) -> None:
        """Initializes the OAuthClient object.

        This object is used to authenticate against the OAuth service and get authorization token.

        Args:
            login (str): The login username.
            password (str): The login password.
            client_id (str): The client ID.
            client_secret (str): The client secret.
            authorize_service_url (str): The URL of the authorization service.
            token_service_url (str): The URL of the token service.
        """
        service_information = ServiceInformation(
            authorize_service=authorize_service_url,
            token_service=token_service_url,
            client_id=client_id,
            client_secret=client_secret,
            scopes=[],
        )
        self.__manager = CredentialManager(service_information)
        self.login = login
        self.password = password
        self.__token = None

    @timeout(seconds=60)
    def get_token(self) -> str:
        """Gets the OAuth token.

        Returns:
            str: The OAuth token.
        """
        if self.__token is None:
            self.__manager.init_with_user_credentials(
                login=self.login,
                password=self.password,
            )
            self.__token = self.__manager._access_token
        elif self.__manager.is_access_token_expired():
            self.__manager.refresh_access_token()
            self.__token = self.__manager._access_token
        return self.__token


def create_oauth_client(
    client_id: str,
    client_secret: str,
    authorize_service_url: str,
    token_service_url: str,
    login: str = None,
    password: str = None,
) -> (OAuthClient, BTPAPIError):
    """Factory method to create OAuthClient."""
    if not HAS_OAUTH2_CLIENT_LIBRARY:
        print("oauth2_client library is missing")
        return None, BTPAPIError(
            msg=missing_required_lib("oauth2_client"),
            exception=OAUTH2_CLIENT_LIBRARY_IMPORT_ERROR,
        )
    try:
        result = OAuthClient(
            login=login,
            password=password,
            client_id=client_id,
            client_secret=client_secret,
            authorize_service_url=authorize_service_url,
            token_service_url=token_service_url,
        )
    except Exception as e:
        return None, BTPAPIError(
            msg="Could not create OAuth client",
            exception=str(e),
        )
    return result, None


from ansible.errors import AnsibleActionFail

from ansible.plugins.action import ActionBase


class BTPActionModule(ActionBase):
    _VALID_ARGS = frozenset(
        [
            "login",
            "password",
            "api_endpoint",
            "client_id",
            "client_secret",
            "authorize_service_url",
            "token_service_url",
        ]
    )
    BYPASS_HOST_LOOP = False
    TRANSFERS_FILES = False
    _requires_connection = False
    _supports_check_mode = False
    _supports_async = False

    def __init__(
        self, task, connection, play_context, loader, templar, shared_loader_obj
    ):
        """Initializes the BTPActionModule ansible action plugin.

        Args:
            task (ansible.executor.task_vars.Task): The task object.
            connection (ansible.plugins.connection.Connection): The connection object.
            play_context (ansible.playbook.play_context.PlayContext): The play context object.
            loader (ansible.parsing.dataloader.DataLoader): The data loader object.
            templar (ansible.template.Templar): The templar object.
            shared_loader_obj (ansible.plugins.loader.Loader): The shared loader object.

        Raises:
            None.

        Returns:
            None.
        """
        super().__init__(
            task, connection, play_context, loader, templar, shared_loader_obj
        )
        plugin_args = self._task.args.copy()
        login = plugin_args.get("login")
        password = plugin_args.get("password")
        api_endpoint = plugin_args.get("api_endpoint")
        client_id = plugin_args.get("client_id")
        client_secret = plugin_args.get("client_secret")
        authorize_service_url = plugin_args.get("authorize_service_url")
        token_service_url = plugin_args.get("token_service_url")
        self.client = BTPAccountsServiceClient(
            url=api_endpoint,
        )
        self.oauth_client, error = create_oauth_client(
            login=login,
            password=password,
            client_id=client_id,
            client_secret=client_secret,
            authorize_service_url=authorize_service_url,
            token_service_url=token_service_url,
        )
        if error is not None:
            raise AnsibleActionFail(
                obj=dict(error), message="Could not create OAuth client"
            )

    def run(self, tmp=None, task_vars=None):
        super().run(tmp, task_vars)


btp_required_together = [
    ("login", "password"),
    (
        "client_id",
        "client_secret",
        "authorize_service_url",
        "token_service_url",
        "api_endpoint",
    ),
]
btp_argument_spec = dict(
    login=dict(type="str", required=True),
    password=dict(type="str", required=True, no_log=True),
    api_endpoint=dict(type="str", required=True),
    client_id=dict(type="str", required=True, no_log=True),
    client_secret=dict(type="str", required=True, no_log=True),
    authorize_service_url=dict(type="str", required=True),
    token_service_url=dict(type="str", required=True),
)


def plugin_failed(error, msg: str) -> dict:
    if isinstance(error, list):
        return {
            "failed": True,
            "msg": msg,
            "errors": (dict(e) for e in error),
        }
    return {**{"failed": True, "msg": msg}, **dict(error)}


__metaclass__ = type


def run_plugin(
    client: BTPAccountsServiceClient, token: str, expand: bool = True
) -> dict:
    btp_global_account_info, err = client.get_global_account(token=token, expand=expand)
    if err is not None:
        return plugin_failed(err, msg="Could not get global account information")

    return {
        "failed": False,
        "changed": False,
        "btp_global_account_info": dict(btp_global_account_info),
    }


class ActionModule(BTPActionModule):
    _VALID_ARGS = BTPActionModule._VALID_ARGS.union(["expand"])

    def run(self, tmp=None, task_vars=None):
        super().run(tmp, task_vars)

        action_argument_spec = dict(
            expand=dict(type="bool", required=False, default=True)
        )
        argument_spec = dict(**btp_argument_spec, **action_argument_spec)
        self.validate_argument_spec(
            argument_spec=argument_spec, required_together=btp_required_together
        )

        expand = self._task.args.get("expand")
        return run_plugin(
            client=self.client,
            token=self.oauth_client.token,
            expand=expand,
        )
