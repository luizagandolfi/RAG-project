from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Optional

class States(str, Enum):
    AP = "Amapá"
    AM = "Amazonas"
    PA = "Pará"
    MA = "Maranhão"
    PI = "Piauí"
    CE = "Ceará"
    RN = "Rio Grande do Norte"
    PB = "Paraíba"
    PE = "Pernambuco"
    AL = "Alagoas"
    SE = "Sergipe"
    BA = "Bahia"
    ES = "Espírito Santo"
    RJ = "Rio de Janeiro"
    RP = "São Paulo"
    PR = "Paraná"
    SC = "Santa Catarina"
    RS = "Rio Grande do Sul"

class ActivityType(str, Enum):
    exploracao_rasa = "Exploração offshore (águas rasas)"
    exploracao_profunda = "Exploração offshore (águas profundas/ultraprofundas)"
    perfucarao_pocos = "Perfuração de poços marítimos"
    producao_exportacao = "Produção e extração de petróleo/gás"
    transporte = "Transporte de petróleo/gás por navios ou dutos submarinos"
    instalacao_plataforma = "Instalação de plataforma fixa ou flutuante"
    outras = "Outras"

class ProtectedAreaType(str, Enum):
    apa = "Área de Proteção Ambiental (APA)"
    reserva_extrativista = "Reserva Extrativista"
    parque_nacional_marinho = "Parque Nacional Marinho"
    reserva_biologica = "Reserva Biológica"
    outra = "Outra"

class ExpectedImpact(str, Enum):
    emissao_gases = "Emissão de gases poluentes"
    alteracao_biodiversidade = "Alteração na biodiversidade marinha"
    derramamento_oleo = "Derramamento de óleo"
    risco_vazamento = "Riscos de vazamento de substâncias tóxicas"
    geracao_residuos = "Geração de resíduos perigosos"
    poluicao_sonora = "Poluição sonora submarina"
    poluicao_quimica = "Poluição química"
    impacto_socioeconomico = "Impacto socioeconômico"
    outro = "Outro"

class MitigationMeasure(str, Enum):
    tratamento_residuos = "Tratamento de resíduos"
    sistema_contencao = "Sistemas de contenção e dispersão de poluentes"
    restauracao_ecossistemas = "Restauração de ecossistemas"
    plano_derramamento_oleo = "Plano de contingência para derramamento de óleo"
    monitoramento = "Monitoramento ambiental contínuo"
    compensacao_ambiental = "Programas de compensação ambiental"
    nao_possui = "Não possui plano de gerenciamento de resíduos"
    nao_necessario = "Não é necessário plano de gerenciamento de resíduos"
    outra = "Outra"

class WaterContamination(str, Enum):
    oil_spill = "Derramamentos de Petróleo"
    produced_water = "Águas Produzidas"
    chemicals = "Produtos Químicos"
    efluents = "Efluentes de Estações de Tratamento"
    contaminated_soil = "Acúmulo de Sedimentos e Solos Contaminados"
    gas = "Gás e Metano"
    other = "Outros/Nenhum"

class EIARIMA(str, Enum):
    de_acordo = "O projeto já passou por Avaliação de Impacto Ambiental (EIA/RIMA)"
    nao_de_acordo = "O projeto ainda não passou por Avaliação de Impacto Ambiental (EIA/RIMA)"
    em_andamento = "O projeto está passando por Avaliação de Impacto Ambiental (EIA/RIMA)"
    nao_aplicavel = "O projeto não precisa passar por Avaliação de Impacto Ambiental (EIA/RIMA)"

class LegalConformity(str, Enum):
    licenca_previa = "O projeto possui licença prévia"
    licenca_instalacao = "O projeto possui licença de instalação"
    licenca_operacao = "O projeto possui licença de operação"
    nao_possui = "O projeto não possui nenhuma licenca"
    nenhuma = "Nehuma licenca é aplicavel"


class PlatformType(str, Enum):
    fixa = "Plataforma fixa"
    semi_submersivel = "Plataforma semi-submersível"
    fpso = "FPSO (Floating Production Storage and Offloading)"
    outra = "Outra"

class ExtractionMethod(str, Enum):
    perfuracao_convencional = "Perfuração convencional"
    fraturamento_hidraulico = "Fraturamento hidráulico"
    injecao_gas = "Injeção de gás para aumento da recuperação"
    outro = "Outro"


# Modelo do formulário atualizado com opções fixas
class EnvironmentalImpactForm(BaseModel):
    # 1. Informações Gerais do Projeto
    project_name: str
    affected_states: List[States]
    activity_types: List[ActivityType]

    # 2. Área de Influência Ambiental
    protected_area: bool
    protected_area_type: Optional[List[ProtectedAreaType]] = None
    distance_to_coast_km: Optional[float] = None
    affects_sensitive_ecosystem: bool
    sensitive_ecosystem_details: Optional[str] = None

    # 3. Impactos Ambientais Potenciais
    expected_impacts: List[ExpectedImpact]
    water_contamination_risk: bool
    contamination_source: Optional[List[WaterContamination]] = None


    # 5. Medidas de Controle e Mitigação
    mitigation_measures: List[MitigationMeasure]
    eia_rima: EIARIMA
    legal_conformity: List[LegalConformity] = None

    # 7. Impacto Socioeconômico
    affects_traditional_communities: bool
    affected_communities_details: Optional[str] = None
    socioeconomic_benefits: Optional[str] = None

    # 8. Risco e Segurança Ambiental
    emergency_response_plan: bool
    hazardous_waste_details: Optional[str] = None


    # 11. Especificidades Técnicas da Atividade Offshore
    platform_type: List[PlatformType]
    exploration_depth_meters: float
    drilling_distance_to_shore_km: float
    extraction_method: List[ExtractionMethod]
    considerations: Optional[str] = None