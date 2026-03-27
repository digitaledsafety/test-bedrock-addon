import * as GameTest from "@minecraft/server-gametest";

GameTest.register("HelloWorldTests", "hello_world_message", (test) => {
  const player = test.spawnSimulatedPlayer({ x: 0, y: 2, z: 0 }, "TestPlayer");

  test.print("Running hello_world_message test...");

  // Just a simple test that passes if we get here
  test.succeed();
})
.maxTicks(100)
.structureName("ComponentTests:empty");
