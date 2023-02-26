from pydantic import BaseModel, Field


class Tarifas(BaseModel):
    """Classe para representar as tarifas para diferentes planos."""
    sem_plano: float = Field(..., description="Tarifa do Usuario Sem Plano")
    FaleMais30: float = Field(..., description="Tarifa do Usuario Com Plano Fale Mais 30")
    FaleMais60: float = Field(..., description="Tarifa do Usuario Com Plano Fale Mais 60")
    FaleMais120: float = Field(..., description="Tarifa do Usuario Com Plano Fale Mais 120")