# Minecraft Hello World Addon Template

This is a template for a Minecraft Bedrock Edition Addon. It includes a simple behavior pack that says "Hello World" to players when they join, and a basic resource pack.

## Features

- **Behavior Pack (behavior_pack)**: Includes a script that broadcasts a message to players.
- **Resource Pack (resource_pack)**: Basic resource pack linked to the behavior pack.
- **Testing**: Includes a manifest validation script and a GameTest framework sample.
- **CI/CD**: GitHub Action workflow that validates the manifests and builds a `.mcaddon` file.

## Getting Started

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    ```
2.  **Manifest Configuration**:
    Update the `behavior_pack/manifest.json` and `resource_pack/manifest.json` files with your own project names, descriptions, and new UUIDs.

3.  **Local Testing**:
    Run the manifest validation script:
    ```bash
    node scripts/validate_manifests.js
    ```

## Development

-   `behavior_pack/scripts/main.js`: The main logic of your behavior pack.
-   `behavior_pack/scripts/hello_test.js`: Sample GameTest for in-game testing.
-   `resource_pack/pack_icon.png`: The icon for your resource pack.

## Deployment

The GitHub Actions workflow in `.github/workflows/deploy.yml` automatically:
1.  Runs manifest validation on pull requests and pushes to `main`.
2.  Zips the behavior and resource packs into a `.mcaddon` file on pushes to `main`.
3.  Uploads the `.mcaddon` file as a build artifact.

## License

MIT
