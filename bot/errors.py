from __future__ import annotations


class NonExistentRoleError(ValueError):
    """
    Raised by the Information Cog when encountering a Role that does not exist.

    Attributes:
        `role_id` -- the ID of the role that does not exist
    """

    def __init__(self, role_id: int):
        super().__init__(f"Could not fetch data for role {role_id}")

        self.role_id = role_id
