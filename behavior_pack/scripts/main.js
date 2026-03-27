import { world, system } from "@minecraft/server";
import { ModalFormData } from "@minecraft/server-ui";
import "./hello_test.js";

// Basic join message
world.afterEvents.playerSpawn.subscribe((event) => {
  const { player } = event;
  if (event.initialSpawn) {
    player.sendMessage("Welcome to the Showcase Addon!");
    player.sendMessage("Try using the Magic Wand to open the UI.");
  }
});

// Magic Wand interaction
world.afterEvents.itemUse.subscribe((event) => {
  const { source: player, itemStack } = event;

  if (itemStack.typeId === "custom:magic_wand") {
    const modal = new ModalFormData()
      .title("Magic Wand Menu")
      .textField("What would you like to say?", "I am the master of magic!", "Hello!")
      .toggle("Summon a companion?", true)
      .dropdown("Pick a lucky number", ["1", "2", "3", "4", "5"], 2);

    modal.show(player).then((response) => {
      if (response.canceled) {
        player.sendMessage("You canceled the magic!");
        return;
      }

      const [text, summon, number] = response.formValues;
      player.sendMessage(`You said: ${text}`);
      player.sendMessage(`Your lucky number is: ${number + 1}`);

      if (summon) {
        player.runCommandAsync("summon custom:companion ~ ~ ~");
        player.sendMessage("A companion has appeared!");
      }
    }).catch((err) => {
      console.error("Failed to show form: " + err);
    });
  }
});

system.run(() => {
  console.warn("Showcase Addon Loaded!");
});
