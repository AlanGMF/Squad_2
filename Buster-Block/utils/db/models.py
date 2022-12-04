from sqlalchemy import Column, String, Integer, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from connect import Base


class Cities(Base):
    """Table model cities"""
    __tablename__ = 'cities'

    def __init__(self, id_city: int, city: str) -> None:
        self.id_city = id_city
        self.city = city

    # Column information
    id_city = Column(Integer, primary_key=True)
    city = Column(String)
    idcity = relationship('Customers', cascade='all, delete, delete-orphan')


class Customers(Base):
    """Customers table model"""
    __tablename__ = 'customers'

    def __init__(self, id_customer: int, dob: Date, gender: str,
                 age: int, id_city: int) -> None:

        self.id_customer = id_customer
        self.dob = dob
        self.gender = gender
        self.age = age
        self.id_city = id_city

    # Column information
    id_customer = Column(Integer, primary_key=True)
    dob = Column(Date)
    gender = Column(String)
    age = Column(Integer)
    id_city = Column(Integer, ForeignKey('cities.id_city', ondelete='CASCADE'))
    idcustomer = relationship('Transactions',
                              cascade='all, delete, delete-orphan')


class ProductCategories(Base):
    """Model of the product_categories table"""
    __tablename__ = 'product_categories'

    def __init__(self, id_product_category: str,
                 id_category: int, category: str,
                 id_subcategory: int, subcategory: str) -> None:

        self.id_product_category = id_product_category
        self.id_category = id_category
        self.category = category
        self.id_subcategory = id_subcategory
        self.subcategory = subcategory

    # Column information
    id_product_category = Column(String, primary_key=True)
    id_category = Column(Integer, nullable=False)
    category = Column(String)
    id_subcategory = Column(Integer, nullable=False)
    subcategory = Column(String)
    idproductcategory = relationship('Transactions',
                                     cascade='all, delete, delete-orphan')


class StoreTypes(Base):
    """Storetype table model"""
    __tablename__ = 'store_types'

    def __init__(self, id_store_type: int, store_type: str) -> None:

        self.id_store_type = id_store_type
        self.store_type = store_type

    # Column information
    id_store_type = Column(Integer, primary_key=True)
    store_type = Column(String)
    idstoretype = relationship('Transactions',
                               cascade='all, delete, delete-orphan')


class Store(Base):
    """Table model store"""
    __tablename__ = 'stores'

    def __init__(self, id_store: int, store_name: str) -> None:
        self.id_store = id_store
        self.store_name = store_name

    # Column information
    id_store = Column(Integer, primary_key=True)
    store_name = Column(String)
    idstore = relationship('Transactions',
                           cascade='all, delete, delete-orphan')


class Transactions(Base):
    """Transaction Table Model"""
    __tablename__ = 'transactions'

    def __init__(self, transaction_number: int, id_customer: int,
                 transaction_date: Date, id_subcategory: int,
                 id_category: int, quantity: float, rate: float,
                 tax: float, total_amount: float, id_store_type: int,
                 id_store: int, id_product_category: str) -> None:

        self.transaction_number = transaction_number
        self.id_customer = id_customer
        self.transaction_date = transaction_date
        self.id_subcategory = id_subcategory
        self.id_category = id_category
        self.quantity = quantity
        self.rate = rate
        self.tax = tax
        self.total_amount = total_amount
        self.id_store_type = id_store_type
        self.id_store = id_store
        self.id_product_category = id_product_category

    id_transaction = Column(Integer, primary_key=True, autoincrement=True)
    transaction_number = Column(Numeric, nullable=False)

    id_customer = Column(Integer,
                         ForeignKey(
                                    'customers.id_customer',
                                    ondelete='CASCADE'
                                    ),
                         primary_key=True)

    transaction_date = Column(Date)
    id_subcategory = Column(Integer, nullable=False)
    id_category = Column(Integer, nullable=False)
    quantity = Column(Numeric)
    rate = Column(Numeric)
    tax = Column(Numeric)
    total_amount = Column(Numeric)

    id_store_type = Column(Integer,
                           ForeignKey(
                                      'store_types.id_store_type',
                                      ondelete='CASCADE'
                                      ),
                           primary_key=True)

    id_store = Column(Integer,
                      ForeignKey('stores.id_store', ondelete='CASCADE'),
                      primary_key=True)

    id_product_category = Column(String,
                                 ForeignKey(
                                            'product_categories.id_product_category',
                                            ondelete='CASCADE'
                                            ),
                                 primary_key=True)
