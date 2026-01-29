import spade
import random
import asyncio
from spade.behaviour import PeriodicBehaviour

class SensorAgent(spade.agent.Agent):
    class MonitorConditions(PeriodicBehaviour):
        async def run(self):
            disasters = ["Flooding", "Earthquake", "Fire Outbreak", "Gale"]
            locations = ["Sector A-1", "Sector B-4", "Central District", "Riverside"]
            
            event_type = random.choice(disasters)
            location = random.choice(locations)
            severity = random.randint(1, 10)

            print(f"[PERCEPT] {event_type} detected at {location} | Severity: {severity}")
            
            with open("event_logs.txt", "a") as f:
                f.write(f"Type: {event_type} | Location: {location} | Severity: {severity}\n")

    async def setup(self):
        self.add_behaviour(self.MonitorConditions(period=5))

async def main():
    agent = SensorAgent("joshua_dcit403@xmpp.jp", "dcit403")
    await agent.start()
    
    print("SensorAgent is monitoring the environment... ")
    print("Generating logs. Press Ctrl+C to stop after you have enough data.")

    try:
        while True:
            await asyncio.sleep(1) 
    except KeyboardInterrupt:
        await agent.stop()
        print("Stopping agent...")

if __name__ == "__main__":
    spade.run(main())