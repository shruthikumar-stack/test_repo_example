"""
Data models for the application.
"""
from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime


@dataclass
class User:
    id: int
    name: str
    email: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    is_active: bool = True

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "created_at": self.created_at.isoformat(),
            "is_active": self.is_active,
        }


@dataclass
class Project:
    id: int
    name: str
    description: str
    owner_id: int
    created_at: datetime = field(default_factory=datetime.utcnow)
    status: str = "active"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "owner_id": self.owner_id,
            "created_at": self.created_at.isoformat(),
            "status": self.status,
        }


@dataclass
class Task:
    id: int
    title: str
    project_id: int
    assignee_id: Optional[int] = None
    priority: str = "medium"
    completed: bool = False

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "project_id": self.project_id,
            "assignee_id": self.assignee_id,
            "priority": self.priority,
            "completed": self.completed,
        }
