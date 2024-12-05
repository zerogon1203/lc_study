from pydantic import BaseModel, Field
from datetime import datetime

class Output(BaseModel):
    carrier: str | None = Field(description="Name of Carrier, for example: EVERGREEN LINE")
    booking_number: str | None = Field(description="Booking number")
    feeder_vessel: str | None = Field(description="Feeder vessel name")
    final_vessel: str | None = Field(description="Final vessel name")
    depot: str | None = Field(description="Container depot location")
    port_name: str | None = Field(description="name of port of loading")
    etd: datetime | None = Field(description="Estimated time of departure")
    eta: datetime | None = Field(description="Estimated time of arrival")
    cargo_closing_date: datetime | None = Field(description="Cargo closing date")
    doc_cut_off_date: datetime | None = Field(description="Document cut off date")
    container_type: str | None = Field(description="Container type")
    container_quantity: int | None = Field(description="Container quantity")
