import sc2

from sc2 import run_game, maps, Race, Difficulty, UnitTypeId
from sc2.player import Bot, Computer


class SigmadsenZergBot(sc2.BotAI):
    async def on_step(self, iteration):
        if len(self.gas_buildings) < 1 and self.already_pending(UnitTypeId.EXTRACTOR) == 0:
            placement_position = self.vespene_geyser.closest_to(self.start_location)
            my_drone = self.workers.filter(
                lambda worker: worker.is_collecting or worker.is_idle
            ).closest_to(placement_position)
            my_drone.build_gas(placement_position)


run_game(maps.get("TritonLE"), [
    Bot(Race.Zerg, SigmadsenZergBot()),
    Computer(Race.Terran, Difficulty.VeryEasy)
], realtime=True)
