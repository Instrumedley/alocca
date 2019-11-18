import graphene

from graphene_django.types import DjangoObjectType, ObjectType
from alocca.stock.models import Instrument, Portfolio, Trade


class InstrumentType(DjangoObjectType):
    class Meta:
        model = Instrument


class PortfolioType(DjangoObjectType):
    class Meta:
        model = Portfolio


class TradeType(DjangoObjectType):
    class Meta:
        model = Trade


# INPUT CLASS FOR PORTFOLIO

class PortfolioInput(graphene.InputObjectType):
    name = graphene.String(description='Name for Instrument')
    description = graphene.String(description="Symbol for Instrument")
    holding_value = graphene.Float(description="Holding Value for Portfolio")
    total_profit_loss = graphene.Float(description="Total Profit Loss for Portfolio")


# QUERY

class Query(ObjectType):
    all_instruments = graphene.List(InstrumentType)
    all_portfolios = graphene.List(PortfolioType)

    instrument = graphene.Field(InstrumentType,
                                id=graphene.Int(),
                                symbol=graphene.String())

    portfolio = graphene.Field(PortfolioType,
                                id=graphene.Int(),
                                name=graphene.String())

    def resolve_all_instruments(self, info, **kwargs):
        return Instrument.objects.all()

    def resolve_all_portfolios(self, info, **kwargs):
        return Portfolio.objects.all()

    def resolve_instrument(self, info, **kwargs):
        id = kwargs.get('id')
        symbol = kwargs.get('symbol')

        if id is not None:
            return Instrument.objects.get(pk=id)

        if symbol is not None:
            return Instrument.objects.get(symbol=symbol)

        return None

    def resolve_portfolio(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Portfolio.objects.get(pk=id)

        if name is not None:
            return Portfolio.objects.get(name=name)

        return None


# MUTATIONS #

class CreatePortfolio(graphene.Mutation):

    id = graphene.Int()
    name = graphene.String()
    description = graphene.String()
    holding_value = graphene.Float(required=False)
    total_profit_loss = graphene.Float(required=False)

    class Arguments:
        name = graphene.String(description='Name for Instrument')
        description = graphene.String(description="Symbol for Instrument")
        holding_value = graphene.Float(description="Holding Value for Portfolio",required=False)
        total_profit_loss = graphene.Float(description="Total Profit Loss for Portfolio",required=False)


    class Meta:
        description = "Creates a new Portfolio"

    portfolio = graphene.Field(PortfolioType)

    @staticmethod
    def mutate(self, info, name, description, holding_value=None, total_profit_loss=None):
        portfolio = Portfolio(
            name=name,
            description=description,
            holding_value=holding_value,
            total_profit_loss=total_profit_loss,
        )
        portfolio.save()

        return CreatePortfolio(
            id=portfolio.id,
            name=portfolio.name,
            description=portfolio.description,
            holding_value=portfolio.holding_value,
            total_profit_loss=portfolio.total_profit_loss
        )


class UpdatePortfolio(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    description = graphene.String()

    class Arguments:
        id = graphene.Int(required=True)
        input = PortfolioInput(required=True)

    portfolio = graphene.Field(PortfolioType)

    @staticmethod
    def mutate(root, info, id, input=None):
        portfolio_instance = Portfolio.objects.get(pk=id)
        if portfolio_instance:
            portfolio_instance.name = input.name
            portfolio_instance.description = input.description
            portfolio_instance.save()
            return UpdatePortfolio(portfolio=portfolio_instance)
        return UpdatePortfolio(portfolio=None)


class CreateTrade(graphene.Mutation):

    id = graphene.Int()
    portfolio_id = graphene.Int()
    instrument_id = graphene.Int()
    volume = graphene.Float(required=True)
    buy_value = graphene.Float()
    sell_value = graphene.Float(required=True)
    profit_loss = graphene.Float()

    class Arguments:
        id = graphene.Int()
        portfolio_id = graphene.Int()
        instrument_id = graphene.Int()
        volume = graphene.Float()
        buy_value = graphene.Float()
        sell_value = graphene.Float()
        profit_loss = graphene.Float()

    trade = graphene.Field(TradeType)

    class Meta:
        description = "Creates a new Trade"

    @staticmethod
    def mutate(self, info, portfolio_id, instrument_id, volume, buy_value, sell_value, profit_loss):

        portfolio = Portfolio.objects.get(pk=portfolio_id)
        instrument = Instrument.objects.get(pk=instrument_id)

        if portfolio is None or instrument is None:
            return CreateTrade(trade=None)

        trade = Trade.objects.create(
            portfolio_id=portfolio_id,
            instrument_id=instrument_id,
            volume=volume,
            buy_value=buy_value,
            sell_value=sell_value,
            profit_loss=profit_loss
        )
        trade.save()

        return CreateTrade(
            id=trade.id,
            volume=trade.volume,
            buy_value=trade.buy_value,
            sell_value=trade.sell_value,
            profit_loss=trade.profit_loss
        )

class UpdateTrade(graphene.Mutation):
    id = graphene.Int()
    portfolio_id = graphene.Int()
    instrument_id = graphene.Int()
    volume = graphene.Float()
    buy_value = graphene.Float()
    sell_value = graphene.Float()
    profit_loss = graphene.Float()

    class Meta:
        description = "Updates a trade given a certain id"

    class Arguments:
        id = graphene.Int()
        portfolio_id = graphene.Int()
        instrument_id = graphene.Int()
        volume = graphene.Float()
        buy_value = graphene.Float()
        sell_value = graphene.Float()
        profit_loss = graphene.Float()

    trade = graphene.Field(TradeType)

    @staticmethod
    def mutate(self, info, id, portfolio_id, instrument_id, volume, buy_value, sell_value, profit_loss):
        trade_instance = Trade.objects.get(pk=id)
        if trade_instance:
            trade_instance.portfolio_id = portfolio_id
            trade_instance.instrument_id = instrument_id
            trade_instance.volume = volume
            trade_instance.buy_value = buy_value
            trade_instance.sell_value = sell_value
            trade_instance.profit_loss = profit_loss
            trade_instance.save()
            return UpdateTrade(trade=trade_instance)
        return UpdateTrade(trade=None)


class Mutation(graphene.ObjectType):
    create_portfolio = CreatePortfolio.Field()
    create_trade = CreateTrade.Field()
    update_portfolio = UpdatePortfolio.Field()
    update_trade = UpdateTrade.Field()