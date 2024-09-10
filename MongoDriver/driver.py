from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, \
    AsyncIOMotorCollection


class AioMongoDriver:
    """Асинхронный драйвер для MongoDB"""
    def __init__(self, username: str, password: str, host: str, database: str) -> None:
        self._username = username
        self._password = password
        self._host = host
        self._database = database
        
        self.client: AsyncIOMotorClient | None = None
        self.db: AsyncIOMotorDatabase | None = None
        self.collection: AsyncIOMotorCollection | None = None
        self._connect()
        
    def _connect(self) -> None:
        """Подключить базу данных"""
        connect_url = "mongodb+srv://{username}:{password}@{host}/?authSource={database}".format(
            username=self._username, 
            password=self._password, 
            host=self._host, 
            database=self._database
        )
        
        self.client = AsyncIOMotorClient(connect_url)
        self.db = self.client[self._database]
        
    def set_collection(self, collection: str) -> None:
        """Установить коллекцию для работы"""
        self.collection = self.db[collection]
    
    @property
    def admin(self) -> AsyncIOMotorDatabase:
        return self.client.admin
        
    async def insert_one(self, document: dict):
        """Вставить данные в коллекцию"""
        collection = self.db[self.collection]
        result = await collection.insert_one(document)
        return result
    
    async def find_one(self, filter: dict):
        """Получить данные из коллекции"""
        collection = self.db[self.collection]
        result = await collection.find_one(filter)
        return result
    
    async def update_one(self, filter: dict, update: dict):
        """Обновить данные в коллекции"""
        collection = self.db[self.collection]
        result = await collection.update_one(filter, update)
        return result
        
    async def delete_one(self, filter: dict):
        """Удалить данные из коллекции"""
        collection = self.db[self.collection]
        result = await collection.delete_one(filter)
        return result
    
    async def count_documents(self, filter: dict):
        """Получить количество документов в коллекции"""
        collection = self.db[self.collection]
        count = await collection.count_documents(filter)
        return count
