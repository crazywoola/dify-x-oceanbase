from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


class SeekdbProvider(ToolProvider):
    
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            import pyseekdb
        except ImportError as exc:
            raise ToolProviderCredentialValidationError(
                "pyseekdb is not installed. Please install the SeekDB client dependency."
            ) from exc

        host = credentials.get("host")
        port_value = credentials.get("port", 2881)
        tenant = credentials.get("tenant") or "sys"
        user = credentials.get("user") or "root"
        password = credentials.get("password", "")
        database = credentials.get("database") or "demo"

        if not host:
            raise ToolProviderCredentialValidationError("Host is required.")

        try:
            port = int(port_value)
        except (TypeError, ValueError) as exc:
            raise ToolProviderCredentialValidationError("Port must be a valid integer.") from exc

        try:
            client = pyseekdb.Client(
                host=host,
                port=port,
                tenant=tenant,
                database=database,
                user=user,
                password=password,
            )
            client.count_collection()
        except Exception as exc:
            raise ToolProviderCredentialValidationError(
                f"Unable to connect to SeekDB: {exc}"
            ) from exc

   
