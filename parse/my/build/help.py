from typing import Any, Tuple, Dict


class ColumName:
    data: str = "Дата"
    inter_reserves: str = 'Международные резервы'
    currency_reserves:str = 'валютные резервы'
    foreign_currency:str = 'иностранная валюта'
    sdr_account: str = 'счет в СДР'
    position_imf:str = 'резервная позиция в МВФ'
    monetary_gold:str = 'монетарное золото'

    @classmethod
    def get_dict(cls, 
        data: str, 
        inter_reserves: str, 
        currency_reserves: str,
        foreign_currency: str,
        sdr_account: str,
        position_imf: str,
        monetary_gold: str) -> Dict[str, Any]:
        return {
            cls.data: data,
            cls.inter_reserves: {
                cls.inter_reserves: inter_reserves,
                cls.currency_reserves:{
                    cls.currency_reserves: currency_reserves,
                    cls.foreign_currency: foreign_currency,
                    cls.sdr_account: sdr_account,
                    cls.position_imf: position_imf
                },
                cls.monetary_gold: monetary_gold
            }
        }

    @classmethod
    def get_tuple(cls) -> Tuple[str, ...]:
        return (
            cls.data,
            cls.inter_reserves,
            cls.currency_reserves,
            cls.foreign_currency,
            cls.sdr_account,
            cls.position_imf,
            cls.monetary_gold)

