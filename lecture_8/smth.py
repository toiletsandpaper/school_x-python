class MosquitoesCloud:
    def __init__(
        self, 
        damage_per_mosquito: float = 1.7, 
        mosquitoes_in_cloud: int = 5
    ):
        if damage_per_mosquito is not None and mosquitoes_in_cloud is not None:
            self.damage_per_mosquito = damage_per_mosquito
            self.mosquitoes_in_cloud = mosquitoes_in_cloud
            self.damage = damage_per_mosquito * mosquitoes_in_cloud
        else:
            raise ValueError('Please provide correct variables')
        
    def __add__(self: 'MosquitoesCloud', other: 'MosquitoesCloud') -> 'MosquitoesCloud':
        new_mosquitoes_cloud = MosquitoesCloud(
            damage_per_mosquito=(
                self.damage_per_mosquito + other.damage_per_mosquito
            ) / 2,
            mosquitoes_in_cloud=self.mosquitoes_in_cloud + other.mosquitoes_in_cloud, 
        )
        return new_mosquitoes_cloud