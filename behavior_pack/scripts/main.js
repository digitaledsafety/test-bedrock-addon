import { world, system } from "@minecraft/server";
import "./hello_test.js";

world.afterEvents.playerSpawn.subscribe((event) => {
  const { player } = event;
  if (event.initialSpawn) {
    player.sendMessage("Hello World from the Addon Template!");
  }
});

system.run(() => {
  console.warn("Hello World Addon Loaded!");
});
