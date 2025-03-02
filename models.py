from datetime import datetime
from typing import Optional

from fastapi import Query
from pydantic import BaseModel


class CreateFormData(BaseModel):
    wallet: str = Query(...)
    name: str = Query(...)
    webhook: str = Query(None)
    description: str = Query(..., min_length=0)
    amount: int = Query(..., ge=0)
    flatrate: int = Query(...)


class CreateTicketData(BaseModel):
    form: str = Query(...)
    name: str = Query(...)
    email: str = Query("")
    ltext: str = Query(...)
    sats: int = Query(..., ge=0)


class Form(BaseModel):
    id: str
    wallet: str
    name: str
    webhook: Optional[str]
    description: str
    amount: int
    flatrate: int
    amountmade: int
    time: datetime


class Ticket(BaseModel):
    id: str
    form: str
    email: str
    ltext: str
    name: str
    wallet: str
    sats: int
    paid: bool
    time: datetime
