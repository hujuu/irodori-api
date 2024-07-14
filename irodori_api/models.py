from bson import ObjectId
from pydantic import Field, BaseModel, validator
from typing import List, Optional
from datetime import datetime


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class MongoBaseModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        json_encoders = {ObjectId: str}



class GiftBase(MongoBaseModel):
    nft_id: str = Field(..., min_length=1)
    message: str = Field(..., min_length=1)


class GiftUpdate(MongoBaseModel):
    message: Optional[str] = None


class GiftDB(GiftBase):
    pass


class MarketDescriptionBlockData(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    data: Optional[dict] = None


class MarketDescription(BaseModel):
    time: Optional[int] = None
    blocks: Optional[List[MarketDescriptionBlockData]] = None
    version: Optional[str] = None


class ScenarioBase(MongoBaseModel):
    portfolio_id: str = Field(..., min_length=1)
    name: str = Field(..., min_length=1)
    status: str = Field(..., min_length=1)
    count: str = Field(..., min_length=1)
    round: str = Field(..., min_length=1)
    rate: str = Field(..., min_length=1)
    evaluation: str = Field(..., min_length=1)
    liquidity_discount: Optional[float] = None
    investment_amount: Optional[int] = None
    created_at: Optional[datetime] = None


class ScenarioUpdate(MongoBaseModel):
    name: Optional[str] = None
    status: Optional[str] = None
    count: Optional[str] = None
    round: Optional[str] = None
    rate: Optional[str] = None
    evaluation: Optional[str] = None
    first_sales: Optional[int] = None
    first_gross_profit: Optional[int] = None
    first_sg_and_a: Optional[int] = None
    first_operating_income: Optional[int] = None
    first_tax: Optional[int] = None
    second_sales: Optional[int] = None
    second_gross_profit: Optional[int] = None
    second_sg_and_a: Optional[int] = None
    second_operating_income: Optional[int] = None
    second_tax: Optional[int] = None
    third_sales: Optional[int] = None
    third_gross_profit: Optional[int] = None
    third_sg_and_a: Optional[int] = None
    third_operating_income: Optional[int] = None
    third_tax: Optional[int] = None
    force_sales: Optional[int] = None
    force_gross_profit: Optional[int] = None
    force_sg_and_a: Optional[int] = None
    force_operating_income: Optional[int] = None
    force_tax: Optional[int] = None
    fifth_sales: Optional[int] = None
    fifth_gross_profit: Optional[int] = None
    fifth_sg_and_a: Optional[int] = None
    fifth_operating_income: Optional[int] = None
    fifth_tax: Optional[int] = None
    first_capital_investment: Optional[int] = None
    first_depreciation: Optional[int] = None
    second_capital_investment: Optional[int] = None
    second_depreciation: Optional[int] = None
    third_capital_investment: Optional[int] = None
    third_depreciation: Optional[int] = None
    force_capital_investment: Optional[int] = None
    force_depreciation: Optional[int] = None
    fifth_capital_investment: Optional[int] = None
    fifth_depreciation: Optional[int] = None
    current_accounts_receivable: Optional[int] = None
    current_inventory: Optional[int] = None
    current_accounts_payable: Optional[int] = None
    current_advance_payment: Optional[int] = None
    first_accounts_receivable: Optional[int] = None
    first_inventory: Optional[int] = None
    first_accounts_payable: Optional[int] = None
    first_advance_payment: Optional[int] = None
    second_accounts_receivable: Optional[int] = None
    second_inventory: Optional[int] = None
    second_accounts_payable: Optional[int] = None
    second_advance_payment: Optional[int] = None
    third_accounts_receivable: Optional[int] = None
    third_inventory: Optional[int] = None
    third_accounts_payable: Optional[int] = None
    third_advance_payment: Optional[int] = None
    force_accounts_receivable: Optional[int] = None
    force_inventory: Optional[int] = None
    force_accounts_payable: Optional[int] = None
    force_advance_payment: Optional[int] = None
    fifth_accounts_receivable: Optional[int] = None
    fifth_inventory: Optional[int] = None
    fifth_accounts_payable: Optional[int] = None
    fifth_advance_payment: Optional[int] = None
    fifth_net_income_after_tax: Optional[int] = None
    interest_bearing_debt: Optional[int] = None
    c_and_ce: Optional[int] = None
    liquidity_discount: Optional[float] = None
    investment_amount: Optional[int] = None
    market_irregular: Optional[bool] = None
    market_trend_irregular: Optional[bool] = None
    market_description: Optional[MarketDescription] = None
    cash_burn_irregular: Optional[bool] = None


class ScenarioDB(ScenarioBase):
    first_sales: Optional[int] = None
    first_gross_profit: Optional[int] = None
    first_sg_and_a: Optional[int] = None
    first_operating_income: Optional[int] = None
    first_tax: Optional[int] = None
    second_sales: Optional[int] = None
    second_gross_profit: Optional[int] = None
    second_sg_and_a: Optional[int] = None
    second_operating_income: Optional[int] = None
    second_tax: Optional[int] = None
    third_sales: Optional[int] = None
    third_gross_profit: Optional[int] = None
    third_sg_and_a: Optional[int] = None
    third_operating_income: Optional[int] = None
    third_tax: Optional[int] = None
    force_sales: Optional[int] = None
    force_gross_profit: Optional[int] = None
    force_sg_and_a: Optional[int] = None
    force_operating_income: Optional[int] = None
    force_tax: Optional[int] = None
    fifth_sales: Optional[int] = None
    fifth_gross_profit: Optional[int] = None
    fifth_sg_and_a: Optional[int] = None
    fifth_operating_income: Optional[int] = None
    fifth_tax: Optional[int] = None
    first_capital_investment: Optional[int] = None
    first_depreciation: Optional[int] = None
    second_capital_investment: Optional[int] = None
    second_depreciation: Optional[int] = None
    third_capital_investment: Optional[int] = None
    third_depreciation: Optional[int] = None
    force_capital_investment: Optional[int] = None
    force_depreciation: Optional[int] = None
    fifth_capital_investment: Optional[int] = None
    fifth_depreciation: Optional[int] = None
    current_accounts_receivable: Optional[int] = None
    current_inventory: Optional[int] = None
    current_accounts_payable: Optional[int] = None
    current_advance_payment: Optional[int] = None
    first_accounts_receivable: Optional[int] = None
    first_inventory: Optional[int] = None
    first_accounts_payable: Optional[int] = None
    first_advance_payment: Optional[int] = None
    second_accounts_receivable: Optional[int] = None
    second_inventory: Optional[int] = None
    second_accounts_payable: Optional[int] = None
    second_advance_payment: Optional[int] = None
    third_accounts_receivable: Optional[int] = None
    third_inventory: Optional[int] = None
    third_accounts_payable: Optional[int] = None
    third_advance_payment: Optional[int] = None
    force_accounts_receivable: Optional[int] = None
    force_inventory: Optional[int] = None
    force_accounts_payable: Optional[int] = None
    force_advance_payment: Optional[int] = None
    fifth_accounts_receivable: Optional[int] = None
    fifth_inventory: Optional[int] = None
    fifth_accounts_payable: Optional[int] = None
    fifth_advance_payment: Optional[int] = None
    fifth_net_income_after_tax: Optional[int] = None
    interest_bearing_debt: Optional[int] = None
    c_and_ce: Optional[int] = None
    market_irregular: Optional[bool] = None
    market_trend_irregular: Optional[bool] = None
    market_description: Optional[MarketDescription] = None
    cash_burn_irregular: Optional[bool] = None
    pass


class UserBase(MongoBaseModel):
    name: str = Field(..., min_length=1)
    sub: str = Field(..., min_length=1)


class UserDB(UserBase):
    pass


class PerBase(MongoBaseModel):
    scenario_id: str = Field(..., min_length=1)
    name: str = Field(..., max_length=20)
    per: Optional[int] = None
    # created_at: Optional[datetime] = None


class PerUpdate(MongoBaseModel):
    per: Optional[int] = None


class PerDB(PerBase):
    pass


class PerItemList(MongoBaseModel):
    data: List[PerBase]


class QuantsBase(MongoBaseModel):
    Code: Optional[int] = None
    CompanyName: str = Field(..., min_length=1)


class QuantsDB(QuantsBase):
    pass


class Choice(BaseModel):
    name: str
    answer: bool


class Question(MongoBaseModel):
    sort: int
    title: str
    name: str
    choices: List[Choice]


class QuestionBase(MongoBaseModel):
    name: str
    questions: List[Question]


class QuestionUpdate(MongoBaseModel):
    name: Optional[str] = None
    questions: List[Question]


class QuestionDB(QuestionBase):
    pass
